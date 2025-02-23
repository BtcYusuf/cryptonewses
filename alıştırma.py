# -*- coding: utf-8 -*-

import requests  # requests modülünü içe aktarıyoruz

API_KEY = "90fcaa9779dd4b21bd6ba27560428330"

def haber_cek(kripto_adi):
    """NewsAPI'den belirli bir kripto para ile ilgili haberleri çeker"""
    url = f"https://newsapi.org/v2/everything?q={kripto_adi}&apiKey={API_KEY}&language=tr"

    response = requests.get(url)
    data = response.json()

    if "articles" in data:
        haberler = data["articles"][:5]  # İlk 5 haberi al
        return haberler
    return None

def main():
    kripto_adi = input("Hangi Kripto Para Hakkında Haber Almak İstiyorsunuz? (örn: Bitcoin, Ethereum) ").strip()

    haberler = haber_cek(kripto_adi)

    if haberler:
        print("\n📢 Kripto Haberleri:\n")
        for i, haber in enumerate(haberler, start=1):
            print(f"{i}. {haber.get('title', 'Başlık Yok')}")
            print(f"Kaynak: {haber.get('source', {}).get('name', 'Kaynak Yok')}")
            print(f"Link: {haber.get('url', 'Link Yok')}\n")
    
    else:
        print("❌ Kripto Para Haberleri Bulunamadı!")

if __name__ == "__main__":
    main()
