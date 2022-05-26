def Diamond_Left(aurum, ferrum):
    Au = aurum // 2
    Fe = ferrum // 3
    def min(a, b):
        if a <= b:
            return a
        else:
            return b
    diamond = min(Au, Fe)
    gold = aurum - diamond * 2
    iron = ferrum - diamond * 3
    return diamond, gold, iron

# ---------------------------------------------------------------------------------------------------------

gold_and_iron = input('Number of gold&iron: ')
list_GNI = gold_and_iron.split(' ')
diamond, gold, iron = Diamond_Left(int(list_GNI[0]), int(list_GNI[1]))
print('Diamond: {diamond}, Gold: {gold}, Iron: {iron}'.format(diamond = diamond, gold = gold, iron = iron))