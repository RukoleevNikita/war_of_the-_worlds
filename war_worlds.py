# import random
# task 1
# Напишите программу по следующему описанию. Есть класс "Воин". От него создаются три экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

class ClassWarrior():
    def __init__(self, n, hp,  att,):
        self.name = n
        self.health = hp
        self.attack = att


    #     # if __name__ == '__main__':
warriorFirst = ClassWarrior('Visigoth', 100, 20)
warriorSecond = ClassWarrior('Roland', 100, 20)
warriorThird = ClassWarrior('Attila', 100, 20)
print(warriorFirst.__dict__, warriorSecond.__dict__, warriorThird.__dict__)
