dict={"huangheriver":"china","nile":"egypt","xx":"USA"}
for river,country in dict.items():
    print(river.title(),"runs through",country )
for river in dict.keys():
    print(river.title())
for country in dict.values():
    print(country.title())

print("------------------------------")

favorite_language={"aa":"english","bb":"chinese","cc":"french","dd":"german","ee":"janpanese"}
survey_list=["aa","22","33","ee","66","dd","jj"]
for person in survey_list:
    if person in favorite_language.keys():
        print(person,"，感谢您接受调查！")
    else:
        print(person,"请尽快接受调查！")
