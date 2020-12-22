from caser_cipher import __version__ 
from caser_cipher.caser_cipher import *


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    txt='hello'
    key=5
    actual=encrypt(txt,key)
    assert actual=='mjqqt'

def test_decrypt():
    txt='hello'
    key=5
    actual=decrypt(encrypt(txt,key),key)
    assert actual=='hello'

def test_zxy():
    txt='xyz'
    key=3
    actual=encrypt(txt,key)
    assert actual=='ccc'