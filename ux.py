from village import * 

running = True 

data = create_data(savefile)
try:
    treasury = data["treasury"]
    incomes = data["incomes"]
    modifiers = data["modifiers"]
except KeyError: 
    treasury = 0
    incomes = {}
    modifiers = {}

print("Welcome to village calculator! Type h: to see the commands available!")

while running: 
    view_all(incomes, modifiers, treasury) 

    choice = input("Write what you want to do: ")

    if choice == "h": 
        print( """
                q - quit without saving 

                Weekly modfiers:
                ma - add a weekly modifier 
                mr - remove a weekly modifier 
                mv - view the current weekly modifiers 

                Weekly income: 
                ia - add a weekly income 
                ir - remove a weekly income 
                iv - view the current weekly incomes 

                w - view total weekly income with modifiers applied 

                Treasury: 
                ta - add an amount of gp to the treasury 
                tr - remove an amount of gp from the treasury 
                tv - view treasury
                tm - multiply treasury with a number 

                Simulate:
                sw - simulate nr of week(s) and adds the income to the treasury 
              
                Save mangement: 
                s - save the added modfiers, treasury and incomes 
                delete - delete all saved data 
                """
              )
    elif choice == "ma":
        name = input("Choose a name for a weekly modifer: ")
        nr = input("Choose a precentage: ")
        add_modifier(modifiers, name, int(nr)) 
        print(name, "was added to the weekly modfiers!")
    
    elif choice == "mr": 
        name = input("Choose a name for weekly modifer: ") 
        nr = input("Choose a precentage: ")
        remove_modifier(modifiers, name) 
        print(name, "was removed from the weekly modfiers!")
    
    elif choice == "mv": 
        view_modifiers(modifiers)

    elif choice == "ia": 
        name = input("Choose a name for weekly income: ") 
        nr = input("Choose an amount of gp: ")
        add_income(incomes, name, int(nr))
        print(name, "was added to the weekly modfiers!")
    
    elif choice == "ir": 
        name = input("Choose a name for weekly income: ") 
        nr = input("Choose an amount of gp: ")
        remove_income(incomes, name) 
        print(name, "was removed from the weekly income!")

    elif choice == "iv": 
        view_income(incomes)
    
    elif choice == "w": 
        print("Total weekly income is: ", total_income_per_week(incomes, modifiers), "gp")

    elif choice == "ta": 
        nr = input("Enter amount to add to treasury: ")
        treasury = treasury_add(treasury, int(nr))
        print("Treasury added with ", nr)

    elif choice == "tr": 
        nr = input("Enter amount to remove from treasury: ")
        treasury = treasury_remove(treasury, int(nr))
        print("Treasury added with ", nr)
    
    elif choice == "tm": 
        nr = input("Enter a number to multiply from treasury: ")
        treasury = treasury_remove(treasury, int(nr))
        print("Treasury multiplied with ", nr)
    
    elif choice == "tv": 
        view_treasury(treasury)

    elif choice == "sw": 
        weeks = input("Enter how many weeks you want to simulate: ")
        treasury = treasury_after_weeks(incomes, modifiers, treasury, int(weeks))
        print(weeks, " weeks simulated and added to treasury.")

    elif choice == "s": 
        save_data(treasury, incomes, modifiers)
    
    elif choice == "delete": 
        remove_all_saved_data()
        modifiers ={}
        treasury = 0 
        incomes = {}
    
    elif choice == "q":
        running = False
    
    else: 
        print("Please select one of the commands listed under h.")