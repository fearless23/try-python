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

# Method - len(list) -> int
nums = [7,8,9,10]
x = len(nums)
print('length of nums', x)

# Method - Push to list
g = "abc" # each item of g: a,b,c
g = 56  # each item -> error
g = [1, 2, 3] # each item => 1, 2, 3
g = [1, 2, 3, [4,5]] # each item => 1, 2, 3, [4,5]
g = { "age": 32, "name":'jassi', "info": {"pop": 250} } # each item => top level key of dict
g = ["a", 'b','c']; # each item => a, b, c
nums.append(g) # add g to end
nums.extend(g) # add each item of g to end, g should be iterable (string, list, dict:(keys))
# print(nums)
# Changes the original array => Mutable

# Method - removing from list
# .pop changes the original array => Mutable
f = [1,2,3,4,5,[1,2,3]]
h = f.pop() # remove the last element of the list
print('h pop()', h)
h2 = f.pop() # remove the last element of the list
print('h2 pop()', h2)
# [1,2,3,4]
h3 = f.pop(2)
print('h3 pop(2)', h3)
print('--->',f)

# Method -> insert at index
p = [1,2,3]
p.insert(2,"jassi")
print('p --> ', p)

# Method -> index, find thes the value
z = ["jassi", 23, 45, 78, 90, 78, 91,  {"name":"jassi"}, ["jassi","jassi"],"jassi",]
j = z.index({"name":"jassi"},2)
print('index of 90 -->', j)
k = z.count("jassi")
print('jassi occured -->', k)
z.remove("jassi")
print('z', z)

z.reverse() # Mutable
print(z)