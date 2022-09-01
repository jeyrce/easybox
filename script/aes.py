# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

encrypt_key = 'clkdczyzsdsywr07'  # 16位加密字符
block_size = 32


def encrypt(key: str, text: str) -> str:
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    secure = aes.encrypt(pad(text.encode('utf-8'), block_size))
    return secure.hex()


def decrypt(key: str, secure: str) -> str:
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    text = unpad(aes.decrypt(bytes.fromhex(secure)), block_size)
    return text.decode('utf-8')


if __name__ == '__main__':
    tests = [
        '18888888888',
        '420325199909083355',
    ]
    for test in tests:
        x = encrypt(encrypt_key, test)
        print(test, '->', x, len(x))
        y = decrypt(encrypt_key, x)
        print(y)
