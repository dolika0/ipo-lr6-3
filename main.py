'''
Написать программу, которая:
- Запрашивает у пользователя количество строк. (*должна быть проверка*)
- Затем сами строки.
- Определяет, сколько различных слов содержится в этом тексте, и выводит из количество

'''
kolvStrok = int(input("Введите количество строк\n")) # Запрос от пользователя

text = '' # Инициализация переменной

if kolvStrok <= 0 and kolvStrok.isdigit(): # Задаём условие 
   print('Число должно быть больше нуля') # Вывод на экран
   
else: # Число введено верно
   
     for i in range(1, kolvStrok+1) : # Цикл
      str = input(f"Введите строку \n") # Полулучение строки от пользователя
      text = text + str + ' ' # Добавление строк к общему тексту
    
print(text) # Вывод всего текста
text = text.split() # Разделение по пробелам
text = set(text) # Делаем множество чтобы найти уникальные слова
print(len(text)) # Вывод кол-ва слов в тексте
