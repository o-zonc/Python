# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-09-16
# 과제번호: 3주차 1번

count = int(input('몇 마리를 주문하시나요? : '))
chicken = 18000
price = count * chicken

if price >= 100000:
    final_price = price * 0.8
elif price >= 50000:
    final_price = price * 0.9
elif price >= 20000:
    final_price = price + 2000
else:
    final_price = price + 4000

print('결제 금액은 %d 원입니다.'%(final_price))