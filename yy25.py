# def make_album(singer_name,song_name,song_num=""):
#     album={"singer":singer_name,"song":song_name}
#     if song_num:
#         album["song_num"]=song_num#为什么key和value可以命名一样
#     return album
# album_one=make_album("aa","sun","5")
# print(album_one)

def make_album(singer_name,song_name,song_num=""):
    album={"singer":singer_name,"song":song_name}
    if song_num:
        album["song_num"]=song_num
    return album
while True:
    singer_name=input("请输入您喜爱的歌手：")
    if singer_name=="q":
        break
    else:
        song_name=input("请输入他的代表歌曲：")
        song_num=input("请输入专辑曲目数量：")
        album=make_album(singer_name,song_name,song_num)
        print(album)

