# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input('ИМЯ ')
surname = input('ФАМИЛИЯ ')
year = int(input('ГОД РОЖДЕНИЯ '))
city = input('ГОРОД ')
email = input('email ')
telephone = input('ТЕЛЕФОН ')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])


print(my_func(name='name', surname='surname',  year="year", city='city', email='email', telephone='telephone'))