from time import sleep
from cmath import sqrt

print('')
print('This program was developed with Python 3.10.2 64-Bit...')
sleep(2)
print('If you let me know the coefficients of equation, I can solve it for you.')
sleep(2)
print('')
gree=input('Linear: press [1] / Quadratic: press [2] / Cubic: press [3] / Quartic: press [4] / Help: press [9] | ')
EQdeg=int(gree)
while type(gree)!=int:
  print('That input is not available.')
  print('')
  gree=input('Linear: press [1] / Quadratic: press [2] / Cubic: press [3] / Quartic: press [4] / Help: press [9] | ')
  if type(gree)==int:
    EQdeg=int(gree)
    break      
ansErr=0
print('')

while True:
  if EQdeg==1:
    d=float(input('a from ax+b=0 | '))
    e=float(input('b from ax+b=0 | '))
    if d==0:
      if e==0:
        ansErr=2
      else:
        ansErr=3
    else:
      x1=e/d

  if EQdeg==2:
    c=float(input('a from ax^2+bx+c=0 | '))
    d=float(input('b from ax^2+bx+c=0 | '))
    e=float(input('c from ax^2+bx+c=0 | '))
    if c==0:
      ansErr=12
    else:
      ansErr=90
      sqr=(d**2)-(4*c*e)
      x1=((-1*d)+sqrt(sqr))/(2*c)
      x2=x1+(d/c)
      if x1==x2:
        EQdeg=72
      else:
        EQdeg=2

  if EQdeg==3:
    b=float(input('a from ax^3+bx^2+cx+d=0 | '))
    c=float(input('b from ax^3+bx^2+cx+d=0 | '))
    d=float(input('c from ax^3+bx^2+cx+d=0 | '))
    if d==42:
      print("Hey! You'd better read 'The Hitchhiker's Guide to the Galaxy'!")
    e=float(input('d from ax^3+bx^2+cx+d=0 | '))
    if b==0:
      ansErr=13
    else:
      ansErr=90
      p=-1*(c/(3*b))
      q=2*((c)**3)-9*b*c*d+27*(b**2)*e
      r=4*(((c**2)-3**b*d)**3)
      s=sqrt((q**2)-r)
      cbrtp=((q+s)/2)**(1/3)
      cbrtn=((q-s)/2)**(1/3)
      wp=(1+complex(0,(3)**(0.5)))/(6*b)
      wn=(1-complex(0,(3)**(0.5)))/(6*b)
      x1=p-(1/(3*b))*cbrtp-(1/(3*b))*cbrtn
      x2=p+wp*cbrtp+wn*cbrtn
      x3=p+wp*cbrtn+wn*cbrtp
      if x1==x2 and x2==x3:
        EQdeg=731
      elif x1!=x2 and x2!=x3 and x3!=x1:
        EQdeg=3
      else:
        EQdeg=732

  if EQdeg==4:
    a=float(input('a from ax^4+bx^3+cx^2+dx+e=0 | '))
    if a==42:
      print("Oh, that's a really interesting number...!")
    b=float(input('b from ax^4+bx^3+cx^2+dx+e=0 | '))
    c=float(input('c from ax^4+bx^3+cx^2+dx+e=0 | '))
    d=float(input('d from ax^4+bx^3+cx^2+dx+e=0 | '))
    e=float(input('e from ax^4+bx^3+cx^2+dx+e=0 | '))
    if a==0:
      ansErr=14
    else:
      ansErr=90
      p=b/(4*a)
      q=(2*c)/(3*a)
      r=(c**2)-(3*b*d)+(12*a*c)
      s=(2*(c**2))-(9*b*c*d)+(27*a*(d**2))+(27*e*(b**2))-(72*a*c*e)
      t=-((b**3)/(a**3))+((4*b*c)/(a**2))-((8*d)//a)
      v=((2*(1/3))*r)/(3*a*((s+((-4*(r**3)+s**2)**0.5)**(1/3))))+(s+((-4*(r**3)+s**2)**0.5)**(1/3))/(3*(2**(1/3))*a)
      f=sqrt(4*(p**2)-q+v)/2
      g=sqrt(8*(p**2)-2*q-v-t/(4*((4*(p**2)-q+v)**0.5)))/2
      x1=-p-f-g
      x2=-p-f+g
      x3=-p+f-g
      x4=-p+f+g
      if x1==x2 and x2==x3 and x3==x4:
        EQdeg=741
      if x1!=x2 and x2!=x3 and x3!=x4 and x4!=x1:
        EQdeg=4
      else:
        if x1==x2 and x3!=x4:
          EQdeg=742
          if x2==x3:
            x2=x4
          if x2==x4:
            x2=x3
        else:
          EQdeg=743
          if x1==x2:
            x2=x3
            x3=x4
          if x1==x3 or x2==x3:
            x3=x4
          else:
            x4=x4

  while EQdeg==9:
    saint=input('print help pages: press [1] [2] [3] / to get out: press [0]')
    if type(saint)!=float:
      print('That input is not available.')
    st=float(saint)
    if st==1:
      print('-'*79)
      print('<Developer>')
      print('이경환')
      print('instagram @8taby')
      print('-'*79)
    if st==2:
      print('-'*79)
      print('<<EQdeg code legend>>')
      print('-'*79)
      print('EQdeg==1      | linear equation')
      print('EQdeg==2      | quadratic equation')
      print('EQdeg==3      | cubic equation')
      print('EQdeg==4      | quartic equation')
      print('EQdeg==5      | plainpath')
      print('EQdeg==6      | ...')
      print('EQdeg==7xx    | multiple root detacted')
      print(  'EQdeg==72   | [Quad] for only root')
      print(  'EQdeg==731  | [Cub] for only root')
      print(  'EQdeg==732  | [Cub] for two different roots')
      print(  'EQdeg==741  | [Quar] for only root')
      print(  'EQdeg==742  | [Quar] for two different roots')
      print(  'EQdeg==743  | [Quar] for three different roots')
      print('EQdeg==8      | ...')
      print('EQdeg==9      | help')
      print('-'*79)
    elif st==3:
      print('-'*79)
      print('<<ansErr code legend>>')
      print('-'*79)
      print('ansErr==1x    | equation degree conflict')
      print('  ansErr==12  | [Quad]')
      print('  ansErr==13  | [Cub]')
      print('  ansErr==14  | [Quar]')
      print('ansErr==2     | indeterminate')
      print('ansErr==3     | inconsistent')
      print('ansErr==4     | ...')
      print('ansErr==5     | ...')
      print('ansErr==6     | ...')
      print('ansErr==7     | ...')
      print('ansErr==8     | ...')
      print('ansErr==9x    | no error exists')
      print('  ansErr==90  | comments')
      print('  ansErr==99  | break')
      print('-'*79) 
    elif st==0:
      print('putting down help...')
      sleep(2)
      print('')
      EQdeg=int(input('Linear: press [1] / Quadratic: press [2] / Cubic: press [3] / Quartic: press [4] / Help: press [9] | '))
      while type(gree)!=int:
        print('That input is not available.')
        print('')
        gree=input('Linear: press [1] / Quadratic: press [2] / Cubic: press [3] / Quartic: press [4] / Help: press [9] | ')
        if type(gree)==int:
          EQdeg=int(gree)
          break      
      break
    else:
      print('That page has not been written...')

  if ansErr==14:
    sleep(1)
    print('...')
    print('Run in Lower Degree Mode...')
    sleep(1)
    if b==0:
      ansErr=13
    else:
      ansErr=90
      p=-1*(c/(3*b))
      q=2*((c)**3)-9*b*c*d+27*(b**2)*e
      r=4*(((c**2)-3**b*d)**3)
      s=sqrt((q**2)-r)
      cbrtp=((q+s)/2)**(1/3)
      cbrtn=((q-s)/2)**(1/3)
      wp=(1+complex(0,(3)**(0.5)))/(6*b)
      wn=(1-complex(0,(3)**(0.5)))/(6*b)
      x1=p-(1/(3*b))*cbrtp-(1/(3*b))*cbrtn
      x2=p+wp*cbrtp+wn*cbrtn
      x3=p+wp*cbrtn+wn*cbrtp
      if x1==x2 and x2==x3:
        EQdeg=731
      elif x1!=x2 and x2!=x3 and x3!=x1:
        EQdeg=3
      else:
        EQdeg=732

  if ansErr==13:
    sleep(1)
    print('...')
    print('Run in Lower Degree Mode...')
    sleep(1)
    if c==0:
      ansErr=12
    else:
      ansErr=90
      sqr=(d**2)-(4*c*e)
      x1=((-1*d)+sqrt(sqr))/(2*c)
      x2=x1+(d/c)
      if x1==x2:
        EQdeg=72
      else:
        EQdeg=2

  if ansErr==12:
    sleep(1)
    print('...')
    print('Run in Lower Degree Mode...')
    sleep(1)
    if d==0:
      if e==0:
        ansErr=2
      else:
        ansErr=3
    else:
      Lx=e/d
      ansErr=90

  if ansErr==2:
    print('')
    print('ERROR: INDETERMINATE')
    sleep(1)
    print('Given equation is indeterminate.')
    print('ALL complex number meets the equation.')
    sleep(2)
    print('')
    EQdeg=input('Linear: press [1] / Quadratic: press[2] / Cubic: press[3] / Quartic: press[4] / help: press [9] | ')

  if ansErr==3:
    print('')
    print('ERROR: INCONSISTENT')
    sleep(1)
    print('Given equation is inconsistent.')
    print('NO division by 0 is permitted.')
    sleep(2)
    print('')
    EQdeg=input('Linear: press [1] / Quadratic: press[2] / Cubic: press[3] / Quartic: press[4] / help: press [9] | ')

  if ansErr==90:
    print('')
    print("I'm now calculating...")
    sleep(3)
    print("Yes! I found the answer!")
    sleep(2)
    print("You'd like to know it, right?")
    sleep(2)
    re=input("Yes: press [y] / No: press [n] | ")
    rel=re.lower()
    if rel=='y':
      print('')
      print('The answer...')
      sleep(2)
      ansErr=99
      if EQdeg==1:
        print(x1)
      if EQdeg==2:
        print(x1,x2)
      if EQdeg==72:
        print(x1)
      if EQdeg==3:
        print(x1,x2,x3)
      if EQdeg==731:
        print(x1)
      if EQdeg==732:
        print(x1,x2)
      if EQdeg==4:
        print(x1,x2,x3,x4)
      if EQdeg==741:
        print(x1)
      if EQdeg==742:
        print(x1,x2)
      if EQdeg==743:
        print(x1,x2,x3)
    if rel=='n':
      print('...')
      sleep(2)
      print('It has gone...')
      sleep(2)
      print('')
      EQdeg=input('Linear: press [1] / Quadratic: press[2] / Cubic: press[3] / Quartic: press[4] / help: press[9] | ')
    else:
      print('Oops!...')
      sleep(1)
      re=input("Yes: press [y] / No: press [n] | ")

  if ansErr==99:
    break