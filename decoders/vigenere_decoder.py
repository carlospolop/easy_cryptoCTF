from itertools import cycle


class Vigenere_BF:
    def __init__(self, buffer, key, search=None):
        self.buffer = buffer
        self.key = key
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}'
        self.final_decrypt = {}
        self.search = search
        self.found = False
        self.found_array = []

    def get_found(self):
        return self.found

    def get_found_array(self):
        return self.found_array
    
    def check_found(self, toCheck):
        if self.search in toCheck:
            self.found = True
            self.found_array.append(toCheck)
        return toCheck

    def print_found(self):
        for val in self.found_array:
            print val

    def vigeasy_decrypt(self, alphabet):
        """Encrypt the string and return the ciphertext"""
        cyphertext = self.buffer
        cyphertext = cyphertext[:len(cyphertext)-len(self.key)]
        pairs = zip(cyphertext, cycle(self.key))
        result = ''
        for pair in pairs:
            (x,y)=pair
            total = alphabet.index(x) - alphabet.index(y)
            if total < 0:
                total += len(alphabet)
            result += alphabet[total % len(alphabet)]
        return self.check_found(result)

    def vigeasy_decrypt_loop(self):
        for i in range (0, len(self.alphabet)-3):
            alphabet = self.alphabet[len(self.alphabet)-(i+3):62] + self.alphabet[:len(self.alphabet)-(i+3)] + self.alphabet[62:]
            self.final_decrypt['vigenere'][alphabet] = self.vigeasy_decrypt(alphabet)

    def bruteForce(self):
        try:
            self.final_decrypt['vigenere'] = {}
            self.vigeasy_decrypt_loop()
            return self.final_decrypt
        except:
            pass

    def mprint(self):
        print "###### Vigenere ######"
        for val in self.final_decrypt['vigenere'].values():
            print val
        print "###### Vigenere END ######"