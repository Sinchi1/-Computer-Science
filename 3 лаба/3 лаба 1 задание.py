import re
def Search(str_input):
    count = re.findall(r'=|-{|p',str_input)
    return len(count)
    

print(Search('pasdlalskdapw#@(@#$)@Isqppp=021o3-}')) #6    
print(Search('-0123paos[po2-=130psl;-}202002skaldp12=]')) 
print(Search('a;lgf[dspogs0aor[]ewpe=1][SAL;]')) 
print(Search('ydgaoXLK:,ms;lrtauiow[pdla;s')) 
print(Search('GHFDJMTNRYUSKDFJNSMI12093I21PO90S')) 
alph = ['=','-{','p']




