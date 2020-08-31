#IMPORT#
import requests
import json
from os import path
import datetime
#DATALAYER#
#############################################################
today = datetime.datetime.now()
#############################################################
ymd = (str(today).split(' ') [0])
#############################################################
print(ymd)
#############################################################
file_name = f'./rates--{ymd}.json'
#############################################################
key = '6b6c81aa65f79d03267586e8fa720d51'
#############################################################
endpoint = 'http://data.fixer.io/api/latest' + '?access_key=' + key
#############################################################
#LOGIC LAYER#
#############################################################
def close():
    pass
#############################################################
#get data#
if path.exists(file_name):
    file = open(file_name, 'r')
    data = json.loads(file.read())
else:
    response = requests.get(endpoint)
    data = json.loads(response.text)
    file = open(file_name, 'w')
    file.write(response.text)
    file.close()
#############################################################
if data['success'] is False:
    print(data)
    print("CANNOT ACCES DATA")
else:
    #print(data)
    eur = 1
    mdl = data['rates']['MDL']
    usd = data['rates']['USD']
    rub = data['rates']['RUB']
    #print( eur , mdl , usd , rub )
    #print(convert(1_000_000 ,))
#############################################################
def menu():
    print('1. Transform from eur')
    print('2. Transform from usd')
    print('3. Transform from rub')
    print('4. Transform from mdl')
    print('0.Close the panel')
    decision_1 = input('Option : ')
    while decision_1 != '0':
        if '1' in decision_1:
            print('1. Transform to usd')
            print('2. Transform to rub')
            print('3. Transform to mdl')
            decision_2 = input('Second option : ')
            money_value = input('Value ?> ')
            if '1' in decision_2:
                # usd = 1.19065
                money_usd = float(money_value) * usd
                print(money_usd)
            if '2' in decision_2:
                # rub = 88.209546
                money_rub = float(money_value) *  rub
                print(money_rub)
            if '3' in decision_2:
                # mdl = 19.843749
                money_mdl = float(money_value) *  mdl
                print(money_mdl)

            print('1. Transform from eur')
            print('2. Transform from usd')
            print('3. Transform from rub')
            print('4. Transform from mdl')
            print('0.Close the panel')
            decision_1 = input('Option : ')
            #############################################################
        if '2' in decision_1:
            print('1. Transform to eur')
            print('2. Transform to rub')
            print('3. Transform to mdl')
            decision_2 = input('Second option : ')
            money_value = input('Value ?> ')
            if '1' in decision_2:
                money_eur = (float(eur) / usd) * float(money_value)
                print(money_eur)
            if '2' in decision_2:
                money_eur = (float(eur) / usd) * float(money_value)
                money_rub = float(money_eur) *  rub
                print(money_rub)
            if '3' in decision_2:
                money_eur = (float(eur) / usd) * float(money_value)
                money_mdl = float(money_eur) *  mdl
                print(money_mdl)
            print('1. Transform from eur')
            print('2. Transform from usd')
            print('3. Transform from rub')
            print('4. Transform from mdl')
            print('0.Close the panel')
            decision_1 = input('Option : ')
        if '3' in decision_1:
            print('1. Transform to eur')
            print('2. Transform to usd')
            print('3. Transform to mdl')
            decision_2 = input('Second option : ')
            money_value = input('Value ?> ')
            if '1' in decision_2:
                money_eur1 = (float(eur) * rub) * float(money_value)
                money_eur = float(money_eur1) * float(1)
                print(money_eur)
            if '2' in decision_2:
                money_eur1 = (float(eur) * rub) * float(money_value)
                money_rub = float(money_eur1) * rub
                print(money_rub)
            if '3' in decision_2:
                money_eur1 = (float(eur) * rub) * float(money_value)
                money_mdl = float(money_eur1) * mdl
                print(money_mdl)
            print('1. Transform from eur')
            print('2. Transform from usd')
            print('3. Transform from rub')
            print('4. Transform from mdl')
            print('0.Close the panel')
            decision_1 = input('Option : ')
        if '4' in decision_1:
            print('1. Transform to eur')
            print('2. Transform to usd')
            print('3. Transform to rub')
            decision_2 = input('Second option: ')
            money_value = input('Value ?> ')
            if '1' in decision_2:
                money_eur1 = (float(eur) / mdl) * float(money_value)
                money_eur = float(money_eur1) * float(1)
                print(money_eur)
            if '2' in decision_2:
                money_eur1 = (float(eur) / mdl) * float(money_value)
                money_usd = float(money_eur1) * usd
                print(money_usd)
            if '3' in decision_2:
                money_eur1 = (float(eur) / mdl) * float(money_value)
                money_rub = float(money_eur1) * rub
                print(money_rub)
            print('1. Transform from eur')
            print('2. Transform from usd')
            print('3. Transform from rub')
            print('4. Transform from mdl')
            print('0.Close the panel')
            decision_1 = input('Option : ')

menu()