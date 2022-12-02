# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-11-04
# 과제번호: 10주차 1번

print('어떤 노래를 선택할까요?\n "새삥", "After LIKE", "Hype Boy", "강남스타일"')
song = input("입력: ")
song = song.lower()

if song == "새삥":
    with open("새삥.txt", "r", encoding="utf-8") as newthx:
        txt = newthx.readlines()
elif song == "after like":
    with open("After Like.txt", "r", encoding="utf-8") as al:
        txt = al.readlines()
elif song == "hype boy":
    with open("Hype Boy.txt", "r", encoding="utf-8") as Hb:
        txt = Hb.readlines()
elif song == "강남스타일":
    with open("강남스타일.txt", "r", encoding="utf-8") as gangnam:
        txt = gangnam.readlines()
else:
    raise Exception(f"{song}(이)라는 노래는 목록에 없습니다.")


li = []
con = []
for line in txt:
    li.append(line.strip('\n'))
for words in li:
    con.extend(words.split(" "))

while True:
    word = input("가사에서 어떤 단어를 찾고 싶으신가요? : ")
    if word == "":
        print("단어 개수 찾기 프로그램을 종료합니다.")
        break
    cnt = 0
    for words in con:
        if word in words:
            cnt += 1
        else:
            continue
    if cnt > 0:
        print(f'노래 "{song}"에서 "{word}"라는 가사는 {cnt}번 등장합니다.')
    else:
        print('가사가 없습니다')