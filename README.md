**Poké Capstone**

![image](https://github.com/user-attachments/assets/2579fc30-04bb-4b56-b1e7-f0e2a7f057fa)

Welcome to my Pokémon dojo! This project will use datasets to look at competitive Pokémon data. This will also allow you to see the type(s), movesets, abilities, and base stats (HP, ATK, etc.) of the Pokémon to help with crafting a competitive team of your own! You'll be able to search each Pokémon by name and it will provide specific Pokémon type, abilities that can be learned, and even all valid moves it can learn. 

**Questions Answered By The Code**

This code can be used to answer a few questions:
1. _Which Pokémon has the best base stats?_
2. _What moves can the Pokémon learn?_
3. _What abilities can be learned for each Pokémon?_

Look no further as you can check out the base stats, abilities, and moves of Pokémon to pick the right partner to start your team. This code will also give the option to check the top 5 Pokémon for each stat!


**Running Pokemon.py**

To run this project, you can open the Pokemon.py file. I've notated each section of the code thoroughly to make sure its easily understandable. In lines 36 and 37 I've commented it out so it doesn't spam you with cleaned data thats already in the project under the Cleaned Data folder. If you'd like to test that part out too, just uncomment it and it should work! I've added sample data of what the finished csv looks like when its created. This would be located in the Saved Data folder. Yours may differ depending on what Pokémon you enter into the query :)

Once you run the code, it will ask you for some input (pokemon name you'd like to search) Once inputted, it will output the info relevant to the Pokémon. It will then ask if you'd like to search for another Pokémon. You can either say yes or no. After you're done searching for Pokémon, it will ask again if you'd like to see the top 5 Pokémon for each stat. This is a good way to know what is the best for the stats you're looking for.

If you're here for the quick rundown of the top Pokémon for each stat, you can head over to the Plots for Stats folder as it graphs out the top 5 Pokémon for each stat (HP, ATK, etc.) Surprisingly the top 5 for each stat aren't all legendary Pokémon!

https://github.com/nathan-m91/Capstone/tree/main/Plots%20for%20Stats





**Sources for the data**

This uses the pokedex.csv, moves.csv, and valid_moves.csv from the below link

https://www.kaggle.com/datasets/jakejoeanderson/pokemon-stats-valid-moves-more?select=valid_moves.csv



**Creating a virtual environment to run the code**

There are a few packages that need to be installed. I've listed these in the requirements.txt file. I'd recommend setting up a virtual environment so you can pip install the packages!
To do this, please follow the below terminal commands. It may be best to open the terminal from the folder where this project is cloned so you don't have to cd for the requirements.

_Linux/macOS:_

>python3 -m venv venv

_Windows:_

>python -m venv venv

**To activate the virtual environment.**

_Linux//macOS:_

>source venv/bin/activate

_Windows:_

>venv/Scripts/activate

**To install the packages listed in the requirements.txt file:**

>pip install -r requirements.txt

**To leave this virtual environment:**

>deactivate


**Project Requirements**

1. _Loading data_
  * I loaded in three CSV files to analyze.
2. _Clean and operate on the data while combining them._
  * I removed unneccesary columns from the data in the CSVs then renamed some columns to make it easier to read. I also made all columns lowercase to make it easier to merge and query in SQL. The all_moves.csv and valid_moves.csv were merged to keep on moves that matched in both of the CSVs. I then removed the redundant columns. The merged CSV and the cleaned pokdex.csv files were saved and moved to the Cleaned Data folder in this project. When running this, it will prompt for a pokemon name which will then run the queries I created in SQL to pull the relevant data before saving it to a csv for later use.
3. _Visualize / Present your data._
  * I created 6 matplotlib graphs of the top 5 Pokémon for each base stat (HP, ATK, etc.) This is to help visualize which Pokémon are the top when you're searching for a new addition to your Pokémon team. All graphs were saved in Plots for Stats with the name associated to the top five of that Stat.
4. _Best Practices_
  * I've listed the steps on how to create/run a virtual environment on a local computer. This prevents the packages required from having to be installed on the computer itself and can be deactivated after running the data.
5. _Interpret Your Data_
  * The Pokemon.py file has been fully notated with what each set of code is doing. In the README above, I also notated what the code does and some quirks of the code. I've also saved the output of what the code will do in the Saved Data folder as another visualization for what to expect from running this.
