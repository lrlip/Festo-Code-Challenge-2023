
def inAlphabeticOrder(string):
    return string == ''.join(sorted(string))


with open('./static/01_keymaker_ordered.txt', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    if inAlphabeticOrder(line):
        print('Week 0.1: answers is:', line)
