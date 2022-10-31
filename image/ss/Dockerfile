FROM python:3.7.5
RUN pip install shadowsocks==2.8.2 \
    -i https://mirrors.aliyun.com/pypi/simple/  \
    --trusted-host mirrors.aliyun.com \
    --no-cache-dir && \
    sed -i 's/EVP_CIPHER_CTX_cleanup/EVP_CIPHER_CTX_reset/g' /usr/local/lib/python3.7/site-packages/shadowsocks/crypto/openssl.py

# ---
EXPOSE 8388:8388 1080:1080
CMD ['/usr/local/bin/ssserver',\
    '-p',\
    '8388',\
    '-k',\
    '1234',\
    '-m',\
    'rc4-md5'\
]

#CMD ['/usr/local/bin/sslocal',
#    '-b',
#    '0.0.0.0',
#    '-s',
#    '127.0.0.1',
#    '-k',
#    '1234',
#    '-m',
#    'rc4-md5'
#]
