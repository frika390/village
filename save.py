import ast 

savefile = "save.txt" # Change if name of savefile is changed

def save_value(input_value:str, filename:str) -> None:
    """Write save_value in filename.""" 
    with open(filename, 'w') as f: 
        f.write(input_value)


def load_value(filename:str) -> str: 
    """Return what's in the file of filename."""
    with open(filename, 'r') as f: 
        read = f.read() 
    return read 


def create_data(savefile) -> dict: 
    try: # if anything already saved 
        data = ast.literal_eval(load_value(savefile))
    except: # if nothing is saved
        data = {}
    return data 


def save_data(treasury:int, incomes: dict, modifiers: dict) -> None: 
    """Save the treasury, incomes and modifiers in savefile."""
    user_input = input("Are you sure you want to overwrite your savefile? (y/n) >> ")
    if user_input == "y": 
        data = {}
        data["treasury"] = treasury
        data["incomes"] = incomes 
        data["modifiers"] = modifiers 
        save_value(str(data), savefile) 
        print("Save sucessfull: ", data) 
    else: 
        print("Did not save.")


def remove_all_saved_data() -> None: 
    """Delete all content in savefile."""
    user_input = input("Are you sure you want to delete your savefile? (y/n) >> ")
    if user_input == "y": 
        save_value("", savefile)
        print("All data cleared.") 
    else: 
        print("Did not wipe data.")

if __name__ == "__main__": 
    treasury = 10
    modifiers = {}
    incomes = {}

    save_data(treasury, incomes, modifiers)
    remove_all_saved_data()