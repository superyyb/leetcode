My_food=["carrot","cabbage","beef"]
Friend_food=My_food[:]
My_food.append("icecream")
Friend_food.append("fruit")
print("My_food:",My_food)
print("Friend_food:",Friend_food)

print("-"*40)

My_food=["carrot","cabbage","beef"]
Friend_food=My_food
My_food.append("icecream")
Friend_food.append("fruit")
print("My_food:",My_food)
print("Friend_food:",Friend_food)

print("-"*40)

My_food=["carrot","cabbage","beef","pork","milk"]
for food in My_food[2:5]:
    print(food.title())
print("-"*40)
My_food = ["carrot", "cabbage", "beef", "pork", "milk"]
for food in My_food[:3]:
    print(food.title())
print("-" * 40)
My_food = ["carrot", "cabbage", "beef", "pork", "milk"]
for food in My_food[3:]:
    print(food.title())

print("-" * 40)

alien_color=input("请输入射杀的外星人颜色：")
if alien_color=="green":
    print("5 point got!")
elif alien_color=="yellow":
    print("10 point got!")
elif alien_color=="red":
    print("15 point got!")