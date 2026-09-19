'''
a=0.2
b=0.4
c=0.6
a=2
b=4
c=6
a="cow"
b="tiger"
c="kourt"
a=True
b=False
c=True
'''

name=""
name1=input("Please enter any name: ")
name2=input("Please enter another name:")

l1 = len(name1)
l2 = len(name2)

if l1>l2:
    print(name1)
else:
    print(name2)
