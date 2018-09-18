from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

class CesarCypher(object):

    def __init__(self, offset=3):
        self.offset = offset

    def encode(self, text):
        return ''.join([unichr(ord(c) + self.offset) for c in text])

    def decode(self, data):
        return ''.join([unichr(ord(c) - self.offset) for c in data])



def build_pair(length=4096,exponent=65537):
    new_key = RSA.generate(length,e=exponent)
    return new_key, new_key.publickey()

def export_pair(name, pair,format='PEM'):
    private_key, public_key = pair
    with open('%s.pki.%s' % (name,format),'wb+') as pki_output:
        pki_output.write(private_key.exportKey(format))
    with open('%s.pku.%s' % (name,format),'wb+') as pku_output:
        pku_output.write(public_key.exportKey(format))

    
def encrypt(key, blob):
    cipher = PKCS1_OAEP.new(key)
    result = cipher.encrypt(blob)
    return result

def decrypt(key, blob):
    cipher = PKCS1_OAEP.new(key)
    result = cipher.decrypt(blob)
    return result

if __name__ == '__main__':
    key_pair = build_pair()
    print(key_pair)
    export_pair('test',key_pair)
    pki, pku = key_pair
    print(hashlib.sha256(pku.exportKey()).hexdigest())
    origin = 'ettore'
    pku_encoded = encrypt(pku, origin)
    pki_decoded = decrypt(pki, pku_encoded)
    print(origin,pku_encoded,pki_decoded)


    pki_encoded = encrypt(pki, origin)
    pku_decoded = decrypt(pku, pki_encoded)
    print(origin,pki_encoded,pku_decoded)
