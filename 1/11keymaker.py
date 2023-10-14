def import_hammer_collection() -> dict(int, dict[str, int]):
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


def apply_hammer(hammer: dict) -> str:
    """Apply a hammer to transform a key segment

    Args:
        hammer (dict): dict representing the hammer

    Returns:
        str: The transformed key segment
    """
    return hammer['after']


def is_valid_recipe(recipe) -> None | str:
    """Checks if a recipe is valid and retuns the resulting key

    Args:
        recipe (list): list of steps representing the recipe

    Returns:
        None | str: the resulting key if valid, otherwise None
    """
    key_string = 'A'

    for step in recipe:
        # split the string to individual letters 'test' --> ['t','e','s','t']
        key_list = list(key_string)

        hammer_index, hammer_position = map(int, step)
        # position cannot exceed length of the
        if hammer_position > len(key_string) or hammer_index > len(hammers):
            return None
        # Key at the hammer position must be the same as the hammer used
        elif hammers[hammer_index]['before'] != key_string[hammer_position - 1]:
            return None
        else:
            # Replace the entry in the list with the hammer
            key_list[hammer_position - 1] = apply_hammer(hammers[hammer_index])
        key_string = ''.join(key_list)
    return key_string


hammers = import_hammer_collection()
recipes = import_hammer_recipe()

# Find and print the valid key string
for recipe in recipes:
    key_string = is_valid_recipe(recipe=recipe)
    if key_string:
        print('valid key :', key_string)
        break
