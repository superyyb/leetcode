#自动生成30个外星人
aliens=[]#创建空列表
for i in range(30):
    new_alien={"color":"yellow","point":5}
    aliens.append(new_alien)
print(aliens[:5])
#等同于：（是否换行的区别）
for alien in aliens[:5]:
    print(alien)
print("total number of aliens:",str(len(aliens)))

#修改前五个外星人的参数
for alien in aliens[:5]:
    if alien["color"]=="yellow":
        alien["color"]="green"
        alien["point"]=10
        alien["speed"]="medium"
for alien in aliens[:5]:
    if alien["color"]=="yellow":
        alien["color"]="green"
        alien["point"]=10
        alien["speed"]="medium"
for alien in aliens:
    print(alien)
print("______________________")


for alien in aliens[:5]:
    if alien["color"]=="green":
        alien["color"] = "red"
        alien["point"] = 15
        alien["speed"] = "fast"
    elif alien["color"]=="green":
        alien["color"] = "purple"
        alien["point"] = 20
        alien["speed"] = "slow"
# for alien in aliens[:10]:
#     if alien["color"]=="yellow":
#         alien["color"]="red"
#         alien["point"]=15
#         alien["speed"]="fast"

favorite_places={"alice":["aa","bb","cc"],"bob":["ee"],"clare":["ff","gg"]
                 }
for name in favorite_places.keys():
    print(name.title(),"‘s favorite place is ")
    for place in favorite_places[name]:#根据key获取value
        print(place)


print("______________________")

for places in place:
    print(places)