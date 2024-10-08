num = int(input("Введите число: ")) # Запрашиваем у пользователя число


if num > 1: # Простые числа должны быть больше 1, поэтому делаем такую проверку
    
    i = 2  # Начинаем проверку с числа 2
    
    while num % i != 0: # Используем цикл while для поиска делителя
        
        i += 1  # Переходим к следующему числу
    
    if i == num: # Если цикл завершился и делитель - само число, то оно простое
        
        print(num, "является простым числом") # Выводим число, которое является простым и подписываем его. 
        
    else: # Если условие не соответствует i == num, тогда выполняем следующий блок. 
        
        print(num, "не является простым числом") # Выводим число, которое не является простым и подписываем его. 
        
else: # Если условие не соответствует num > 1, тогда выполняем следующий блок. 
    
    print(num, "не является простым числом") # Выводим число, которое не является простым и подписываем его. 
