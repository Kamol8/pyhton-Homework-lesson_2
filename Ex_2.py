#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input())
sum_digits = 1

for i in range(num):
    sum_digits *= i + 1
    print(sum_digits, end = ', ')