lst1=["车次","出发站-到达站","出发时间","到达时间隔","历时时长"]
lst2=["G1569","北京南-天津南","18:06","18:39","00:33"]
lst3=["G1567","北京南-天津南","18:15","18:49","00:34"]
lst4=["G8917","北京南-天津南","18:20","19:19","00:59"]
lst5=["G203","北京南-天津南","18:35","19:09","00:34"]
print(lst1,"\n",lst2,"\n",lst3,"\n",lst4,"\n",lst5)
while True:
    user_ticket=input("请输入要购买的车次：")
    user_name=input("请输入乘车人，若多位乘车人请用逗号分隔：")
    ticket_list=[lst2,lst3,lst4,lst5]
#for index in range(0,len(lst1)):
    found=False
    for ticket in ticket_list:
        if user_ticket in ticket[0]:
            print("您已购买了",ticket[0],ticket[1],ticket[2],"开的车票，请",user_name,"尽快换取纸质车票。【铁路客服】")
            found=True
            break
    if found==False:
        print("请重新选择正确的车票：")
    else:
        break#购票成功后退出循环

dic_ticket={
        "G1569":["北京南-天津南", "18:06", "18:39", "00:33"],
        "G1567":["北京南-天津南", "18:15", "18:49", "00:34"],
        "G8917":["北京南-天津南", "18:20", "19:19", "00:59"],
        "G203":["北京南-天津南", "18:35", "19:09", "00:34"]
    }
    print("车次  出发站-到达站  出发时间  到达时间隔  历时时长")
for key in dic_ticket.key():
    print(key,end="")
for item in dic_ticket.get(key):
    print(item,end="")



