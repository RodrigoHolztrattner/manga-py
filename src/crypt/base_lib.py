
import base64
import codecs
import gzip
import zlib
from struct import pack, unpack
from binascii import unhexlify

from Crypto.Cipher import AES
from Crypto.Hash import SHA256, MD5
from execjs import compile as js_compile


class BaseLib:

    @staticmethod
    def decode_escape(data):  # pragma: no cover

        if isinstance(data, str):
            data = data.encode()
        try:
            data = codecs.escape_decode(data)
            return data[0]
        except Exception:
            return ''

    @staticmethod
    def encode_hex(data):  # pragma: no cover
        return codecs.decode(data, 'hex')

    @staticmethod
    def to_sha_256(data):  # pragma: no cover
        if isinstance(data, str):
            data = data.encode()
        sha = SHA256.new()
        sha.update(data)
        return sha.digest()

    @staticmethod
    def decrypt_aes(iv, key, data):  # pragma: no cover
        aes = AES.new(key, AES.MODE_CBC, iv)
        return aes.decrypt(data)

    @staticmethod
    def base64decode(data, altchars=None, validate=False):  # pragma: no cover
        return base64.b64decode(data, altchars, validate)

    @staticmethod
    def base64encode(data, altchars=None):  # pragma: no cover
        return base64.b64encode(data, altchars)

    @staticmethod
    def exec_js(source, js):  # pragma: no cover
        return js_compile(source).eval(js)

    @staticmethod
    def gunzip(data):  # pragma: no cover
        return gzip.decompress(data)

    @staticmethod
    def gzip(data, lvl: int = 9):  # pragma: no cover
        return gzip.compress(data, lvl)

    @staticmethod
    def zlib_d(data, **kwargs):  # pragma: no cover
        return zlib.decompress(data, **kwargs)

    @staticmethod
    def zlib_c(data, **kwargs):  # pragma: no cover
        return zlib.compress(data, **kwargs)

    @staticmethod
    def md5(string):  # pragma: no cover
        _ = MD5.new()
        _.update(string.encode())
        return _

    @staticmethod
    def pack(fmt, *args):  # pragma: no cover
        return pack(fmt, *args)

    @staticmethod
    def unpack(fmt, string):  # pragma: no cover
        return unpack(fmt, string)

    @staticmethod
    def str2hex(string):
        hex_str = ''
        if isinstance(string, bytes):
            string = string.decode()
        for char in string:
            int_char = ord(char)
            hex_num = hex(int_char).lstrip("0x")
            hex_str += hex_num
        return hex_str

    @staticmethod
    def hex2str(string):
        clear_str = ''
        if isinstance(string, bytes):
            string = string.decode()
        for counter in range(0, len(string), 2):
            hex_char = string[counter]+string[counter+1]
            clear_str += unhexlify(hex_char)
        return clear_str