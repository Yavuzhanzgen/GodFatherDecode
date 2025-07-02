from base64 import b64decode
from Crypto.Cipher import AES

def decrypt(ciphertext_b64):
    cipherbytes = b64decode(ciphertext_b64)
    key = b'B9M80O2RAK1VRJNV'
    
    init_vector = cipherbytes[:16]
    messagebytes = cipherbytes[16:]
    
    cipher = AES.new(key, AES.MODE_CBC, init_vector)
    decrypted = cipher.decrypt(messagebytes)
    
    pad_len = decrypted[-1]
    return decrypted[:-pad_len].decode('utf-8')

print("Sifreli Base64 metni girin (cikmak icin 'q' yazin):")

while True:
    s = input("> ")
    if s.lower() == 'q':
        break
    try:
        sonuc = decrypt(s)
        print(f"Cozulen metin: {sonuc}")
        
    except Exception as e:
        print(f"Cozulemedi: {e}")
