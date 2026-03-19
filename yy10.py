My_pet=["小绿","小红","小白"]
for pet in My_pet:
    print(pet,"really eats a lot in summer." )
print("But I really love them!")

#列表解析
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)

print("-"*40)

squares=[value**2 for value in range(1,11)]
print(squares)

print("-"*40)

squares=[]
for value in range(1,1000000):
    squares.append(value)
print(min(squares),max(squares),sum(squares))

print("-"*40)

squares=[]
for value in range(1,21):
    if value%2!=0:
        squares.append(value)
print(squares)

print("-"*40)

squares=[]
for value in range(3,31):
    if value%3==0:
        squares.append(value)
print(squares)

print("-"*40)

squares=[]
for value in range(1,11):
    squares.append(value**3)
print(squares)