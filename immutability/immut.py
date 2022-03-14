l = [[1,2,3],10,12]
m = l
print('l',id(l))
l[0] = [56]
print('l after 0 index',id(l))
print('m',id(m))
print('m',m)
l = [1,2,3]
print('l after re-assign',id(l))
print('m',id(m))