import itertools


words = ['muffin','1993','93','beagle','Beagle','Muffin']
combinations = []

for r in range(2, 5):
    combinations.extend(itertools.combinations(words, r))

passwords = [''.join(combination) for combination in combinations][:]

with open("passwords.txt", 'w') as f:
    for password in passwords:
        f.write(password + '\n')
