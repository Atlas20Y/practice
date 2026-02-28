prices = [11, 12, 34, 1, 45, 13, 19, 10]

all_positive = all([p > 0 for p in prices])  # all как логическое И собирает все значения из генератора
has_one_digit_element = any([p < 10 for p in prices])  # any возвращает тру если есть хотябы один елемент true

print(all_positive)
