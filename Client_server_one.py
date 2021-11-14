import subprocess
import chardet
import locale

#Exercise_1

a = 'сокет'
b = 'разработка'
c = 'декоратор'

a_in_bites = a.encode('utf-8')
print(a_in_bites)
in_bites_a= b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
print(in_bites_a.decode('utf-8'))


b_in_bites = b.encode('utf-8')
print(b_in_bites)
in_bites_b=b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
print(b_in_bites.decode('utf-8'))

c_in_bites=c.encode('utf-8')
print(c_in_bites)
in_bites_c=b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
print(in_bites_c.decode('utf-8'))

a_bites = str.encode(a,encoding = 'utf-8')
print(a_bites)
print(a_bites.decode(encoding='utf-8'))

#Exercise_2

elements = [b'class', b'function', b'method']

for line in elements:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))

# Exercise_3. Определить, какие из слов «attribute»,
# «класс», «функция», «type» невозможно записать в байтовом типе.

#el_1 = b'«attribute»'
#el_2=b'класс'
#el_3=b'функция'
#el_4=b'type'

#elements_2 = [b'«attribute»', b'класс', b'функция', b'type']
#print(elements_2)

#Ответ: SyntaxError: bytes can only contain ASCII literal characters.

#Execrise_4.


elements_3 = ["разработка", "администрирование", "protocol", "standard"]

for el in elements_3:
    print(el)
    a = el.encode(encoding='UTF-8')
    print(a,type(a))
    bit = bytes.decode(a, encoding='utf-8')
    print(bit,type(bit))
    print('-'*15)

# Ответ: SyntaxError: bytes can only contain ASCII literal characters.


ARGS=['ping','yandex.ru']
YA_PING = subprocess.Popen(ARGS,stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    print(type(line))
    result=chardet.detect(line)
    line=line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

ARGS=['ping','youtube.com']
YA_PING = subprocess.Popen(ARGS,stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    print(type(line))
    result=chardet.detect(line)
    line=line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))



F_N = open('test_file.txt','w',encoding = 'utf-8')
F_N.write('сетевое программирование сокет декоратор')
F_N.close()
print(type(F_N))


with open('test.txt',encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end = '')
    print()

file_coding = locale.getpreferredencoding()


