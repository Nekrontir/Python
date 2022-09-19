# 1 задание - не до конца понял что от меня нужно

'''p = 3.141
d = 0.001
c = p*d
print('длина окружности = ',round(c,10))'''

####################################################

# 2 задание - 

'''a = input('введите целое число для которого нужно найти множители: ')
lst = []
for i in range(2, int(a / 2) + 1):
    if a % i == 0:
        lst.append(i)    
print (lst)'''

######################################################

# 3 задание

'''lst = [1,4,3,6,7,8,2,1,4,5,6,3,57,2,35,47,56]
print (lst)
uniq = set(lst)
print(uniq)'''
myList = [1, 4, 3, 6, 7, 8, 2, 1, 4, 5, 6, 3, 57, 2, 35, 47, 56]
uniqueList = []
for item in myList:
    itemExist = False
    for x in uniqueList:
        if x == item:
            itemExist = True
            break
    if not itemExist:
        uniqueList.append(item)
print(uniqueList)

####################################################