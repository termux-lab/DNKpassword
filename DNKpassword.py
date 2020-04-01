import vk, os, sys, colorama, random
os.system("clear")
dilefor = random.randint(0,9999)
passgen = []
newspass = []
arg = 1
while True:
    try:
        nwp = sys.argv[arg]
        passgen.append(nwp)
        newspass.append(nwp)
        arg+=1
    except:
        break
def passGen():
    try:
        BDate()
    except:
        return False
    try:
        lastName()
    except:
        return False
    try:
        firstName()
    except:
        return False
    try:
        CityUser()
    except:
        return False
    try:
        HomeCity()
    except:
        return False
    try:
        DomainUser()
    except:
        return False
    try:
        HomeP()
    except:
        return False
    try:
        MobileP()
    except:
        return False
    try:
        SiteUser()
    except:
        return False
def BDate():
    date = b['bdate']
    mod_date = date.split('.')
    date1 = mod_date[0]
    date2 = mod_date[1]
    date3 = mod_date[2]
    date4 = str(date1)+str(date2)
    date5 = str(date2)+str(date1)
    date6 = str(date2)+str(date3)
    date7 = str(date3)+str(date2)
    date8 = str(date1)+str(date3)
    date9 = str(date3)+str(date1)
    date = str(date1)+str(date2)+str(date3)
    passgen.append(date)
    passgen.append(date1)
    passgen.append(date2)
    passgen.append(date3)
    passgen.append(date4)
    passgen.append(date5)
    passgen.append(date6)
    passgen.append(date7)
    passgen.append(date8)
    passgen.append(date9)
def lastName():
    lastN = b['last_name']
    lastN1 = str(lastN[0])+str(lastN[1])
    lastN2 = str(lastN[1])+str(lastN[2])+str(lastN[3])+str(lastN[4])
    LAST = lastN.lower()
    LAST1 = lastN1.lower()
    LAST2 = lastN2.lower()
    LAST0 = lastN.upper()
    LAST01 = lastN1.upper()
    LAST02 = lastN2.upper()
    lastN3 = lastN.replace('й', 'i').replace('ц', 'ts').replace('у', 'y').replace('к', 'k').replace('е', 'e').replace('н', 'n').replace('г', 'g').replace('ш', 'sh').replace('щ', 'shch').replace('з', 'z').replace('х', 'h').replace('ъ', "").replace('ф', 'f').replace('ы', 'i').replace('в', 'v').replace('а', 'a').replace('п', 'p').replace('р', 'r').replace('о', 'o').replace('л', 'l').replace('д', 'd').replace('ж', 'zg').replace('я', 'ya').replace('ч', 'ch').replace('с', 's').replace('м', 'm').replace('и', 'i').replace('т', 't').replace('ь', "").replace('б', 'b').replace('ю', 'yu').replace('Й', 'I').replace('Ц', 'TS').replace('У', 'Y').replace('К', 'K').replace('Е', 'E').replace('Н', 'N').replace('Г', 'G').replace('Ш', 'SH').replace('Щ', 'SHCH').replace('З', 'Z').replace('Х', 'H').replace('Ъ', "'").replace('Ф', 'F').replace('Ы', 'Y').replace('В', 'V').replace('А', 'A').replace('П', 'P').replace('Р', 'R').replace('О', 'O').replace('Л', 'L').replace('Д', 'D').replace('Ж', 'ZH').replace('Э', 'E').replace('Я', 'YA').replace('Ч', 'CH').replace('С', 'S').replace('М', 'M').replace('И', 'I').replace('Т', 'T').replace('Ь', "'").replace('Б', 'B').replace('Ю', 'YU').replace('э', 'е').replace('ё', 'e').replace('Ё', 'E')
    lastN31 = str(lastN3[0])+str(lastN3[1])
    lastN32 = str(lastN3[1])+str(lastN3[2])+str(lastN3[3])+str(lastN3[4])
    lastN30 = lastN3.lower()
    last311 = lastN31.lower()
    last321 = lastN32.lower()
    lastN3110 = lastN3.upper()
    last312 = lastN31.upper()
    last322 = lastN32.upper()
    passgen.append(lastN)
    passgen.append(lastN1)
    passgen.append(lastN2)
    passgen.append(LAST)
    passgen.append(LAST1)
    passgen.append(LAST2)
    passgen.append(LAST0)
    passgen.append(LAST01)
    passgen.append(LAST02)
    passgen.append(lastN3)
    passgen.append(lastN31)
    passgen.append(lastN32)
    passgen.append(lastN30)
    passgen.append(last311)
    passgen.append(last321)
    passgen.append(lastN3110)
    passgen.append(last312)
    passgen.append(last322)
