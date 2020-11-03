# CreativeTestTask_RestAPI


Задача для домашнего выполнения:

   Напишите сервис Rest Api у которого должны быть следующие модели:
   
   1. Пользователи (login, password, name, city) # city foreignkey к пользователю
   2. Города(name) - Города добавить/удалить/изменить может только admi
   3. Объявления (name, users, city, body, price) # users,ciity - foreignkey
   
   Функционал должен быть следующим (необходимо только API):
   
   1. Регистрация пользователя
   2. Авторизовать пользователя (jwt)
   3. Добавить/изменить/удалить объявление
   4. Вывод объявлении с возможностью сортировок (передавая аргумент sort = 1 или -1)
   5. Поиск объявлении (должен работать с возможностью опечаток)
   6. Фильтрация объявлении по городам/пользователям.

Готовый результат необходимо залить на github. 


