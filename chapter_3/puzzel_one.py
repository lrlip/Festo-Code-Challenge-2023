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
    
    key = string_A_needs_an_F(key, hammers=hammers)
    
    if key:
        for idx in range(len(key) - 1):
            output = key[idx] + key[idx+1]

            # If hammer exist, assign letter
            if letter := hammers.get(output):
                new_key = replace_hammer_key(key, idx, letter)

                if check_key(new_key, hammers):
                    return True
                else:
                    continue
            else:
                continue
        
def replace_hammer_key(key, idx, replacement):
    return key[:idx] + replacement + key[idx+2:]

def string_E_needs_an_F(key, hammers):
    res_E = [i for i in range(len(key)) if key.startswith('E', i)]
    res_FE = [i for i in range(len(key)) if key.startswith('FE', i)]
    
    if len(res_FE) == len(res_E):
        for i in reversed(res_FE):
            key = replace_hammer_key(key, idx=i, replacement=hammers['FE'] )        
        return key
    
    return False

def read_keys():
    with open('static/31_keymaker_forge_2.txt', 'r') as file:
        keys = file.read().splitlines()
    return keys



def get_correct_key():
    """Read the file and runs the function for all keys"""
    keys = read_keys()

    for key in keys:
        key = string_E_needs_an_F(key, hammers=hammers)
        if key:
            print(key)
            if check_key(key, hammers):
                print('The key you search is:', key)


def string_A_needs_an_F(key, hammers):
    res_AF_FA = []
    res_A = [i for i in range(len(key)) if key.startswith('A', i)]
    res_AF = [i for i in range(len(key)) if key.startswith('AF', i)]
    res_FA = [i  for i in range(len(key)) if key.startswith('FA', i)]
    res_FAF = [i for i in range(len(key)) if key.startswith('FAF', i)]
    res_AFA = [i for i in range(len(key)) if key.startswith('AFA', i)]
    
    res_AF_FA = set(res_AF + [idx + 1 for idx in res_FA])

    # Every A needs a AF or an FA so length A cannot be bigger than set of FA, AF
    if len(res_A) > len(res_AF_FA):
        return None
    
    # An AF can be transformed if not FAF
    res_FAF_not_FA = set(res_FAF) - set(res_FA)
    # an FA can be transformed if not an FAF
    if res_FAF_not_FA:
        for idx in reversed(res_FAF_not_FA):
            key = replace_hammer_key(key, idx=idx, replacement=hammers['FA'])
            
    return key
        
hammers = import_hammer_collection()
print(hammers)
get_correct_key()

# keys = read_keys()
# for idx, key in enumerate(keys[:10]):
#     print(idx, key :=string_E_needs_an_F(key, hammers=hammers))
#     print(idx, string_A_needs_an_F(key, hammers=hammers))
    
    