def firstName():
    firstN = b['first_name']
    firstN1 = str(firstN[0])+str(firstN[1])
    firstN2 = str(firstN[1])+str(firstN[2])+str(firstN[3])+str(firstN[4])
    FIRST = firstN.lower()
    FIRST1 = firstN1.lower()
    FIRST2 = firstN2.lower()
    FIRST0 = firstN.upper()
    FIRST01 = firstN1.upper()
    FIRST02 = firstN2.upper()
    firstN3 = firstN.replace('й', 'i').replace('ц', 'ts').replace('у', 'y').replace('к', 'k').replace('е', 'e').replace('н', 'n').replace('г', 'g').replace('ш', 'sh').replace('щ', 'shch').replace('з', 'z').replace('х', 'h').replace('ъ', "'").replace('ф', 'f').replace('ы', 'i').replace('в', 'v').replace('а', 'a').replace('п', 'p').replace('р', 'r').replace('о', 'o').replace('л', 'l').replace('д', 'd').replace('ж', 'zg').replace('я', 'ya').replace('ч', 'ch').replace('с', 's').replace('м', 'm').replace('и', 'i').replace('т', 't').replace('ь', "'").replace('б', 'b').replace('ю', 'yu').replace('Й', 'I').replace('Ц', 'TS').replace('У', 'Y').replace('К', 'K').replace('Е', 'E').replace('Н', 'N').replace('Г', 'G').replace('Ш', 'SH').replace('Щ', 'SHCH').replace('З', 'Z').replace('Х', 'H').replace('Ъ', "'").replace('Ф', 'F').replace('Ы', 'Y').replace('В', 'V').replace('А', 'A').replace('П', 'P').replace('Р', 'R').replace('О', 'O').replace('Л', 'L').replace('Д', 'D').replace('Ж', 'ZH').replace('Э', 'E').replace('Я', 'YA').replace('Ч', 'CH').replace('С', 'S').replace('М', 'M').replace('И', 'I').replace('Т', 'T').replace('Ь', "'").replace('Б', 'B').replace('Ю', 'YU').replace('э', 'е').replace('ё', 'e').replace('Ё', 'E')
    firstN31 = str(firstN3[0])+str(firstN3[1])
    firstN32 = str(firstN3[1])+str(firstN3[2])+str(firstN3[3])+str(firstN3[4])
    firstN30 = firstN3.lower()
    first311 = firstN31.lower()
    first321 = firstN32.lower()
    firstN3110 = firstN3.upper()
    first312 = firstN31.upper()
    first322 = firstN32.upper()
    passgen.append(firstN)
    passgen.append(firstN1)
    passgen.append(firstN2)
    passgen.append(FIRST)
    passgen.append(FIRST1)
    passgen.append(FIRST2)
    passgen.append(FIRST0)
    passgen.append(FIRST01)
    passgen.append(FIRST02)
    passgen.append(firstN3)
    passgen.append(firstN31)
    passgen.append(firstN32)
    passgen.append(firstN30)
    passgen.append(first311)
    passgen.append(first321)
    passgen.append(firstN3110)
    passgen.append(first312)
    passgen.append(first322)
