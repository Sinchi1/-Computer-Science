import re 

def regReplace(str_input):
    return re.sub(r'\s(?:[1][0-9]|[2][0-3]|[0][0-9]):[0-5][0-9]:[0-5][0-9](?:[\s|.])|\s(?:[1][0-9]|[2][0-3]|[0][0-9]):[0-5][0-9](?:[\s|.])',' (TBD) ',str_input)

print(regReplace('Уважаемые студенты! B эту субботу в 15:00 планируется доп. занятие на 2 часа.To есть в 17:00:00 оно уже точно кончится. '))
print(regReplace('fdglk340ro40[w=-31o2ws;k-02] 01:23:56 3glk4034 14:32:34.'))
print(regReplace('lxkvpodsid30294=-646ot0dzP43P{43 08:00:23 g.fkdg3-2420:4032 06:58.'))
print(regReplace('адлфыдадфлыажфыда 17:43:10 4 fgldkg 00:58.'))
print(regReplace('д45-6045-0f054045 28:435:23%$)05лвфыдл 34:54.'))
