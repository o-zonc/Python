import random #random 모듈을 임포트해주새오

sum = 0 #이게 없으면 작동이 안돼오
for j in range(3): #3번 반복해 주새오
  maxint = random.randint(0,10) #0부터 10까지의 정수 랜덤으로 지정할 거애오
  print(j+1,'번째 시행. 임의의 정수:',maxint) #갓챠한 정수를 표시해주새오
  if maxint <= 1: #랜덤으로 지정된 정수가 0,1일때 수행할 명령이애오
    sum += 0
  else: #랜덤으로 지정된 정수가 2보다 클 때 명령이애오
    for k in range(2,maxint+1): #2부터 랜덤으로 지정한 정수까지 반복할 거애오
      p = True #소수라면 그대로 True로 남아있게 코드를 짤 거애오
      for i in range(2,k): #2부터 k 전까지 반복할 거애오
        if k % i == 0: #나눠보는 것이애오
          p = False #한번이라도 나누어지면 소수가 아니애오
      if p == True: #소수라면
        print('소수:',k) #표시해주새오
        sum += k #그리고 더해주새오
  print('') #한칸 띄워주새오

print('sum:',sum) #결과를 표시해주새오