week = ('понедельник','вторник','среда','четверг','пятница', 'суббота', 'воскресенье')
day = int (input ("введите номер дня недели"))
if day > 0 and day < 8 :
    if (week[day - 1] == week[5]) or (week[day - 1] == week[6]) :
        print(week[day-1],'выходной')
    else:
        print (week[day-1])
else:
    print ('Try one more time')

     