#первая  задача - не смог победить числа с точкой,с целым числом работает
#подозреваю что намудрил с вводом числа

#lst = [int(i) for i in input('введите число = ')]
#sum = (int(0))
#for number in lst:
#    sum += number  
#print('сумма = ', sum)    

#########################################################################

#вторая задача

#n = int(input ('Введите число: '))
#number = 1
#for i in range(1,n+1): 
#    number *= i
#    print (number)        

########################################################################

#третья задача - условие брал из файла ворд приложенного к семинару (1 + 1/n) в степени n 

#import math

#n = int(input ('Введите число: '))
#number = 0
#for i in range(1, n+1):
#    number += math.pow((1 + (1/i)), i)
#print (number)

########################################################################

#четвёртая задача  -  с текстовым файлом у меня поработать не получилось

#n = int(input ('Введите число: '))
#lst = (range( -n , n+1 ))
#for i in lst:
#    print (i, end = " ", )
#print()    
#x = int(input ('Введите номер позиции первого числа: '))
#y = int(input ('Введите номер позиции второго числа: '))
#z = lst[ x - 1 ] * lst [ y - 1 ]
#print ('Произведение данных чисел = ', z )

#######################################################################

#5 задание - как то мешает список (хотя и не оригинально, понимаю)

lst = ['шла', 'саша','по','шоссе','и','сосала','сушку']
def  swap(lst):
    for i in range(-1, 2 ):
        lst.reverse
        x = lst.pop(0)
        lst.reverse
        lst.append(x)
print (lst)
swap (lst)
print (lst)


