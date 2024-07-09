immutable_var = (1, True, "homework", 1.5, [2022, 12, 5])
print(immutable_var)
#immutable_var[0] = 2
#immutable_var[1] = False
#immutable_var[2] = 'yeye'
#immutable_var[3] = 1.8
#'tuple' object does not support item assignment
immutable_var[4][0] = 'success'
#прошел, потому что значение элементов списка внутри кортежа изменить можно
print(immutable_var)
mutable_list = [1, 1.25, "street", True, [1, 2, 2, 199]]
mutable_list[0] = 2
mutable_list[1] = True
mutable_list[2] = 1
mutable_list[3] = 6.66
mutable_list[4] = "Золотая чаша золотая, наполняет ароматом чая"
print(mutable_list)