import re 

def matches(str_input):
    c = [a.group() for a in re.finditer(r'(\w+)\-\1\s[А-Я]\.[А-Я].\sР(3114)',str_input)]
    d = [b.group() for b in re.finditer(r'\w+\s([А-Я])\.\1\.\sР(3114)', str_input)]
    a = re.sub(r'(\w+)\-\1\s[А-Я]\.[А-Я].\sР(3114)',' (TBD) ',str_input)
    a = re.sub(r'\w+\s([А-Я])\.\1\.\sР(3114)',' (TBD) ',a)
    return print(a,c,d)
    
    '''
    if len(a) > 0 or len(b) > 0:
        if len(a) > 0 and len(b) == 0:
            return print(a)
        if len(a) == 0 and len(b) > 0: 
            return print(b)
        else: return print(a,b)
    else: return print('Выражений не найдено!')
    '''

matches('Трусковский Г.А. Р3114 Гофман И.Н. Р7878 Спартак Н.В. Р5678') # 0
matches('Трусковский-Трусковский Г.А. Р3114 Федченко К.К. Р3114 Рыжик М.М. Р3245') # Федченко + Рыжик
matches('Трусковский Г.А. Р3114 Гофман И.И. Р7878 Спартак-Спартак Н.В. Р5678') # Cпартак
matches('Трусковский Г.А. Р3114 Гофман-Гофман И.Н. Р7878 Огарков И.И. Р5678') # Гофман+Огарков
matches('Лапинский С.С. Р3114 Сепьев-Сепьев К.Н. Р7878 Цветков И.И. Р5678') # Все