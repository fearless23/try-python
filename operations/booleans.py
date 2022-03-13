# 
"""
AND - OR
T, F

T | T - T
T & T - T

F | F - F
F & F - F

T & F - F
T | F - T


// examples
 T & (T & F | T & F)
"""

A = True  # 1
B = False # 0

# Truthy / Falsy
# values which are not True / False but can be constructed as such
# "jassi" -> Truthy -> True
# 0 -> Falsy -> False
# 1 -> Truthy -> True
# [] -> falsy
# {} -> falsy

C = A + B
D = A * B

E = A and B
F = A or B or False or True
G = 0 or False or {} or [] 
H = [1] and True or 8 or {'name': '1'} 
# true or false -> true -> {}; 
# false or false -> false -> {}
print(G,H)
