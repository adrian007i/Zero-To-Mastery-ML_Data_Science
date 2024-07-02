def format_str(item):
    return f"/{item}/"

def odds(item):
    return item % 2 == 1

print(list(map(format_str, [1,2,3])))
print(list(filter(odds, [1,2,3])))
print(list(zip("abc", [1,2,3])))

def accumulator(acc , item):
    return acc + item

from functools import reduce
print(reduce(accumulator, [1,2,3] , 10))


# list comprehensions

my_list = [char for char in 'hello']
print(my_list)


my_list2 = [num * 2 for num in range(0,10)]
print(my_list2)

my_list3 = [num * 2 for num in range(0,10) if num % 2 == 0]
print(my_list3)


# dictionary comprehension

my_dict4 = {num:num*2 for num in [1,2,3]}
print(my_dict4)
 