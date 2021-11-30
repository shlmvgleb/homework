# Задача 2.
# Напишите программу, в которой будет класс Sort.
#
# Напишите метод для следующих сортировок:
# - bubble — сортировка пузырьком. Принимает список чисел, возвращает отсортированный список чисел.
class Sort:
    def __init__(self, list_1):
        self.list_1 = list_1

    def bubble(self):
        self.list_1 = self.list_1.split()
        self.list_1 = [int(k) for k in self.list_1]
        for o in range(len(self.list_1) + 1):
            a = 0
            for j in range(len(self.list_1) - 1):
                if self.list_1[a] <= self.list_1[a + 1]:
                    a += 1
                elif self.list_1[a] > self.list_1[a + 1]:
                    self.list_1[a], self.list_1[a + 1] = self.list_1[a + 1], self.list_1[a]
                    a += 1
        return self.list_1


if __name__ == '__main__':
    ads = Sort(input('Введите числа в строчку через пробел:\n'))
    for i in ads.bubble():
        print(i, end=' ')
