import re
with open('hunmin.txt', 'r', encoding='utf-8') as hunmin:
    hantext = hunmin.read()

    exp1 = r'[가-힝]{3}'
    re1 = re.findall(exp1, hantext)
    print('exp1: ', re1)

    exp2 = r'[가-힝]+'
    re2 = re.findall(exp2, hantext)
    print('exp2: ', re2)