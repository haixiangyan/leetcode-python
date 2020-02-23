from random import randint

class Codec:
    def __init__(self):
        self.store = {}
        self.store2 = {}

    def encode(self, longUrl: str) -> str:
        self.store[longUrl] = str(randint(1, 100))
        self.store2['https://tinyurl.com/' + self.store[longUrl]] = longUrl
        return 'https://tinyurl.com/' + self.store[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.store2[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))