def import_hammer_collection() -> dict():
    """Import the Hammer collection from file

    Returns:
        dict: dict containg the collection of hammers
    """
    hammer_collection = {}
    with open('static\hammer_collection.txt', 'r') as f:
        for line in f:
            number_hammer = line.split('. ')
            before_after = number_hammer[1].strip().split(' -> ')
            hammer_collection[before_after[1]] = before_after[0]
    return hammer_collection


def check_key(key: str,
              hammers: dict,
              ) -> bool:
    if len(key) == 1:
        # Length 1 must be A
        return key[0] == 'A'

    for idx in range(len(key) - 1):
        output = key[idx] + key[idx+1]

        # If hammer exist, assign letter
        if letter := hammers.get(output):
            new_key = key[:idx] + letter + key[idx+2:]

            if check_key(new_key, hammers):
                return True
            else:
                continue
        else:
            continue


def get_correct_key():
    """Read the file and runs the function for all keys"""
    with open('static/21_keymaker_forge.txt', 'r') as file:
        keys = file.read().splitlines()

    for key in keys:
        if check_key(key, hammers):
            print('The key you search is:', key)


hammers = import_hammer_collection()
get_correct_key()
