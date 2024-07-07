class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def nameprint(self):
        print('Имя героя:', self.name)

    def умножить_здоровье_на_2(self):
        self.health_points *= 2

    def __str__(self):
        return f"Здоровье: {self.health_points}\nПрозвище: {self.nickname}, Суперспособность: {self.superpower}, "

    def __len__(self):
        return len(self.catchphrase)

Harleen_Frances_Quinzel = SuperHero('Harleen Frances Quinzel', 'Harley Quinn',
                                    'immunity to poisons', 100, 'My love scares you, but no gun?')

Harleen_Frances_Quinzel.nameprint()
Harleen_Frances_Quinzel.умножить_здоровье_на_2()
print("После удвоения здоровья:", Harleen_Frances_Quinzel)
print("Длина коронной фразы:", len(Harleen_Frances_Quinzel))