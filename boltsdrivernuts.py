"""
Use this!!
Bolt : ▼│↓
Nut : ◎
Driver : ■■─→
"""

def bolts_count(toolbox_name):
    bolts_num = 0
    toolbox_name.replace('\n','')
    toolbox_name.replace(' ','')
    for i in range(len(toolbox_name) - 62):
        if toolbox_name[i] == '▼' and toolbox_name[31 + i] == '│' and toolbox_name[62 + i] == '↓':
            bolts_num += 1
    return bolts_num

def nuts_count(toolbox_name):
    nuts_num = toolbox_name.count('◎')
    return nuts_num

def drivers_count(toolbox_name):
    drivers_num = toolbox_name.count('■■─→')
    return drivers_num

sample_num = int(input('Choose toolbox : '))
samples = ['toolbox0.txt','toolbox1.txt','bolt.txt','nut.txt','driver.txt']

with open("data/" + samples[sample_num], 'r', encoding='utf8') as f:
    toolbox_name = f.read()

print("Bolts:",bolts_count(toolbox_name))
print("Nuts:",nuts_count(toolbox_name))
print("Drivers:",drivers_count(toolbox_name))