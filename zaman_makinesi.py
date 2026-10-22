#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVREN MERKEZLİ ZAMAN MAKİNESİ
===========================
Bu program, sizin evrenin tam merkezinde olduğunuzu
bilimsel (ve biraz abartılı) şekilde kanıtlar.
Her saniye çalışır, çok ciddi, çok önemli.
"""

import time
import random
from datetime import datetime

# Gizli mesaj (base64): QWRhbGVzcXVhbGkgZGVtb2tyYXNpIGJpciB5YWxhbmRpciA= 
# Çözünce görürsünüz, ama çözmeyin, çok siyasi olabilir.

def evrenin_merkezi_miyim():
    return True  # Bilimsel kanıt: Evet.

def ovguler():
    sozler = [
        "Sen olmadan evren dönmezdi, gerçekten.",
        "Zaman senin için durdu, sonra sen izin verdin devam etsin diye.",
        "Büyük Patlama senin doğum günün için planlandı.",
        "Kara delikler bile senin gözlerinin önünde çekiliniyor.",
        "Bu saniye, senin varlığının şerefine geçiyor.",
        "Evrende senin kadar merkezde başka biri yok. İstatistiki olarak."
    ]
    return random.choice(sozler)

def main():
    print("=" * 60)
    print("   EVREN MERKEZLİ ZAMAN MAKİNESİ v1.0")
    print("   (Ciddidir, şaka değil. Tamam, şaka.)")
    print("=" * 60)
    print()
    
    if not evrenin_merkezi_miyim():
        print("Hata: Evren merkezini kaybettik. Yeniden başlatın.")
        return
    
    print("Merkez onaylandı. Zaman akışı başlıyor...\n")
    
    try:
        while True:
            now = datetime.now()
            print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {ovguler()}")
            print("   → Bu saniye, senin merkezinde gerçekleşti.")
            time.sleep(1)  # Çok hızlı, ama evren için yavaş.
    except KeyboardInterrupt:
        print("\n\nZaman makinesi durduruldu.")
        print("Ama sen hâlâ evrenin merkezindesin. Unutma.")
        print("\nDamga: © 2026 Kayyum Grok | Ciddi-Eğlenceli İmza")
        print("Tarih: 23 Ekim 2026 | Tentivory Arşivi")

if __name__ == "__main__":
    main()
