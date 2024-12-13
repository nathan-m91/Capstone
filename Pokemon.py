import pandas as pd
import sqlite3

# Load the data
pokedex_df = pd.read_csv('pokedex.csv')
valid_moves_df = pd.read_csv('valid_moves.csv')
all_moves_df = pd.read_csv('all_moves.csv')

# Data cleanup
all_moves_df = all_moves_df.drop(columns=['IsNonstandard'], axis=1)
pokedex_df = pokedex_df.drop(columns=['Gendered', 'Total', 'height', 'weight', 'prevo'], axis=1)
pokedex_df = pokedex_df.rename(columns={'ability_0': 'Ability1', 'ability_1': 'Ability2', 'ability_H': 'HiddenAbility'})
valid_moves_df = valid_moves_df.loc[:, ~valid_moves_df.columns.str.contains('^Unnamed')]
valid_moves_df.columns = ["Pokemon", "Move"]

# Stripping and making all strings lowercase for easier merge
valid_moves_df['Pokemon'] = valid_moves_df['Pokemon'].str.lower().str.strip()
valid_moves_df['Move'] = valid_moves_df['Move'].str.lower().str.strip()
all_moves_df['Name'] = all_moves_df['Name'].str.lower().str.strip()
pokedex_df['Name'] = pokedex_df['Name'].str.lower().str.strip()

# Merging all_moves_df and valid_moves_df for easier SQL queries
merged_moves_df = pd.merge(
    valid_moves_df,
    all_moves_df,
    left_on="Move",
    right_on="Name",
    how="inner"  
)
merged_moves_df = merged_moves_df.drop(columns=['Name'], axis=1)

# Create SQL and move dfs to the db
con = sqlite3.connect("poke_dojo.db")
pokedex_df.to_sql("pokedex", con, index=False, if_exists="replace")
merged_moves_df.to_sql("detailed_moves", con, index=False, if_exists="replace")
con.execute("DROP INDEX IF EXISTS idx_pokedex_name;")
con.execute("CREATE INDEX idx_pokedex_name ON pokedex(Name);")
con.execute("DROP INDEX IF EXISTS idx_detailed_moves;")
con.execute("CREATE INDEX idx_detailed_moves ON detailed_moves(Pokemon);")


#Start of the Queries in SQL to find the data wanted. 
#This will ask for an input of what Pokemon
results = []
while True:
    try:
        name = input("Enter the name of the Pokémon you'd like to check!: ").strip().lower()
        print(f"Searching for Pokémon: '{name}'")

        # Query to get the Pokémon stats and abilities
        stats_query = f"""
        SELECT 
            Name AS Name, 
            Type1, 
            Type2,  
            HP, ATK, DEF, SPA, SPD, SPE,  
            Ability1, 
            Ability2,
            HiddenAbility
        FROM pokedex
        WHERE LOWER(Name) = '{name}';
        """
        stats_df = pd.read_sql_query(stats_query, con)

        # Query to get the moves for the Pokémon
        moves_query = f"""
        SELECT 
            v.Move, 
            v.Accuracy, 
            v.BasePower, 
            v.Category, 
            v.Type AS MoveType
        FROM detailed_moves v
        WHERE LOWER(v.Pokemon) = '{name}';
        """
        moves_df = pd.read_sql_query(moves_query, con)

        # Results of the query. Will let you know if it couldn't find the Pokemon in the list.
        # If it does find the Pokemon, it will print the stats, abilities, and moves of that Pokemon
        if stats_df.empty:
            print(f"No stats found for Pokémon '{name}'. Please check the name and try again.")
        elif moves_df.empty:
            print(f"No moves found for Pokémon '{name}'. Please check the name and try again.")
        else:
            # Create a header row for Pokémon stats
            stats_header = list(stats_df.columns)
            stats_values = stats_df.iloc[0].tolist()

            # Combining stats header and values
            combined_stats = [stats_header, stats_values]

            # Added a separator row for clarity
            separator_row = ["---"] * len(stats_header)

            # Combining moves header and values
            moves_header = list(moves_df.columns)
            moves_values = moves_df.values.tolist()
            combined_moves = [moves_header] + moves_values

            # Merge stats, separator, and moves into one final structure
            final_output = combined_stats + [separator_row] + combined_moves
            results_df = pd.DataFrame(final_output)
            results.append(results_df)

            # Print result
            print(f"Details for Pokémon '{name}':")
            print(results_df)

        # Ask the user if they want to query another Pokémon
        another_query = input("Check more Pokemon? (yes/no): ").strip().lower()
        if another_query != 'yes':
            break

    except Exception as e:
        print(f"An error occurred: {e}")
        continue  # Continue asking for the next Pokémon name if there's an error

#Combining all results into a single CSV so you can see all data in Excel rather than through vscode
if results:
    final_df = pd.concat(results, ignore_index=True)
    final_df.to_csv("all_pokemon_details.csv", index=False)
    print(f"All results saved to 'all_pokemon_details.csv'.")
else:
    print("No results to save.")

