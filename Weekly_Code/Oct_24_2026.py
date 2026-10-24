'''
name = input("please enter a name:")
num1=int(input("please enter a number:"))
num2=int(input("please enter another number:"))
num3=int(input("please enter another number:"))
print(name, "is" , num1+num2+num3, "pounds")


for letters in name:
    print(letters)
'''
'''
word = input("please enter a word")
letters=["e"]
for letters in word:
    print(letters)
'''
word=input("please enter")
count=0
checker = ["e"]
for letter in word:
    if letter in checker:
        count=count+1
print(count)
