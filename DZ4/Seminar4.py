#sp  = [int(i) for i in input().split()]
#print (max(sp))
#print (min(sp))

#from math import sqrt

#a, b, c = int(input()), int(input()), int(input())
#d = b**2 - 4*a - c
#if d<0:
#    print('No')
#elif d==0:
#    print(f'x = {-b / (2*a)}' )
#else :
#    print(f'x1 = {-b -  sqrt(d) / (2*a)}' )
#    print(f'x1 = {-b +  sqrt(d) / (2*a)}' )


#sp = [int(input()), int(input())]
#max_ = max(sp)
#min_ = min(sp)
#for i in range(max_, (max_ * min_)):
#    if i%max_ == 0 and i%min_ == 0:
#        print(i)
#        break


#sp = input().split()
#res = {}
#for word in sp:
#    if word in res.keys():
#        res[word] += 1
#        print(res[word], end= ' ')
#    else:
#        res[word] = 0
#        print(res[word], end= ' ')    



#count = int(input())
#d = {}
#for _ in range(count):
#    key, value = input().split()
#    d[key] = value
#user_input = input()
#if user_input in d.keys():
#    print(d[user_input])
#if user_input in  d.value():
#    for k, v in d.items():
#        if user_input == v:
#            print(k)


count = int(input())
d = {}
for _ in range(count):
    for word in input().split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
#result = sorted(d.items(), key = lambda x: (-x[1], x[0]))
#print(result[0][0])  








