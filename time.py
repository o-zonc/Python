class Time:
  def __init__(self,hour,min,sec):
    self.day=0
    self.hour=hour
    self.min=min
    self.sec=sec 
  def __add__(self,other):
    temp=Time(0,0,0)
    at=(self.hour*3600+self.min*60+self.sec)+(other.hour*3600+other.min*60+other.sec)
    while at>=86400:
      at=at-86400
      temp.day=temp.day+1
    temp.hour=at//3600
    temp.min=(at%3600)//60
    temp.sec=(at%3600)%60
    return temp
  def __sub__(self,other):
    temp=Time(0,0,0)
    at=(self.hour*3600+self.min*60+self.sec)+(other.hour*3600+other.min*60+other.sec)
    while at<0:
      at=at+86400
      temp.day=temp.day-1
    temp.hour=at//3600
    temp.min=(at%3600)//60
    temp.sec=(at%3600)%60
    return temp
  def __lt__(self,other):
    if (self.hour*3600+self.min*60+self.sec)<(other.hour*3600+other.min*60+other.sec):
      return True
  def __gt__(self,other):
    if (self.hour*3600+self.min*60+self.sec)>(other.hour*3600+other.min*60+other.sec):
      return True
  def __eq__(self,other):
    if (self.hour*3600+self.min*60+self.sec)==(other.hour*3600+other.min*60+other.sec):
      return True
  def __repr__(self):
    return str(self.day)+'일 '+str(self.hour)+'시 '+str(self.min)+'분 '+str(self.sec)+'초 입니다.'
hour=int(input('시 입력'))
min=int(input('분 입력'))
sec=int(input('초 입력'))
first_time=Time(10,10,10)
second_time=Time(hour,min,sec)
add_time=first_time+second_time
sub_time=first_time-second_time
print('두 시간의 합은')
print(add_time)
print('두 시간의 차는')
print(sub_time)
if first_time>second_time:
  print('첫번째 시간이 늦은 시간입니다.')
elif first_time<second_time:
  print('첫번째 시간이 이른 시간입니다.')
else:
  print('두 시간이 같은 시간입니다.')