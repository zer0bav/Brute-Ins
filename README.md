   
   # Brute-Ins
   
   `Brute-Ins`, is a Python-based tool designed to perform brute force attacks on Instagram accounts. This tool is intended for educational and ethical hacking purposes only. Unauthorized access to real accounts is illegal and considered unethical. Please use this tool only in secure testing environments and with authorized accounts.
   
   ---
   
   ## Features
   
   - Attempts brute force attacks on the Instagram login page.

   - Uses proxies to ensure IP privacy.
   - Automatically tries passwords from a file.
   - Saves the username and successful password to a file.
   - Provides feedback for failed password attempts.
   
   ---
   
   ## Requirements
   
   This project requires the following Python libraries:
   
   - selenium
   - requests
   - threading
   
  To install the dependencies listed in the `requirements.txt` file, use the following commands:
   
   ```bash
   pip install -r requirements.txt
   ```
   
   ---
   
   ## Usage
   
   ### Getting Started
   
   Follow these steps to run the project and install the necessary dependencies:
   
   1. **Install Dependencies:**
      
      ```bash
      pip install -r requirements.txt
      ```
   
   2. **Run the Main Script:**
   
      Execute the  `start.py ` file to begin the process. You will need to specify the Instagram username and password file to be used for the brute force attempts.
   
      ```bash
      python start.py
      ```
   
      The program will guide you through the following steps:


   
      - Specify whether you want to use a proxy.
      - Enter the username and the file path for the password list.
      - Password attempts will begin.
   
      If a successful password is found, a file containing the username and password will be created.
   
   ---
   
   ## File Structure

   
   - **`start.py`**: The executable file of the program. It collects input from the user and starts the brute force process.
   - **`functoin.py`**: Contains functions for performing Instagram login operations.
   - **`requirements.txt`**: A file listing the required Python libraries.
   - **`proxies_check.py`**: A helper script that validates the proxy list.
   
   ---
   
   ## Example Usage

   
   
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
   
   If a successful password is found, a file will be created with the following content:
   
   ```
   Kullanıcı adı: örnek
   Şifre: örnek12345
   ```
   
   ---
   
   ## Ethical Warning
   
 This tool is for educational purposes only. Any unauthorized access attempts to real accounts or systems that belong to others are illegal and unethical. Please use this tool only on authorized accounts and in testing environments. Misuse may lead to legal consequences.


   
   ---
   
   ## Lisans
   
  This project is licensed under the [MIT Lisansı](LICENSE)
   
   ---
   
   ### `requirements.txt`
   
   ```txt
   selenium
   requests
   threading
   ```
