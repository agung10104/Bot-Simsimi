import json

a = open('data.json')
data = json.load(a)

# menambahakan kepintaran pada Bot
print('''
Silahkan pilih opsi: 
1. Melatih Bot 
2. Berbicara dengat Bot
''')

while True:
    input_awal = input('Masukkan kode: ')
    if input_awal == '1':
        while True:
            x = input('Kamu\t: ')
            if x == 'keluar':
                break
            else:
                y = input('Bot\t: ')
                data[x] = y
                b = open('data.json', 'w')
                json.dump(data,b)
                b.close()
    
    
    elif input_awal == '2':
        while True:
            x = input('Kamu\t: ')
            if x == 'keluar':
                break
            if x in data:
                print(f'Bot\t: {data[x]}\n')
            else: 
                print('Bot\t: Itu kata baru')
            

    else:
        pass

