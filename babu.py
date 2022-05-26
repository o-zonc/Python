calories = {
    'ham':100,
    'avocado':60,
    'mayo':80,
    'egg':40,
    'bacon':160,
    'tomato':20,
    'lettuce':30,
    'cheese':40
}

menu = ['ham egg mayo','ham tomato egg','ham avocado','ham cheese','ham egg','bacon cheese tomato egg','bacon mayo','bacon lettuce tomato']

def get_ing_sandwich(calories, menu, selected_ingredient):
    selectedmenu = []
    totalcalories = []
    for i in range(len(menu)): # selected_ingredient가 포함된 샌드위치 추출
        if selected_ingredient in menu[i]:
            selectedmenu.append(menu[i])
    for j in range(len(selectedmenu)): # 샌드위치 칼로리 계산
        cal = 0      
        for keys, values in calories.items():
            if keys in selectedmenu[j]:
                cal += values
        totalcalories.append(cal)
    min_calorie = min(totalcalories)
    max_calorie = max(totalcalories)
    return min_calorie, max_calorie

selected_ingredient = input("Ingredient: ")
min_calorie, max_calorie = get_ing_sandwich(calories, menu, selected_ingredient)

print(min_calorie, max_calorie)