def CityUser():
    city = b['city']['title']
    Ducity1 = city.partition('-')[2]
    Ducity2 = city.partition('-')[0]
    DUCITY1 = Ducity1.upper()
    DUCITY2 = Ducity2.upper()
    ducity1 = Ducity1.lower()
    ducity2 = Ducity2.lower()
    passgen.append(Ducity1)
    passgen.append(Ducity2)
    passgen.append(DUCITY1)
    passgen.append(DUCITY2)
    passgen.append(ducity1)
    passgen.append(ducity2)
    cityN1 = str(city[0])+str(city[1])
    cityN2 = str(city[1])+str(city[2])+str(city[3])+str(city[4])
    CITY = city.lower()
    CITY1 = cityN1.lower()
    CITY2 = cityN2.lower()
    cityN3 = city.replace('й', 'i').replace('ц', 'ts').replace('у', 'y').replace('к', 'k').replace('е', 'e').replace('н', 'n').replace('г', 'g').replace('ш', 'sh').replace('щ', 'shch').replace('з', 'z').replace('х', 'h').replace('ъ', "").replace('ф', 'f').replace('ы', 'i').replace('в', 'v').replace('а', 'a').replace('п', 'p').replace('р', 'r').replace('о', 'o').replace('л', 'l').replace('д', 'd').replace('ж', 'zg').replace('я', 'ya').replace('ч', 'ch').replace('с', 's').replace('м', 'm').replace('и', 'y').replace('т', 't').replace('ь', "").replace('б', 'b').replace('ю', 'yu').replace('Й', 'I').replace('Ц', 'TS').replace('У', 'Y').replace('К', 'K').replace('Е', 'E').replace('Н', 'N').replace('Г', 'G').replace('Ш', 'SH').replace('Щ', 'SHCH').replace('З', 'Z').replace('Х', 'H').replace('Ъ', "'").replace('Ф', 'F').replace('Ы', 'Y').replace('В', 'V').replace('А', 'A').replace('П', 'P').replace('Р', 'R').replace('О', 'O').replace('Л', 'L').replace('Д', 'D').replace('Ж', 'ZH').replace('Э', 'E').replace('Я', 'YA').replace('Ч', 'CH').replace('С', 'S').replace('М', 'M').replace('И', 'I').replace('Т', 'T').replace('Ь', "'").replace('Б', 'B').replace('Ю', 'YU').replace('э', 'е').replace('É', 'E').replace('é', 'e').replace('ё', 'e').replace('Ё', 'E')
    Ducity12 = cityN3.partition('-')[2]
    Ducity22 = cityN3.partition('-')[0]
    DUCITY12 = Ducity12.upper()
    DUCITY22 = Ducity22.upper()
    ducity12 = Ducity12.lower()
    ducity22 = Ducity22.lower()
    passgen.append(Ducity12)
    passgen.append(Ducity22)
    passgen.append(DUCITY12)
    passgen.append(DUCITY22)
    passgen.append(ducity12)
    passgen.append(ducity22)
    cityN31 = str(cityN3[0])+str(cityN3[1])
    cityN321 = str(cityN3[0])+str(cityN3[1])+str(cityN3[2])
    cityN322 = cityN31.lower()
    cityN323 = cityN321.upper()
    cityN32 = str(cityN3[1])+str(cityN3[2])+str(cityN3[3])+str(cityN3[4])
    cityN30 = cityN3.lower()
    city311 = cityN31.lower()
    city321 = cityN32.lower()
    citybig = cityN3.upper()
    passgen.append(city)
    passgen.append(cityN1)
    passgen.append(cityN2)
    passgen.append(CITY)
    passgen.append(CITY1)
    passgen.append(CITY2)
    passgen.append(cityN3)
    passgen.append(cityN31)
    passgen.append(cityN321)
    passgen.append(cityN322)
    passgen.append(cityN323)
    passgen.append(cityN32)
    passgen.append(cityN30)
    passgen.append(city311)
    passgen.append(city321)
    passgen.append(citybig)
def HomeCity():
    home_city = b['home_town']
    passgen.append(home_city)
def DomainUser():
    domain = b['domain']
    domain2 = domain.upper()
    passgen.extend([domain])
    passgen.extend([domain2])
