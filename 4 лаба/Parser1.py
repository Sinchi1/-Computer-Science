import re
import string
# YAML -> XML
f = open('Расписание.json',"r",encoding='utf-8')
f = f.readlines()
tab_count = 0
'''

for i in f:
    if i.count("-") == 1:
        str_out += ''.join(map(str,(re.findall(r'-\s(?:.+):',i)))) # Поиск открытого списка
        str_out += ''.join(map(str,(re.findall(r'(\s\"\w+\")',i)))) # Объект 
        tab_count += 1
        str_out += tab_count*'\t'
        str_out += '\n'
    else:
        if re.match(r':\s\s',i):
            str_out += ''.join(map(str,(re.findall(r'(\w+:\s)',i))))
            tab_count += 1
            str_out += tab_count*'\t'
        elif re.match(r':\s\s',i) == None:
            str_out += ''.join(map(str,(re.findall(r'(\w+:\s)',i)))) #Ключ 
            str_out += ''.join(map(str,(re.findall(r'\"(.+)\"',i)))) # Объект  
            tab_count += 1
            str_out += tab_count*'\t'
            str_out += '\n'
        else:
            str_out += ''.join(map(str,(re.findall(r'(\w+:\s)',i))))
            str_out += ''.join(map(str,(re.findall(r'\"(.+)\"',i))))
            str_out += tab_count*'\t'
            str_out += '\n'
'''
'''
str_key = 0
for i in f:
    if i.count('"')+i.count('{') == 1:
        print('<Body>')
        tab_count += 1 
    elif '"' in i and  ':' in i and ',' in i: 
        a = ''.join(map(str,re.findall(r'\"(.+)\":',i)))
        b = ''.join(map(str,re.findall(r':\s\"(.+)\"',i)))
        print(tab_count*'\t'+f'<{a}>{b}</{a}>')
    elif '"' in i and ':' in i and '{' in i:
        a = ''.join(map(str,re.findall(r'\"(.+)\":',i)))
        print(tab_count*'\t'+f'<{a}>')
'''


alph = list(string.ascii_letters)    
tab_count = 1
last = ''
firstWord = ''
count = 0
tab_count = 0
a = []
print('<?xml version="1.0" encoding="utf-8"?>')
for i in f:
    word = ''
    firstWord = 'Body'
    for j in i: 
        if j in alph or j in '0123456789-':
            letter = j
            word += j 
        if j == ':' and last == '"':
            firstWord = word
            word = ''
        last = j
    for b in i:
        if b in alph or b in '0123456789:- ':
            letter = b
            word += b
        if b == ':' and last == '"':
            word = ''   
        last = b
    if i.count('{') == 1:
            if firstWord == 'Body':
                print(f'<{firstWord}>')
                count += 1
                a.append(str(firstWord))
            else:
                print(f'\t<{firstWord}>')
                count += 1
                a.append(str(firstWord))
    elif i.count('}') == 1 and i.count(',') == 0:
        if a[count-1] == 'Body':
            print(f'</{a[count-1]}>')
            a.pop(count-1)
            count -= 1  
        else:    
            print(f'\t</{a[count-1]}>')
            a.pop(count-1)
            count -= 1  
    elif i.count('},') == 1:
        print(f'\t</{a[count-1]}>')
        a.pop(count-1)
        count -= 1
    else: print(f'\t<{firstWord}>{word} </{firstWord}>')

print(a)
        

    #print(f'<{firstword}>' + f'<{word}>' + f'\<{firstword}>')
  






#print(tab_count)        
#print(str_out)


