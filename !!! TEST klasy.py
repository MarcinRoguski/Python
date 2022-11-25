class Cake:
    def __init__(self, name, kind, taste):
        self.name = name
        self.kind = kind
        self.taste = taste


cake_01 = Cake('Applepie', 'fruity', 'fudge')
cake_02 = Cake('WZ', 'Choco', 'Cherry')
cake_03 = Cake('Muffin', 'Hazelnut', 'Pear')

bakery_offer = [cake_01, cake_02, cake_03]

for cake in bakery_offer:
    print('W ofercie mamy {} o smaku {} z nadzieniem {}'.format(cake.name, cake.kind, cake.taste))
