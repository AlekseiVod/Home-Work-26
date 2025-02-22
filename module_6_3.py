class Horse:
    """класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
1) x_distance = 0 - пройденный путь.
2) sound = 'Frrr' - звук, который издаёт лошадь."""

    def __init__(self, *args):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__(*args)

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    """класс описывающий орла. Объект этого класса обладает следующими атрибутами:
1) y_distance = 0 - высота полёта
2) sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)"""

    def __init__(self, *args):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__(*args)

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    """ класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
Также обладает методами:
1) move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run
и fly соответственно.
2) get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
3) voice - который печатает значение унаследованного атрибута sound."""

    def __init__(self, *args):
        super().__init__(*args)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
