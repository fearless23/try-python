# Im-Mutability

- Mutability: Something that can be changed or modified
- Im-Mutability: Something that cannot be changed or modified

# Memory and Reference
```py
a = 1 # a is pointing to a memory address where value is 1
b = a; # c = 1
a = 2;
# c is pointing to a
# if assignment right side is a primitive value
# then value is copied / duplicated

x = [1, 2, 3]
y = x; # reference
y = x[:] # cloning for list
y = x.copy() # cloning for dict
```
## Memory
----------------
| a=1  -> a = 2 |
---------------
| b=a => b=1  |
--------------
| x = [1,2,3] |
--------------
 y = x
--------------
## Time / Complexity (Resources)

## Shallow Copy and Deep Copy
- Shallow Copy: top level copy (Cheap)
- Deep Copy: entire entity copy (Expensive)
```py
x = [
  0, # xa
  1, # xb
  2,
  3, 
  [4,5, 6], # xd
  7,
  8, 
  {
    name: jassi, 
    info: {
      age: 32, 
      city: delhi
    }
  }
]

y = x;
y = [
  0, # za
  1, # zb
  2, # zc
  3, # zd
  [3,4,5] # xd, ze
  7,
  8, 
  #shadow
  {
    name: jassi, 
    info: {
      age: 32, 
      city: delhi
    }
  }
]
```