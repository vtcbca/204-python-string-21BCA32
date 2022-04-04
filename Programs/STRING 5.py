l=[]
for i in range(3):
    s=input("Enter Student Name:")
    l.append(s)
print(l)

b=[]
for i in range(1):
    c=input("Enter Student Address:")
    b.append(c)
print(b)
for i in l:
    for j in b:
        print('{} --> {}'.format(i,j))

