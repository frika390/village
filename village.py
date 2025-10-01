from save import save_data, remove_all_saved_data, create_data, savefile

        
def add_income(incomes: dict, name: str, income_per_week: int) -> dict:  
    """Add a weekly income in incomes."""
    res = {}
    if name in incomes: 
            print("Name already exists. Do you want to overwrite", name,"? (y/n)")
            yes_or_no = input()  
            if yes_or_no == "y": 
                 incomes[name] = income_per_week 
    else: 
        incomes[name] = income_per_week


def remove_income(incomes: dict, name: str) -> None:
    """Remove a weekly income in incomes.""" 
    if name in incomes: 
        incomes.pop(name)


def view_income(incomes):
    """Print all weekly incomes in incomes.""" 
    print("All incomes are:")
    for name, total_income_per_week in incomes.items():
       print(name, ":", total_income_per_week, "gp")


def add_modifier(modifiers:dict, name: str, precentage:int) -> None:
    """Add a modifier of precentage to modifiers."""
    if name in modifiers: 
        print("Name already exists. Do you want to overwrite", name,"? (y/n)")
        yes_or_no = input()  
        if yes_or_no == "y": 
             modifiers[name] = precentage 

    else: 
        modifiers[name] = precentage


def remove_modifier(modifiers:dict, name:str) -> None: 
    """Remove a modifier from modifiers."""
    if name in modifiers: 
        modifiers.pop(name)


def view_modifiers(modifiers:dict) -> None:
    """Print all the modifiers."""
    print("All modifiers are:")
    for name, precentage in modifiers.items():
       print(name, ":", precentage, "%")


def total_income_per_week(incomes:dict, modifiers:dict) -> int:
    """Calculate total income per week and return it."""
    gp_per_week_pos = 0
    expenses = 0
    for income in incomes.values():
        if income > 0:
            gp_per_week_pos += income
        else: 
            expenses += income
    
    modifiers_per_week = 1 + sum(modifiers.values())/100
    return int((gp_per_week_pos * modifiers_per_week) + expenses)


def treasury_add(treasury:int, number:int) -> int:
        """Add gold to treasury. Return treasury with added gold."""
        return treasury + number  


def treasury_remove(treasury:int, number:int) -> int:
    """Remove gold from treasury. Return treasury with removed gold.""" 
    return treasury - number


def treasury_multiply(treasury:int, number:int) -> int: 
    """Multiply treasury with a number. Return multiplied treasury."""
    return round(number * treasury)

def view_treasury(treasury) -> None:
    """Print all the treasury."""
    print("The treasury are: ", treasury)


def treasury_after_weeks(incomes:dict, modifiers:dict, treasury:int, weeks:int) -> int:
    """Calculate the treasury after number of weeks passed with saved incomes and modifiers. 
    Return new treasury.
    """
    new_treasury = treasury + weeks * total_income_per_week(incomes, modifiers)
    return new_treasury

def view_all(incomes, modifiers, treasury): 
    print()
    view_income(incomes)
    print()
    view_modifiers(modifiers)
    print()
    view_treasury(treasury)
    print()


if __name__ == "__main__": 
    incomes = {}

    add_income(incomes, "Farm" , 10)
    assert incomes == {"Farm": 10} 
    remove_income(incomes, "Farm")
    assert incomes == {}

    modifiers = {}
    add_modifier(modifiers, "Golden-sword", 10)
    assert modifiers == {"Golden-sword": 10}
    remove_modifier(modifiers, "Golden-sword")
    assert modifiers == {}

    add_income(incomes, "Farm" , 10)
    add_modifier(modifiers, "Golden-sword", 10)
    assert total_income_per_week(incomes, modifiers) == 11 
    view_modifiers(modifiers)

    treasury = 10
    assert treasury_after_weeks(incomes, modifiers, treasury, 2) == 32
    data = create_data(savefile)
    try:
        treasury = data["treasury"]
        incomes = data["incomes"]
        modifiers = data["modifiers"]
    except KeyError: 
        treasury = 0
        incomes = {}
        modifiers = {}