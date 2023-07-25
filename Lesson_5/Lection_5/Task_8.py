a = b = c = 42

if a == b == c:
    print('Full coincidence')


if a < b < c:
    print('b > a and b < c')

#Full coincidence

data = {10,9,8,1,6,3}
a,b,c,*d,e = data
print(a,b,c,d,e)