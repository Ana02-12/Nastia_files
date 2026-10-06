import pandas as pd

person = pd.DataFrame({
    "id": [1, 2, 3],
    "email": [
        "john@example.com",
        "bob@example.com",
        "john@example.com"
    ]
})

def delete_duplicate_emails(person):
    # через drop_duplicates() -=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #отсортируем по id
    person.sort_values(by='id', inplace=True)
    # #удалим дубликаты
    # person.drop_duplicates(subset='email',
    #                        keep='first',
    #                        inplace=True)
    # return person
    #через duplicated() -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    #создадим маску, где повтор значения это True
    mask = person['email'].duplicated()
    #удалим с помощью дроп, передав индексы ненужных строк
    person.drop(person[mask].index, inplace=True)


