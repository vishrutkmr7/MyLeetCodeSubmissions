class Encrypter:
    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.hashmap = {}
        for index, value in enumerate(keys):
            self.hashmap[value] = values[index]
        self.dictmap = defaultdict(int)
        for word in dictionary:
            self.dictmap[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        output = ""
        for char in word1:
            if char in self.hashmap:
                output += self.hashmap[char]
            else:
                return ""
        return output

    def decrypt(self, word2: str) -> int:
        return self.dictmap[word2]

        


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
