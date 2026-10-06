import pandas as pd
emp = pd.DataFrame({'id': [1, 2, 3], 'name': ['A', 'B', 'C'],
                    'salary': [100, 200, 300], 'managerId': [2, pd.NA, 2]})
def find_employees(employee):
#через merge -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    #объединить таблицу саму с собой
    employee = pd.merge(employee, employee,
                        #inner - сохранить все столбцы из двух таблиц
                        how='inner',
                        #левый ключ
                        left_on='managerId',
                        #правый ключ
                        right_on='id',
                        #если названия столбцов совпало, то добавь
                        #для левого суффикс и для правого
                        suffixes=('', '_manager'))
    mask = employee['salary'] > employee['salary_manager']
    #двойные скобки, чтоб вернуть именно датафрейм
    #также изменим имя единственного столбца
    return employee[mask][['name']].rename(columns={'name': 'Employee'})
#через map -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    # #создаем вектор, у которого индексы станут ключами
    # manager_salary = employee.set_index('id')['salary']
    # #создадим столбец используя этот словарь-вектор
    # employee['manager_salary'] = employee['managerId'].map(manager_salary)
    # #применим маску
    # mask = employee['salary'] > employee['manager_salary']
    # #выведем ответ
    # return employee[mask]['name'].rename(columns={'name': 'Employee'})
print(find_employees(emp))


