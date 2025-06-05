import numpy as np
import pandas as pd

## ЕСли размерность данных > 2, используют иерархическую индексацию (мультииндекс). В один индекс влючаются несколько уровней

# index = [
#     ('city_1', 2020, 1),
#     ('city_1', 2020, 2),

#     ('city_2', 2010, 1),
#     ('city_2', 2010, 2),

#     ('city_3', 2025, 1),
#     ('city_3', 2025, 2),

#     ('city_4', 2010, 1),
#     ('city_4', 2010, 2),

#     ('city_5', 2020, 1),
#     ('city_5', 2020, 2),

#     ('city_6', 2010, 1),
#     ('city_6', 2010, 2)
# ]

# population = [101, 101, 123, 123, 105, 105, 110, 110, 101, 101, 123, 123]

# pop = pd.Series(population, index = index, dtype='int16')

# # print(pop)

# # print(pop[ [i for i in pop.index if i[1] == 2020] ])

# ## MultiIndex

# index = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(index)

# print(pop)

# # print(pop[:, 2020])

# # pop_df = pop.unstack()
# # print(pop_df)

# # print(pop_df.stack())



# index = [
#     ('city_1', 2020, 1),
#     ('city_1', 2020, 2),

#     ('city_2', 2010, 1),
#     ('city_2', 2010, 2),

#     ('city_3', 2025, 1),
#     ('city_3', 2025, 2),

#     ('city_4', 2010, 1),
#     ('city_4', 2010, 2),

#     ('city_5', 2020, 1),
#     ('city_5', 2020, 2),

#     ('city_6', 2010, 1),
#     ('city_6', 2010, 2)
# ]

# population = [101, 1010, 123, 1230, 105, 1050, 110, 1100, 101, 1010, 123, 1230]

# index = pd.MultiIndex.from_tuples(index)

# pop = pd.Series(population, index = index, dtype='int16')

# # print(pop)

# # print(pop[:,2010,:])
# # print(pop[:,:,2])

# pop_df = pop.unstack()

# # print(pop_df)

# pop_df = pd.DataFrame({'total': pop,
#     'something':[i+10 for i in range(12)]})

# # print(pop_df)

# # print(pop_df['something'])

# # pop_df_1 = pop_df.loc['city_1', 'something']
# # pop_df_2 = pop_df.loc[['city_1', 'city_4'], ['something', 'total']]

# # print(pop_df_1)
# # print(pop_df_2)

# ## Как можно создавать мультииндексы?

# ## 1) Список массивов, задающих значения индекса на каждом уровне

# i1 = pd.MultiIndex.from_arrays([
#     ['a', 'a', 'b', 'b'],
#     [1,2,1,2]
# ])

# print(i1)

# ## 2) Список кортежей, задающих значение индекса в каждой точке

# i2 = pd.MultiIndex.from_tuples([
#     ('a', 1),
#     ('a', 2),
#     ('b', 1),
#     ('b', 2),
# ])

# print(i2)

##  3) Декартово произведение обычных индексов

# i3 = pd.MultiIndex.from_product([
#     ['a', 'b'],
#     [1,2]
# ])

# print(i3)

## 4) Описание внутреннего представления: levels - список списков
## codes - список списков меток

# i4 = pd.MultiIndex(
#     levels = [
#         ['a', 'b', 'c'],
#         [1,2]
#     ],
#     codes = [
#         [0, 0, 1, 1, 2, 2], # a a b b c c
#         [0, 1, 0, 1, 0, 1]] # 1 2 1 2 1 2
# )

# print(i4)

## уровням можно давать названия

# data = {
#     ('city_1', 2010): 100,
#     ('city_2', 2020): 200,
#     ('city_1', 2010): 1001,
#     ('city_2', 2020): 2001,
# }

# s = pd.Series(data)
# print(s)
# print()

# s.index.names = ['city', 'year']
# print(s)

# index = pd.MultiIndex.from_product([
#     ['city_a', 'city_b'],
#     [1000,2000]
#     ],
#     names = ['city', 'year']
# )

# # print(index)

# columns = pd.MultiIndex.from_product([
#     ['pers_a', 'pers_b', 'pers_c'],
#     ['job_1', 'job_2']
#     ],
#     names = ['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4,6))
# # print(data)

# data_df = pd.DataFrame(data, index = index, columns = columns)

# print(data_df)

## Индексация и срезы (по мультииндексу)

# data = {
#     ('city_1', 2010): 100,
#     ('city_2', 2020): 200,
#     ('city_1', 2010): 1001,
#     ('city_2', 2020): 2001,
#     ('city_3', 2010): 1001,
#     ('city_3', 2020): 2001,
# }

# s = pd.Series(data)
# s.index.names = ['city', 'year']

# # print(s['city_1', 2010])
# # print(s['city_1'])

# # print(s.loc['city_1':'city_2'])

# # print(s[:, 2010])

# # print(s[s>2000])

# print(s['city_1':'city_2'])

## Перегруппировка по мультииндексу

rng = np.random.default_rng(1)

# index = pd.MultiIndex.from_product([
#     ['a', 'c', 'b'],
#     [1,2]
# ])

# data = pd.Series(rng.random(6), index = index)
# data.index.names = ['char', 'int']

# print(data)
# # print(data['a':'b'])

# data = data.sort_index()

# print(data['a':'b'])

## Индексы должны быть отсортированы

# index = [
#     ('city_1', 2020, 1),
#     ('city_1', 2020, 2),

#     ('city_2', 2010, 1),
#     ('city_2', 2010, 2),

#     ('city_3', 2025, 1),
#     ('city_3', 2025, 2),

#     ('city_4', 2010, 1),
#     ('city_4', 2010, 2),

#     ('city_5', 2020, 1),
#     ('city_5', 2020, 2),

#     ('city_6', 2010, 1),
#     ('city_6', 2010, 2)
# ]

# population = [101, 1010, 123, 1230, 105, 1050, 110, 1100, 101, 1010, 123, 1230]

# pop = pd.Series(population, index = index)

# print(pop)

# i = pd.MultiIndex.from_tuples(index)

# pop = pop.reindex(i)

# print(pop)

# print(pop.unstack())

# print(pop.unstack(level = 0))

# print(pop.unstack(level = 1))

## NumPy Конкатенация

x = [[1,2,3]]
y = [[4,5,6]]
z = [[7,8,9]]

# print(np.concatenate([x,y,z]))

# print(np.concatenate([x,y,z], axis = 1))
# print(np.concatenate([x,y,z], axis = 0))

## Pandas - concat

# ser1 = pd.Series(['a', 'b', 'c'], index = [1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index = [4,5,6])

# # print(pd.concat([ser1, ser2]))

# ser1 = pd.Series(['a', 'b', 'c'], index = [1,2,3])
# ser2 = pd.Series(['d', 'e', 'f'], index = [1,2,6])

# print(pd.concat([ser1, ser2]))

# print(pd.concat([ser1, ser2], verify_integrity=False))
# print(pd.concat([ser1, ser2], ignore_index=True))

# print(pd.concat([ser1, ser2], keys= ['x', 'y']))

# ser1 = pd.Series(['a', 'b', 'c'], index = [1,2,3])
# ser2 = pd.Series(['b', 'c', 'f'], index = [3,2,6])

# print(pd.concat([ser1, ser2], join='outer'))
# print(pd.concat([ser1, ser2], join='inner'))