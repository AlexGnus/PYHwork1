day = int(input('Введите цифру дня недели от 1 до 7: '))
if day == 6 or day == 7:
    print('Это выходной день')
elif day == 1 or day ==2 or day == 3 or day == 4 or day == 5:
    print ('Это будний день') 
else:
    print ('Вы ввели не корректную цифру')
