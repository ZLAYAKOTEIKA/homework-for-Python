import numpy as np
import pandas as pd


## 1. Разобраться как использовать мультииндексные ключи в данном примере

# index = [
#     ('city_1', 2010),
#     ('city_1', 2020),
#     ('city_2', 2010),
#     ('city_2', 2020),
#     ('city_3', 2010),
#     ('city_3', 2020),
# ]

# population = [
#     101,
#     201,
#     102,
#     202,
#     103,
#     203,
# ]
# pop = pd.Series(population, index = index)
# pop_df = pd.DataFrame(
#     {
#         'total': pop,
#         'something': [
#             10,
#             11,
#             12,
#             13,
#             14,
#             15,
#         ]
#     }
# )

# print(pop)


# pop_df_1 = pop_df.loc[[i for i in pop.index if i[0] == 'city_1']]['something']
# print(pop_df_1)

# pop_df_2 = pop_df.loc[ [i for i in pop.index if i[0] in ['city_1', 'city_3'] ] ][['total','something']]
# print(pop_df_2)

# pop_df_3 = pop_df.loc[ [i for i in pop.index if i[0] in ['city_1', 'city_3'] ] ][['something']]
# print(pop_df_3)



## 2. Из получившихся данных выбрать данные по 
## - 2020 году (для всех столбцов)
## - job_1 (для всех строк)
## - для city_1 и job_2 

# index = pd.MultiIndex.from_tuples(index)
# pop = pop.reindex(index)

# index = pd.MultiIndex.from_product([
#     ['city_a', 'city_b'],
#     [2010,2020]
#     ],
#     names = ['city', 'year']
# )

# columns = pd.MultiIndex.from_product([
#     ['pers_a', 'pers_b', 'pers_c'],
#     ['job_1', 'job_2']
#     ],
#     names = ['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4,6))
# data_df = pd.DataFrame(data, index = index, columns = columns)

# ## - 2020 году (для всех столбцов)
# print(data_df.xs(2020, level='year'))

# print()

# ## - job_1 (для всех строк)
# print(data_df.xs('job_1', level='job', axis=1))

# print()

# ## - для city_1 и job_2 
# print(data_df.loc['city_a'].xs('job_2', level='job', axis=1))




# 3. Взять за основу DataFrame со следующей структурой

# index = pd.MultiIndex.from_product(
#     [
#         ['city_1', 'city_2'],
#         [2010, 2020]
#     ],
#     names=['city', 'year']
# )
# columns = pd.MultiIndex.from_product(
#     [
#         ['person_1', 'person_2', 'person_3'],
#         ['job_1', 'job_2']
#     ],
#     names=['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4,6))
# data_df = pd.DataFrame(data, index = index, columns = columns)

# # Выполнить запрос на получение следующих данных
# # - все данные по person_1 и person_3
# print(data_df[['person_1', 'person_3']])

# print()

# # - все данные по первому городу и первым двум person-ам (с использование срезов)
# print(data_df.iloc[0,:][['person_1','person_2']])

# print()

# # Приведите пример (самостоятельно) с использованием pd.IndexSlice

# idx = pd.IndexSlice

# # Все строки и столбцы с person_1 или person_3
# sliced_data = data_df.loc[:, idx[['person_1', 'person_3'], :]]
# print(sliced_data)



#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)

student_ids = pd.Series([1, 2, 3, 4], name='student_id')

math_scores = pd.Series([85, 92, 78], index=[1, 3, 4], name='math_score')

# Outer Join: Соединяет данные, включая все ID студентов, даже если у них нет оценок.
# Значения, отсутствующие в одной из Series, заполняются NaN.
outer_join = pd.concat([student_ids, math_scores], axis=1, join='outer')
print(outer_join)

print()

# Inner Join: Соединяет данные только для тех ID студентов, которые присутствуют в обеих Series.
inner_join = pd.concat([student_ids, math_scores], axis=1, join='inner')
print(inner_join)