
# Brute-Ins

`Brute-Ins`, Instagram hesaplarına brute force saldırısı gerçekleştirebilmek amacıyla yazılmış bir Python tabanlı araçtır. Bu araç, eğitim ve etik hacking amaçlı kullanılmalıdır. Gerçek hesaplara yönelik izinsiz giriş yapmak yasa dışıdır ve etik olmayan bir davranış olarak kabul edilir. Lütfen bu aracı yalnızca güvenli test ortamlarında ve izinli hesaplar üzerinde kullanın.

---

## Özellikler

- Instagram login sayfasına brute force saldırısı yapmak için şifre denemeleri yapar.
- Proxy kullanarak IP gizliliği sağlar.
- Şifreleri bir dosyadan okuyarak otomatik olarak dener.
- Başarılı şifreyi bulduğunda kullanıcı adı ve şifreyi bir dosyaya kaydeder.
- Başarısız şifreler için geri bildirim yapar.

---

## Gereksinimler

Bu proje aşağıdaki Python kütüphanelerine ihtiyaç duyar:

- selenium
- requests
- threading

Projede kullanılan `requirements.txt` dosyasındaki bağımlılıkları yüklemek için şu komutları kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

---

## Kullanım

### Başlangıç

Projeyi çalıştırmadan önce, gerekli bağımlılıkları yüklemek için aşağıdaki adımları takip edin:

1. **Bağımlılıkları yükleyin:**
   
   ```bash
   pip install -r requirements.txt
   ```

2. **Başlangıç dosyasını çalıştırın:**

   `start.py` dosyasını çalıştırarak işlemi başlatabilirsiniz. Şifre denemelerinin yapılacağı Instagram kullanıcı adını ve şifre dosyasını belirlemeniz gerekecek.

   ```bash
   python start.py
   ```

   Program sizi aşağıdaki adımlarla yönlendirecektir:

   - Proxy kullanmak isteyip istemediğinizi belirleyeceksiniz.
   - Kullanıcı adınızı ve şifre dosya yolunuzu gireceksiniz.
   - Ardından şifreler denenmeye başlanacaktır.

   Şifre denemeleri sırasında başarılı bir şifre bulunduğunda, kullanıcı adı ve şifreyi içeren bir dosya oluşturulacaktır.

---

## Dosya Yapısı

- **`start.py`**: Programın çalıştırılabilir dosyasıdır. Kullanıcıdan girdi alır ve brute force işlemi başlatır.
- **`functoin.py`**: Instagram'a giriş yapmak için gerekli işlemleri gerçekleştiren fonksiyonları içerir.
- **`requirements.txt`**: Gerekli Python kütüphanelerini içeren dosya.
- **`proxies_check.py`**: Proxy listesinin geçerliliğini kontrol eden yardımcı script.

---

## Örnek Kullanım

```bash
python start.py
```

Komutunu çalıştırdığınızda aşağıdaki gibi bir çıktı alırsınız:

```
proxy kullanmak ister misiniz(kendi proxy listeniz varsa tavsiye edilen kullanılmasıdır)(y/n): n
Kullanıcı adınızı giriniz: sadsa312999
Şifre dosya yolunu giriniz: abc.txt
Şifreler deneniyor, lütfen bekleyin...
Kullanılan Proxy: Proxy kullanılmıyor
Geçersiz şifre: password123456
Geçersiz şifre: abcd1234560
Başarılı giriş ile şifre: password12345
```

Eğer başarılı bir şifre bulunursa, bir dosya oluşturulur ve şu şekilde içerik eklenir:

```
Kullanıcı adı: örnek
Şifre: örnek12345
```

---

## Etik Uyarı

Bu araç yalnızca **eğitim amaçlı** kullanılmalıdır. Gerçek hesaplara veya başkalarına ait sistemlere yönelik herhangi bir izinsiz erişim girişimi yasadışıdır ve etik dışıdır. Lütfen bu aracı yalnızca **izinli hesaplar** ve **test ortamlarında** kullanın. Aksi takdirde yasal sorumluluk doğurabilir.

---

## Lisans

Bu proje, [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

### `requirements.txt`

```txt
selenium
requests
threading
```
