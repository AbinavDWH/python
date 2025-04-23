print(4/(3*(2-1)))
x='a'
y='a'
print(id(x)==id(y))
#4=
a=10
b=5
a=a^b
b=a^b
a=a^b
print(a,b)
#for i in range(10):
#    if i%2==0:
#        print(i)
#   else:
#        print(-i)
ly_list = [1, 5, 3, 4]
ly_list.sort()
print(ly_list)
for idx, val in enumerate(['a', 'b']):
    print(idx, val)
# 5
for a, b in zip([1, 2], ['a', 'b']):
    print(a, b)  # 1 a \n 2 b

for i in reversed([1, 2, 3]):
    print(i)  # 3 2 1

for i in reversed([1, 2, 3]):
    print(i)  # 3 2 1

my_list = [1, 2, 3]
print(my_list.index(2))  # 1

print([1, 2, 2, 3].count(2))  # 2

my_list = [1, 2, 3]
print(my_list.pop(2))  # 3

my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # [1, 10, 2, 3]

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2]

print("HELLO".lower())  # hello

print("hello".find('e'))  # 1

print(isinstance(5, int))  # True

print(type(5))  # <class 'int'>

print(all([True, True, False]))  # False

print(any([False, False, True]))  # True

print("  hello  ".strip())  # 'hello'

print("hello".startswith("he"))  # True

print("hello".endswith("lo"))  # True

my_list = [1, 2, 3]
str_list = [str(x) for x in my_list]
print(str_list)  # Output: ['1', '2', '3']

my_list = [1, 2, 3]
result = ''.join(str(x) for x in my_list)
print(result)  # Output: '123'
