from services import AppService
import re
from fastapi import status

async def cleanse_text(text):
      
    # Memisahkan kata-kata setelah hashtag yang tersambung
    pattern = r"#([A-Z][a-z0-9]+)([A-Z][a-z0-9]+)"
    text = re.sub(pattern, r"# \1 \2", text)

    # Mengubah semua huruf menjadi huruf kecil
    text = text.lower()

    # Menghapus spasi di awal dan akhir text
    text = text.strip()

    # Menghapus kata 'user', 'rt', 'amp' dan 'x..'
    text = re.sub(r'\buser\b|\bRT\b|\bamp\b|(\bx[\da-f]{2})', ' ', text, flags=re.IGNORECASE)

    # Menghapus kata '\n'
    text = re.sub(r'\\n', ' ', text, flags=re.IGNORECASE)

    # Menghapus karakter non-alfanumerik
    text = re.sub(r'\W+', ' ', text)

    # Menghapus karakter berulang
    text = re.sub(r'(.)\1+', r'\1', text)

    # Menghapus karakter 'ø', 'ù', 'º', 'ð', dan lainnya
    text = re.sub(r'[øùºðµ¹ª³]', '', text, flags=re.IGNORECASE)
    text = re.sub(r'â', 'a', text, flags=re.IGNORECASE)

    # Menghapus spasi berlebih dengan mengganti beberapa spasi menjadi satu spasi
    text = re.sub(r'\s+', ' ', text).strip()

    # Menghapus seluruh kalimat yang hanya berisi spasi
    text = re.sub(r'^\s+$', '', text)
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