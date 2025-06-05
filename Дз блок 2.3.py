import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать

# - списки Python или массивы NumPy

data1 = pd.Series([0.25, 0.5, 0.75, 1.0], index = ['a', 'b', 'c', 'd'])
data2 = pd.Series(np.linspace(-5,5,20), index = np.arange(20))

# - скалярные значение

data3 = pd.Series(5, index = [chr for chr in 'abcdefghijk'])

# - словари

data4 = pd.Series({
    'a': 1,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 5,
    'f': 8,
    'g': 13,
    'h': 21,
})


# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания:

# - через объекты Series

Ser1 = pd.Series(np.linspace(-1, 1, 12), index = [chr for chr in 'abcdefghijkl'])
Ser2 = pd.Series(np.linspace(0, 10, 12), index = [chr for chr in 'abcdefghijkl'])

DataFr1 = pd.DataFrame({
    'coordinate': Ser1,
    'weight': Ser2,
})


# - списки словарей

D1 = dict(zip([chr for chr in 'abcdefgh'], np.linspace(0, 1, 8)))
D2 = dict(zip([chr for chr in 'cdefghij'], np.linspace(-1, 0, 8)))

DataFr2 = pd.DataFrame([D1, D2], index = ['Index_1', 'Index_2'])


# - словари объектов Series

Ser1 = pd.Series(np.linspace(-1, 1, 12), index = [chr for chr in 'abcdefghijkl'])
Ser2 = pd.Series(np.linspace(0, 10, 12), index = [chr for chr in 'abcdefghijkl'])

DataFr3 = pd.DataFrame({
    'coordinate': Ser1,
    'weight': Ser2,
})

# - двумерный массив NumPy

np.random.seed(1)
data = np.random.randint(-5, 6, size=(10,3))

DataFr4 = pd.DataFrame(data, index = ['Ind_'+str(i) for i in range(1,11)], columns = ['Col_'+str(i) for i in range(1,4)])

# - структурированный массив Numpy

data = np.array([('name_'+str(i), (i+1)**1.3) for i in range(10)], 
                dtype = {'names':('name', 'age'), 'formats': ('U10', 'i4')})

DataFr5 = pd.DataFrame(data)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

Ser1 = pd.Series(np.linspace(-20, -10, 10), index = [chr for chr in 'abcdeghijl'])
Ser2 = pd.Series(np.linspace(-100, -10, 10), index = [chr for chr in 'abdefghijk'])

DataFr6 = pd.DataFrame({'col_1':Ser1,
                       'col_2':Ser2}).fillna(1)


# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng(1)

A = rng.integers(0, 10, (3,4))

#print(A)

B = A - A[:, 0].reshape(3,1)

#print(B)

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, np.nan],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))

df_ff = df.ffill()
df_bf = df.bfill()

# print(df)
# print()
# print(df_ff)
# print()
# print(df_bf)