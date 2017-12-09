import string

class Caesar_BF:
    def __init__(self, buffer, is_reverse, search=None):
        self.buffer = buffer.replace("\n", "")
        self.is_reverse = is_reverse
        self.final_decrypt = {}
        self.search = search
        self.found = False
        self.found_array = []

        self.final_decrypt['caesar'] = {}


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

    def caesar_loop(self, alphabet): #Recorremos cada posible posicion del alfabeto
        for i in range(0, len(alphabet)):
            self.final_decrypt['caesar'][alphabet+"_shift:"+str(i)] = self.caesar_simple(alphabet, i)

    def bruteForce(self): #Todas las posibles posiciones iniciales de cada alfabeto a probar
        alphabet = string.ascii_lowercase
        self.caesar_loop(alphabet)
        alphabet = string.ascii_uppercase
        self.caesar_loop(alphabet)
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        self.caesar_loop(alphabet)
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.caesar_loop(alphabet)
        alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
        self.caesar_loop(alphabet)

        return self.final_decrypt
        

    def mprint(self):
        if self.is_reverse:
            print "###### Reverse Caesar ######"
        else:
            print "###### Normal Caesar ######"
    
        for key in self.final_decrypt['caesar'].keys():
            val = self.final_decrypt['caesar'][key]
            print val +" --> ( "+key+" )"
        print "###### Caesar END ######\n"
