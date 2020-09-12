class Critter:
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Critter.total)
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom 
        Critter.total += 1

    def talk(self):
        print('My name is', self.name)

    def __str__(self):
        ans = 'Объект класса Critter\n' 
        ans += 'name: ' + self.name + '\n'
        return ans  

def main():
    print('Доступ к атрибуту класса через объект:', end = ' ')
    print(Critter.total)
    print('Critters are created.')
    crit1 = Critter("Bobik")
    crit1.talk()
    crit2 = Critter('Murzik')
    crit2.talk()
    crit3 = Critter('critter#3')
    crit3.talk()

    Critter.status()

    print('Доступ к атрибуту класса через объект:', end = ' ')
    print(crit1.total)
    print('Доступ к атрибуту', crit1.name)
    print(crit2)

main()            