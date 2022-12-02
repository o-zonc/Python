# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-11-25
# 과제번호: 13주차 1번

class Pet:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __repr__(self):
        return f"{self.name} {self.age}"    
    
    def __len__(self):
        return 0

    def human_age(self):
        return (4 * self.age)

class Dog(Pet):
    def __len__(self):
        return self.age
    
    def bark(self, num):
        for i in range(num):
            print('bark')

class Cat(Pet):
    def __len__(self):
        return self.age
    
    def meow(self, num):
        for i in range(num):
            print('meow')
##########################


if __name__ == '__main__':   
    lex = Dog('lex', 6)
    lex.bark(8)
    print(len(lex))
    print(lex)
    print('human age:', lex.human_age())
    row = Cat('row', 10)
    row.meow(6)
    print(len(row))
    print(row)
    print('human age:', row.human_age())