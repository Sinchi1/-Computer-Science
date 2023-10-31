import re 

def matches(str_input):
    return re.findall(r'(\w+)\-\1|([А-Я])\.\1',str_input) #Нужно показать что регулярка к разным относится ПОД ВОПРОСОМ

print(matches('Петров П.П. P0000 Анищенко А.А. P33113 Примеров Е.В. P0000 Иванов И.И. P0000'))