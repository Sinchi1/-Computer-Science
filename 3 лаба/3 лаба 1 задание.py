import re
def Search(str_input):
    count = re.findall(r'=-{p',str_input)
    return len(count)
    

print(Search('pasdlalskdap=-{pw#@(@#$)@Isqppp=021o3-}')) #6    
print(Search('-0123paos[po2-=13=-{p0psl;-}202=-{p=-{p002skaldp12=]')) 
print(Search('a;=-{plgf[dspogs0aor[]ewpe=1][SAL;]')) 
print(Search('ydgaoXLK:,ms;lrtauiow[pdla;s')) #1
print(Search('GHFDJM=-{pTNRYUSKDFJNSMI12093I21PO90S')) 
alph = ['=-{p']




