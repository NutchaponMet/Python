# this is my learning python with Arjan Prasertcbs list- youtube
# class Player():
#      def __init__(self, fname, lname, number):
#           self.fname = fname
#           self.lname = lname
#           self.number = number

# if __name__=='__main__':
#      p1 = Player('Nutchapon','Metmaolee',1)
#      print(p1.number)
#      print(p1.fname)

# def q(a:float, b:float, c:float):

class Interest():
     def __init__(self, money, discount, time) -> None:
          self.money = money
          self.discount = discount
          self.time = time

     def pv(self):
          return self.money + (1 + self.discount)**self.time


if __name__ == '__main__':
     i = Interest(100000, 5, 10)
     pv = i.pv()
     print(pv)