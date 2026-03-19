dic_ticket={
        "G1569":["北京南-天津南", "18:06", "18:39", "00:33"],
        "G1567":["北京南-天津南", "18:15", "18:49", "00:34"],
        "G8917":["北京南-天津南", "18:20", "19:19", "00:59"],
        "G203":["北京南-天津南", "18:35", "19:09", "00:34"]
    }
print("车次  出发站-到达站  出发时间  到达时间隔  历时时长")
for key in dic_ticket:#.keys():
    print(key,end=" ")
    for item in dic_ticket.get(key):
        print(item,end="\t")
    print()
train_no=input("请输入买的车次：")
info=dic_ticket.get(train_no,"车次不存在")#info是列表
if info!="车次不存在":
    person=input("请输入多位联系人")
    s=info[0]+info[1]
    print("您已购买了",train_no,s,"开的车票，请",person,"尽快换取纸质车票。【铁路客服】")
else:
    print("输入有误")
