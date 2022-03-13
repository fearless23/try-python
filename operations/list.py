tuplee = (1,2,3)
fruits = ['apple', 'grapes', ['guava1', 'guaVa2']]
#           0         1             2
cars = ['swift', 'nano', 'mercedes', 'lamborgini']
user = {
    'name': 'happy',
    'age': 34
}
numbers = [1,2,'sdfsdfsdfsdfd',user,tuplee, fruits, cars]
#          0 1     2            3     4       5      6
#         -7 -6    -5           -4   -3      -2     -1 

len = len(numbers)
print('length', len)

# operations
# Accessibility - bracket notation list[index]
# length = 7, 
# index =>  0 to 6 <7-1>
# neg index => -1 to -7
# x = numbers[4]
x = numbers[-5]
# print(x)

# assign
numbers[3] = 'happy'
# print(numbers)

y = numbers[5][2][1][3]
print(y)

# 