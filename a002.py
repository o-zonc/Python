def gas(name,**kwarg):
  for key, value in kwarg.items():
    print(type(list(kwarg.items())))

gas('홍길동',국어=90,영어=100,수학=95)
