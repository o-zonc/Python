# 학번: 2022189005
# 이름: 이경환
# 이메일: xerenes@yonsei.ac.kr
# 제출일: 2022-11-25
# 과제번호: 11주차 2번

class Item:
    count = 0

    def __init__(self, title, price):
        self.title, self.price = title, price
    
    def getprice(self):
        return 0

class Book(Item):
    def __init__(self, title, price, page, author):
        self.title, self.price, self.page, self.author = title, price, page, author
        Item.count += 1
    
    def __repr__(self):
        return '제목:'+self.title+' 가격:'+str(self.price)+' 페이지:'+str(self.page)+' 저자:'+self.author
    
    def getprice(self):
        return self.price

class Magazine(Item):
    def __init__(self, title, price, month):
        self.title, self.price, self.month = title, price, month
        Item.count += 1
    
    def __repr__(self):
        return '제목:'+self.title+' 가격:'+str(self.price)+' 출간월:'+str(self.month)

    def getprice(self):
        return self.price

#######################

if __name__=='__main__':
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난장이가 쏘아올린 작은 공', 12000, 112, '조세희')
    magazine1 = Magazine('보그',11000, 9)
    magazine2 = Magazine('싱글즈',13000, 8)
    print('', book1,'\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
    print('총',Item.count,'권')
    book2.getprice()
    magazine1.getprice()
    book1.getprice()