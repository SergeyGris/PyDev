'''
Задача 7 «Парты»

В школе решили набрать три новых математических класса.
Так как занятия по математике у них проходят в одно и
то же время, было решено выделить кабинет для каждого класса
и купить в них новые парты. За каждой партой может сидеть не больше двух учеников.
Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить
парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа:
количество учащихся в каждом из трех классов.

'''
c1 = int(input())
c2 = int(input())
c3 = int(input())

rez = c1 // 2 + c1 % 2 + c2 // 2 + c2 % 2 + c3 // 2 + c3 % 2
print(rez)