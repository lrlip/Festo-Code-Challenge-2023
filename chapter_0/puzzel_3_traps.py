DEACTIVE = ['inactive',
            'disabled',
            'quiet',
            'standby',
            'idle']

ACTIVE = ['live',
          'armed',
          'ready',
          'primed',
          'active']

FLIPPED = ['flipped',
           'toggled',
           'reversed',
           'inverted',
           'switched']

test_file = 'static/03_trap_logs_test.txt'
file = 'static/03_trap_logs.txt'


def file_to_dict(filename):
    trap_dict = {}
    with open(filename) as f:
        file = f.read().splitlines()
        for line in file:
            (key, val) = line.split(':')
            trap_dict[int(key)] = val.strip()
    return trap_dict


def getTrapStateSum(traps: str):
    """Get the trap log and turns it in the 

    Args:
        traps (_type_): _description_

    Returns:
        _type_: _description_
    """

    trap_sum = 0
    for idx in traps:
        trap_state = 0
        log = traps[idx].split()
        for state in log:
            if state in DEACTIVE:
                trap_state = -1
            elif state in ACTIVE:
                trap_state = 1
            elif state in FLIPPED:
                trap_state = trap_state * (-1)

        if trap_state == -1:
            trap_sum += idx
    return trap_sum


traps = file_to_dict(filename=file)

trap_sum = getTrapStateSum(traps=traps)
print('The sum of the trap is:', trap_sum)
