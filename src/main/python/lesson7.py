
class CesarCypher(object):

    def __init__(self, offset=3):
        self.offset = offset

    def encode(self, text):
        return ''.join([unichr(ord(c) + self.offset) for c in text])

    def decode(self, data):
        return ''.join([unichr(ord(c) - self.offset) for c in data])

