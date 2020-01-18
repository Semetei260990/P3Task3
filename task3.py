list_ = list(input("Введите элементы списка через пробел: ").split())
n = int(input("Значение для сдвига: "))
new_list = list_[-n:] + list_[0:-n]
print (f'Новый список: {new_list} ')

