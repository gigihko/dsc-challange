from services import AppService
import re
from fastapi import status

async def cleanse_text(text):
    # Menghapus karakter non-alfanumerik
    text = re.sub(r'\W+', ' ', text)
    
    # Menghapus karakter berulang
    text = re.sub(r'(.)\1+', r'\1\1', text)
    
    # Mengubah semua huruf menjadi huruf kecil
    text = text.lower()
    
    # Menghapus spasi di awal dan akhir teks
    text = text.strip()
    
    return text
    

async def cleansing(sentence):
            try:
                data = await cleanse_text(text=sentence)
                content = {
                    "ok": True,
                    "code": status.HTTP_200_OK,
                    "data": data,
                    "message": "Success",
                }
                return content
            except Exception as e:
                return e