
# #5'. Реализуйте алгоритм перемешивания списка.
import random
def mix_list(list_orig):
     list = list_orig[:]
     list_length = len(list)
     for n in range(list_length):
         index_unknow = random.randint(0, list_length-1)
         temp = list[n]
         list[n] = list[index_unknow]
         list[index_unknow] = temp
     return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный рандомный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)

# #И вот такое еще решение
# import random
# spisok = ["Love", "World", "Peace", "Hello", "Хорошо", "Плохо"]
# random.shuffle(spisok)
# print(spisok)