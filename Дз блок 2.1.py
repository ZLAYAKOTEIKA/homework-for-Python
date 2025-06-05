import numpy as np
import random

np.random.seed(12345)

## 1. Какие еще существуют коды типов?

# dtype: int, int16 (i2), int32 (i4), int64 (i8), float, float16 (f2), float32 (f4), float64 (f8), complex, c(2,4,8,16), S(1->...), ..... 

## 2. Напишите код, подобный приведенному выше, но с другим типом

# a = np.array([1.23, 2, 3, 4, 5], dtype='S16')
# print(type(a), a)

# ## 3. Напишите код для создания массива с 5 значениями, располагающимися через равные интервалы в диапазоне от 0 до 1

# a = np.linspace(0,1,5)
# print(type(a), a)

# ## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

# a = np.random.uniform(0, 1, 5)
# print(type(a), a)

# ## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

# a = np.random.normal(0, 1, 5)
# print(type(a), a)

# ## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)

# a = np.random.randint(0, 10, 5)
# print(type(a), a)

# ## 7. Написать код для создания срезов массива 3 на 4

# a = np.random.randint(10, size=(3,4))
# print(a, end='\n\n')
# print()

# ## - первые две строки и три столбца
# a1 = a[:2, :3]
# print(a1, end='\n\n')

# ## - первые три строки и второй столбец
# a1 = a[:3, 1]
# print(a1, end='\n\n')

# ## - все строки и столбцы в обратном порядке
# a1 = a[::-1, ::-1]
# print(a1, end='\n\n')

# ## - второй столбец
# a1 = a[::, 1]
# print(a1, end='\n\n')

# ## - третья строка
# a1 = a[2, ::]
# print(a1, end='\n\n')

## 8. Продемонстрируйте, как сделать срез-копию

# a = np.array([1, 2, 3, 4, 5])

# b = a[1:4].copy()

# a[2] = 100

# print(b)
# print(a)

## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

# a = np.array([1, 2, 3, 4, 5])
# a_t = a[:, np.newaxis]

# print(a)
# print(a_t)

## 10. Разберитесь, как работает метод dstack

# a = np.random.randint(-5,5, size=(2,2))
# b = np.random.randint(-5,5, size=(2,2))

# print(a)
# print(b)

# print()
# c = np.dstack((a, b))
# print(c[:,:,0])
# print(c[:,:,1])

## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

# a = np.arange(10)
# a1, a2, a3 = np.split(a, [3, 7])

# print(a, a1, a2, a3, sep='\n')
# print(type(a1), type(a2), type(a3))

# a = np.random.randint(-5,5, size=(5,5))
# print(a, end='\n\n')

# a_vspl = np.vsplit(a, [2,3])
# print(*a_vspl, sep='\n\n', end='\n-----\n')

# a_hspl = np.hsplit(a, [2,3])
# print(*a_hspl, sep='\n\n')

# a = np.random.randint(-5,5, size=(3, 3, 3))
# print(a, end='\n\n')

# print('Slices:\n')

# a1 = np.dsplit(a, 1)
# print(*a1, sep='\n\n')


## 12. Привести пример использования всех универсальных функций, которые я привел

# a = np.arange(5,14)
# b = np.arange(1,10)
# print(a, b)

# c = np.add(a,b)
# print(c)

# c = np.subtract(a,b)
# print(c)

# c = np.multiply(a,b)
# print(c)

# c = np.divide(a,b)
# print(c)

# c = np.floor_divide(a,b)
# print(c)

# c = np.multiply(a,b)
# print(c)

# c = np.power(a,b)
# print(c)

# c = np.mod(a,b)
# print(c)
