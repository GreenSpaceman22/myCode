def main():
    
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ")
    print(char_name)
    
    if char_name != "Starlord" or "Mystique" or "Hulk":
        while char_name.capitalize() != "Starlord" or "Mystique" or "Hulk":
            print("That is not one of the characters, try again: ")
            char_name = input().capitalize()
            if char_name == "Starlord" or "Mystique" or "Hulk":
                break

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ")

    while char_stat.lower() != "real name" or "powers" or "archenemy": 
        print("That is not one of the choices, try again: ")
        char_stat = input().lower()
        if char_stat == "real name" or "powers" or "archenemy":
            break
        

    marvelchars= {
        "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

        "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"}
             }

    name = marvelchars.get(char_name)
    name_stat = marvelchars.get(char_name).get(char_stat)
            
    print(f"{char_name}'s {char_stat} is: {name_stat}")
main()

