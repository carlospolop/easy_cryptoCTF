import string

class Caesar_BF:
    def __init__(self, buffer, search=None):
        self.buffer = buffer
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

    def caesar_simple(self, alphabet, shift):
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = string.maketrans(alphabet, shifted_alphabet)
        return self.check_found(self.buffer.translate(table))

    def caesar_loop(self, alphabet):
        for i in range(0, len(alphabet)):
            self.final_decrypt['caesar'][alphabet+str(i)] = self.caesar_simple(alphabet, i)

    def bruteForce(self):
        self.final_decrypt['caesar'] = {}
        alphabet = string.ascii_lowercase
        self.caesar_loop(alphabet)
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        self.caesar_loop(alphabet)
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.caesar_loop(alphabet)

        return self.final_decrypt

    def mprint(self):
        print "###### Caesar ######"
        for val in self.final_decrypt['caesar'].values():
            print val
        print "###### Caesar END ######"
