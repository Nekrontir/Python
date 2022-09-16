'''with open('file.txt') as f:
    lst =[int(n) for n in f.readline().split()]
    for i in range(len(lst)):
        if lst[i] - 1 != lst[i-1]:
            print(lst[i] - 1)'''


'''lst = [1, 5, 2, 3, 4, 6, 1, 7]
res = [lst[0]]
for n in lst[1:]:
    if n > res[len(res) - 1]:
        res.append(n)'''


'''str = 'Привет забвение котёнок абв'        
res = list (filter(lambda x:'абв'  not in  x ,str.split()))
#for word in str.split():
#    if 'абв' not in  word:
#        res.append(word)

print(''.join(res))'''

#print(sum(list(map(lambda x: x**2, list(filter(lambda x: x % 9 == 0, list(range(10,100))))))))


'''def triangl(a,b,c):
    if  a + b > c and b + c >a and a+c> b:
        print('Это треугольник')
    else:
        print('Это не треугольник')

triangl(1,1,2)
triangl(6,7,10)'''
#triangle = lambda a,  b, c:a + b > c and b + c >a and a+c> b



s = 'Буря мглою небо кроет'
nums =[4, 3, 1]
res = []
for n in nums:
    res.append(s[n-1])
print(' '.join(res).capitalize())    
