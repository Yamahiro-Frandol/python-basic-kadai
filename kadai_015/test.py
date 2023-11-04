### 課題　15章 クラスを理解しよう

class Human:
  def printinfo(self):
        print('name:{0}, age:{1}'. format(self.name, self.age))

human = Human()
human.name = "侍太郎"
human.age = 35

human.printinfo()