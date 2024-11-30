import requests
import threading
def prox(proxy_list=None):
    proxy_list = [
        "147.93.128.199:8888",
        "200.174.198.86:8888"
    ]

    for proxy in proxy_list:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        try:
            response = requests.get("https://www.instagram.com", proxies=proxies, timeout=15)
            print(f"Proxy {proxy} çalışıyor! Durum kodu: {response.status_code}")
        except Exception as e:
            print(f"Proxy {proxy} çalışmıyor. Hata: {e}")
