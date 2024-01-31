# Python module that converts a number to text in Russian

#### Python модуль, преобразующий число в текст на русском языке

```python
from num2text_ru import Num2Text

print(Num2Text(55))
# пятьдесят пять

print(Num2Text(3.14))
# три целых четырнадцать сотых
```

##### Поддержка стандартных операций `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `>=`, `!=`

```python
from num2text_ru import Num2Text

num = Num2Text(55)
print(num + 1)
# пятьдесят шесть

print(num / 2)
# двадцать семь целых пять десятых

print(num * Num2Text(2.1))
# сто пятнадцать целых пять десятых

print(num == 55)
# True

print(num < 56)
# True

num += 1
print(num)
# пятьдесят шесть
```
