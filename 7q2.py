def report_score5(sclist, aver, max=30, min=6):# default arguement
    print("성적 : ", sclist)
    print("평균 : ", aver)
    print("최고범위 : ", max, ", 최하범위 : ", min)

scorelist = [78, 56, 67, 95, 82]
my_aver = sum(scorelist) / len(scorelist)
my_max = max(scorelist)
my_min = min(scorelist)

report_score5(scorelist,my_aver)
print("-------")
report_score5(scorelist,my_aver,min=3)
print("-------")
report_score5(scorelist,my_aver,max=105,min=50)