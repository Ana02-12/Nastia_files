import pandas as pd
person = pd.DataFrame({
    'id': [1, 2, 3],
    'email': ['a@b.com', 'c@d.com', 'a@b.com']
})
#через groupby -=-=-=-=-=---=-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def duplicate_emails(person):
    # df_count = (
          #группировка по email
    #     person.groupby('email')
    #     #название группы и количество строк в ней (Series)
    #     #ключ группы стал индексом
    #       .size()
    #     #делаем индекс столбцом
    #     #задаем имя для единственного столбца
    #       .reset_index(name='count')
    #             )
    # mask = df_count['count'] > 1
    # return df_count[mask][['email']]
#через фильтр -=-=-=-=-=---=-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # группировка по столбцу
    df_group = person.groupby('email')
    #оставим только группы длиннее, чем один элемент
    df_filt = df_group.filter(lambda x: len(x) > 1)[['email']]
    return df_filt.drop_duplicates()
#через duplicated -=-=-=-=-=---=-==-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#     #keep=True: только дублирующие значения будут True (мы уже видели этот адрес?)
#     #keep=False: True будут все значения, у которых есть дубликат (он индивидуален?)
#     mask = person.duplicated('email', keep=False)
#     person_mask = person[mask]
#     res = person_mask[['email']].rename(columns={'email': 'Email'})
#     return res.drop_duplicates()
# print(duplicate_emails(person))


