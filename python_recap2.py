# # truthy vs falsey 

# # truthy
# print(bool("hello"))
# print(bool(5))


# # falsy
# print(bool(""))
# print(bool(0))


# # ternary operator

# age = 10
# message = "You are old enough" if age > 18 else "You are not old enough" 
# print(message)

# # is check if the location in memory is the same
# print(message is message)


# user = {
#     "name" : "Adrian",
#     "age": 27
# }

# for key in user.keys():
#     print(key)

# for vals in user.values():
#     print(vals)

# for key,value in user.items():
#     print(key ,)



# enumerate - enumerates an iterable variable - gives you the index counter

# for i, value in enumerate("adrian"):
#     print(i, value)

# the code below gives and error
# for i, value in "Adrian":
#     print(i)


# def test(a):
#     '''
#     This is a doc string and will give hits when being used.
#     '''
#     print(a)

# test("hello")

# print(test.__doc__)


# args and kwargs
# accepts dynamic amount of paramaters
def add(*args , **kwargs):
    print(kwargs)
    return sum(args)

print(add(1,2,3,4,5, num1=5,num2=10))



