s=input("Enter any string:")
l=len(s)
a=s[:1//2]
b=s[1//2:]
if(a==b):
    print ("{} string is a symmetrical" .format(s))
else:
    print("{} string isn't a symmetrical".format(s))
