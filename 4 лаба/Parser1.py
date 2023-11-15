import string
# YAML -> XML
f = open('Расписание.json',"r",encoding='utf-8')
f = f.readlines()
tab_count = 0

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
                print(tab_count*'\t' + f'<{firstWord}>')
                count += 1
                a.append(str(firstWord))
            tab_count += 1
    elif i.count('}') == 1 and i.count(',') == 0:
        tab_count -= 1
        if a[count-1] == 'Body':
            print(f'</{a[count-1]}>')
            a.pop(count-1)
            count -= 1  
        else:    
            print(tab_count*'\t' + f'</{a[count-1]}>')
            a.pop(count-1)
            count -= 1  
    elif i.count('},') == 1:
        tab_count -= 1
        print(tab_count*'\t'+f'</{a[count-1]}>')
        a.pop(count-1)
        count -= 1
    else: print(tab_count*'\t'+f'<{firstWord}>{word} </{firstWord}>')
    
#print(f'<{firstword}>' + f'<{word}>' + f'\<{firstword}>')
#print(tab_count)        
#print(str_out)


