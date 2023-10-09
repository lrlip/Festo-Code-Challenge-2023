def import_hammer_collection():
    """Import the Hammer collection from file

    Returns:
        dict: dict containg the collection of hammers
    """
    hammer_collection = {}
    with open('1\hammer_collection.txt', 'r') as f:
        for line in f:
            number_hammer = line.split('. ')
            before_after = number_hammer[1].strip().split(' -> ')
            hammer_collection[int(number_hammer[0])] = {'before': before_after[0],
                                                        'after': before_after[1]
                                                        }
    return hammer_collection


def import_hammer_recipe():
    """Import the Hammer recipes

    Returns:
        dict: Dict list containig the recipes for the keys
    """
    recipe = []
    recipes = []
    with open("1\\11_keymaker_recipe.txt", 'r') as recipe_file:
        for line in recipe_file:
            line_recipe = line.split(' - ')
            recipe = []
            for part in line_recipe:
                res = part.strip().replace("(", "").replace(")", "").split(', ')
                recipe.append(res)

            recipes.append(recipe)
    return recipes


hammers = import_hammer_collection()
recipes = import_hammer_recipe()


def apply_hammer(hammer):
    return hammer['after']


def is_valid_recipe(recipe):
    # Function to check if recipe is valid

    key_string = 'A'

    for step in recipe:
        key_list = list(key_string)

        hammer_index, hammer_position = map(int, step)
        # position cannot exceed length of the
        if hammer_position > len(key_string):
            return
        # index cannot exceed number of hammers
        elif hammer_index > len(hammers):
            return
        # Key at the hammer position must be the same as the hammer used
        elif hammers[hammer_index]['before'] != key_string[hammer_position - 1]:
            return
        else:
            # Replace the entry in the list with the hammer
            key_list[hammer_position - 1] = apply_hammer(hammers[hammer_index])
        key_string = ''.join(key_list)
    return key_string


for recipe in recipes:
    key_string = is_valid_recipe(recipe=recipe)
    if key_string:
        print('valid key :', key_string)
        break
