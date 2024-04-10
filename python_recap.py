# # datatypes
# print("Hello")

# # integer
# print(type(3))

# # float
# print(type(.25))

# # powers
# print(2 ** 2)

# # rounded down
# print(1 // 2)

# # math functions
# print(round(3.9))
# print(abs(-100))

# # binary
# print(bin(5))
# print(int('0b101' , 2))


# print("""
# Multi
# Line
# Strings

# """)


# hello = "01234"
# # hello[start, stop_excluded, stepover]
# print(hello[0 : 5 : 2])
# print(hello[0:]) # defaults the stop to he 5
# print(hello[:5]) # defaults the start to be 0
# print(hello[::1]) #defaults the start and stop 


# print(hello[-1]) #grabs the last element
# print(hello[-5]) #grabs the first element
# print(hello[::-1]) #steps over in reverse
# print(hello[::-2]) #steps over in reverse by 2

# # immutability
# selfish = '1234567'

# selfish = 'a'
# print(selfish)

# # other functions

# quote = "to be or not to be"
# print(quote.find("be"))
# print(quote.replace("be", "ha"))

# # copying a list
# li = [1,2,3,4]
# print(li)
# li2 = li[:]
# li2[0] = 0
# print(li2)


# # list funtion

# basket = [1,2,3,4,5]
# basket.append(100) #append value to end of list
# basket.insert(2,200) # insert at index 2
# basket.extend([200]) # append at end of list

# print(basket.pop()) # pop at end
# print(basket.pop(1)) # pop at index
# print(basket)


# basket.clear() # empty the list
# print(basket)

# nw_basket = [1,2,3,"111",5, 1]
# print(nw_basket.index("111"))  #return index where the value is 111
# print(nw_basket.index("111", 0 , 4))  #return index where the value is 111 between the range of 0 and 4
# print("111" in nw_basket)

# print(nw_basket.count(1))



# range
# print(list(range(1,100)))


# list unpacking
# a,b,c, *other , d= 1,2,3,4,5,6,7,8
# print(other) # [4, 5, 6, 7, 8]


# dictioinaries

# my_dic = {
#     "name": "Adrian",
#     "skl": "usd"
# }
# # print(my_dic["age"]) # this would give an error
# print(my_dic.get("age", 10))  #this defaults a value and avoids an error
# print(my_dic)




# my_dic2 = dict(name = "Adrian", age = 100)
# print(my_dic2)


# tuple, faster than a list but immutable and cannot change
tuplee = (1,2,3,4,5)








