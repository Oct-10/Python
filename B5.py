import time,random

class Adobe():
    智商 = random.randint(80,200)
    胸围 = random.randint(30,40)
    腰围 = random.randint(30,80)
    臀围 = random.randint(50,100)

    def say():
        print('主人，您好！')

    def cute():
        print('主人，求抱抱！')

    def angry():
        print('主人，我要报警了！')

    def run():
        print('我快乐地奔跑、奔跑……哎呦喂！撞墙了')

    @classmethod
    def naozi(cls):
        print('主人，我的智商是：')
        print(str(cls.智商))

    @classmethod    
    def body(cls):
        print('主人，我的三围是：')
        print('胸围'+str(cls.胸围))
        print('腰围'+str(cls.腰围))
        print('臀围'+str(cls.臀围))
        print('哈哈哈哈哈，下面粗上面细，我长得像个圆锥。')

Adobe.say()
time.sleep(1)
Adobe.naozi()
time.sleep(1)
Adobe.body()
time.sleep(1)
Adobe.cute()
time.sleep(1)
Adobe.angry()
time.sleep(1)
Adobe.run()
