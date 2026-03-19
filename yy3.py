
while True:
    print("Who are you?")
    name=input()
    if name!="J":
        continue
    print("Hello,J. What is the password?")
    password=input("It's a fish.")
    if password=="s":
        break
print("Access granted!")

print("What's your name?")
for i in range(10):
    print("Jimmy 10 times"+"("+str(i)+")")

total=0
for num in range(101):
    total=total+num
print(total)

