# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в 
# его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения
# одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  

def result_list(list1,list2):
    list3 =[]
    for item in list1:
        #print(item)
        count = 0
        for i in item:
            #print(i)
            if i in list2:
                count+=1
        list3.append(count)
    
    return set(list3)

lst = 'пАра-ра-рам рАм-пам-папЮам па-ра-па-да'
lst = lst.lower()
lst1 = lst.split()
#print(lst1)
lst2 = list('аоуеэяиыю')
#print(lst2)
 
res = result_list(lst1,lst2)
#print(res)
        
if len(res)==1:
    print('Парам пам-пам')
else:
    print('Пам парам')
