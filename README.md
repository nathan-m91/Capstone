**Poké Capstone**

![image](https://github.com/user-attachments/assets/2579fc30-04bb-4b56-b1e7-f0e2a7f057fa)

Welcome to my Pokémon dojo! This project will use datasets to look at competitive Pokémon data. This will also allow you to see the type(s), movesets, abilities, and base stats (HP, ATK, etc.) of the Pokémon to help with crafting a competitive team of your own! You'll be able to search each Pokémon by name and it will provide specific Pokémon type, abilities that can be learned, and even all valid moves it can learn. 

What if you're looking for a bulky support Pokémon to complement your quick physical sweeper Pokémon? Look no further as you can check out the base stats of Pokémon to pick the right partner to start your team. This code will also give the option to check the top 5 Pokémon for each stat!

Once you run the code, it will ask you for some input (pokemon name, etc.) Once inputted, it will output the info relevant to the Pokémon. After your done, it will ask again if you'd like to see the top 5 Pokémon for each stat. This is a good way to know what is the best for the stats you're looking for.


To run this project, you can open the Pokémon.py file. I've notated each section of the code thoroughly to make sure its easily understandable. In lines 36 and 37 I've commented it out so it doesn't spam you with cleaned data thats already in the project under the Cleaned Data folder. If you'd like to test that part out too, just uncomment it and it should work! I've added sample data of what the finished csv looks like when its created. Yours may differ depending on what Pokémon you enter into the query :)

If you're here for the quick rundown of the top Pokemon for each stat, you can head over to the Plots for Stats folder as it graphs out the top 5 Pokemon for each stat (HP, ATK, etc.) Surprisingly the top 5 for each stat aren't all legendary Pokemon!

https://github.com/nathan-m91/Capstone/tree/main/Plots%20for%20Stats





**Sources for the data**

This uses three csvs from the below link

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