def HomeP():
    has_mobile = b['home_phone']
    has_mobile = str(has_mobile.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', ''))
    ths1 = has_mobile
    hm = str(has_mobile[-4] + has_mobile[-3] + has_mobile[-2] + has_mobile[-1])
    hm1 = has_mobile[-7] + has_mobile[-6] + has_mobile[-5] + has_mobile[-4] + has_mobile[-3] + has_mobile[-2] + has_mobile[-1]
    passgen.append(hm)
    passgen.append(hm1)
def MobileP():
    mobile = b['mobile_phone']
    mobile = mobile.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    mms1 = mobile
    mm = mobile[-4] + mobile[-3] + mobile[-2] + mobile[-1]
    mm1 = mobile[-7] + mobile[-6] + mobile[-5] + mobile[-4] + mobile[-3] + mobile[-2] + mobile[-1]
    passgen.append(mm)
    passgen.append(mm1)
    passgen.append(mms1)
def SiteUser():
    site = b['site']
    site1 = site.replace('https://', '').replace('http://', '').replace('www.', '').replace('www', '')
    test2 = site1.partition('/')[2]
    test3 = test2.partition('-')[2]
    test4 = test2.partition('-')[0]
    passgen.append(test2)
    passgen.append(test3)
    passgen.append(test4)
print("""
dnk
\033[31mO\033[0m       \033[34mo O\033[0m dnk   \033[31mo O\033[0m       \033[34mo\033[0m       dnk
| \033[31mO\033[0m   \033[34mo\033[0m | | \033[34mO\033[0m   \033[31mo\033[0m | | \033[31mO\033[0m   \033[34mo\033[0m |dnk
| | \033[31mO\033[0m | | | | \033[34mO\033[0m | | | | \033[31mO\033[0m | |
| \033[34mo\033[0m   \033[31mO\033[0m | | \033[31mo\033[0m   \033[34mO\033[0m | | \033[34mo\033[0m   \033[31mO\033[0m |  dnk
\033[34mo\033[0m  dnk  \033[31mO o\033[0m       \033[34mO o\033[0m       \033[31mO\033[0m
dnk            dnk
                          dnk
||======[\033[33mDNKPASSWORD\033[0m]==-----\033[44m(\033[31mVK.\033[0m\033[44mCOM/ID0)\033[0m
                           \033[31m.\033[0m
                           \033[31m.\033[0m
                          \033[31m.\033[0m
""")
if newspass!=[]:
    print("Add = "+str(newspass))
token = input("[!]Access Token: ")
uidser = input("[!]User ID: ")
try:
    session = vk.Session(access_token=token)
    api = vk.API(session ,v='5.103', lang='ru')
    b = api.users.get(user_ids=uidser, fields="domain, bdate, city, contacts, domain, site, home_town")[0]
    numb='1'
except:
    numb='0'
    print("""[*]Token or user ID entered incorrectly""")
try:
    session = vk.Session(access_token=token)
    api = vk.API(session ,v='5.103', lang='ru')
    api.groups.join(group_id=191415465)
except:
    print("""[*]Plaese, update Token""")
if numb == "1":
    passGen()
    ist=0
    isto=0
    ist1=0
    isto1=0
    istos=0
    res=0
    while True:
        try:
            if ist >= len(passgen):
                isto+=1
                ist=0
            dnk = passgen[isto]+passgen[ist]
            print(dnk)
            f = open('DnkPass_'+str(dilefor)+'.txt','a+')
            f.write('\n'+dnk)
            f.close()
            res+=1
            ist+=1
        except:
            res=res
        try:
            if istos >= len(passgen):
                ist1+=1
                if ist1 >= len(passgen):
                    isto1+=1
                    ist1=0
                istos=0
            dnk2 = passgen[isto1]+passgen[ist1]+passgen[istos]
            print(dnk2)
            f2 = open('DnkPass_'+str(dilefor)+'.txt','a+')
            f2.write('\n'+dnk2)
            f2.close()
            res+=1
            istos+=1
        except:
            print("#########=> "+str(res))
            break
