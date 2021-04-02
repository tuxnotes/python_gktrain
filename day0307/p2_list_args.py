class Custom(object):
    # 顾客
    def __init__(self, name, goods=[]):
        # 这里goods的写法是有问题的，不同的实例会共享goods列表。如果不想共享则goods=None,正确写法如下：
        """
        def __init(self, name, goods=None):
            self.name = name
            if goods is None:
                goods = []
            self.goods = goods
        """
        self.name = name
        self.goods = goods

    def buy(self, goods_name):
        # 购买物品
        self.goods.append(goods_name)

    def pay_up(self):
        # 结账
        print(self.name)
        for item in self.goods:
            print(item)


custom1 = Custom('Tome')
custom1.buy('apple')

custom2 = Custom('jerry')
custom2.buy('cake')
custom2.pay_up()

print(id(custom1.goods))
print(id(custom2.goods))