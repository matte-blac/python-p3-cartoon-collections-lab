def roll_call_dwarves(dwarf_names):
    # prints dwarf names in numbered order
    for index, dwarf_names in enumerate(dwarf_names, start = 1):
        print(f'{index}. {dwarf_names}')
    pass

def summon_captain_planet(planeteer_calls):
    # capatalizes calls and adds '!'
    capitalized_calls = [call.capitalize() + '!' for call in planeteer_calls]
    return capitalized_calls
pass

def long_planeteer_calls(planateer_calls):
    # checks if any call is longer than 4 characters
    return any(len(call) > 4 for call in planateer_calls)
pass

def find_the_cheese(ingredients):
    # finds first cheese in list
    cheese_types = ["cheddar", "gouda", "camembert"]
    for ingredient in ingredients:
        if ingredient in cheese_types:
            return ingredient
    # if non-existent, returns null
    return None
pass