#lst = [int(i) for i in input().split()]
#lst2 = []

#for i in lst:
 #   if lst.count(i) == 1:
  #      lst2.append(i)
#print (i*lst2)
     

#lst = [int(i) for i in input().split()]

#for idx, i in range(lst):
 #   if lst[i] > lst[i - 1]:
  #      print(lst[i])



#from time import time

#print(time())
#print(type(time()))
#def run(n):
#    a = time()
#    b = int(a)
#    c = (a - b) * 10
#    print(int((b**c) % n))

#run(20)

#lst = [i for i in input().split()]
#n = int(input('Введите число: '))
#flag = 0

#for i in lst:
#    if i.find(str(n)) != -1:
#        print('yes')
#        break
#    else:
#        flag += 1
#if flag == len(lst):
#    print('no')

#lst = [i for i in input().split()]
#set1 = set(lst)
#print(len(set1))

#lst = [i for i in input().split()]
#lst2 = [i for i in input().split()]
#print(sorted(set(lst) & set(lst2)))
#print(sorted(set(lst) | set(lst2)))

#MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
#        'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..',
#         'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---',
#         'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-',
#         'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..'}

#help = 'Help me SOS'.upper()

#for i in help:
#  if i in MORSE:
#    print(MORSE[i], end='')
#  else:
#    print("\n")  


#num_dict = {}
#lst = input('введите: ').split(' ')
#for i in lst:
  #if i not in num_dict:
  #  num_dict[i] = 1 
  #else:
  #  num_dict[i] += 1
#  num_dict[i] = num_dict.get(i,0) +1 
#  print(num_dict[i])