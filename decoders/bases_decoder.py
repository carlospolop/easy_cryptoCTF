import base64
import string

class Bases_BF:
    def __init__(self, buffer, is_reverse, search=None):
        self.buffer = buffer.replace("\n", "")
        self.is_reverse = is_reverse
        self.std_alphabet64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        self.std_alphabet64_url = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
        self.std_alphabet32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
        self.std_alphabet85 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-:+=^!/*?&<>()[]{}@%$#'
        self.bool_base64 = True
        self.bool_base32 = True
        self.bool_base85 = True
        self.final_decrypt = {}
        self.search = search
        self.found = False
        self.found_array = []
        self.to_print = []
        self.usefull_urls = ["https://www.dcode.fr/ascii-85-encoding"]

        self.final_decrypt['base'] = {}
        self.final_decrypt['base']['64'] = {}
        self.final_decrypt['base']['32'] = {}

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

    def b64_simple(self, custom_alphabet):
        pad = 4 - (len(self.buffer) % 4)
        #ENCODE_TRANS = string.maketrans(STANDARD_ALPHABET, CUSTOM_ALPHABET)
        buffer = self.buffer
        if pad != 4:
            buffer = self.buffer + "="*pad
        decode_trans = string.maketrans(custom_alphabet, self.std_alphabet64)
        return self.check_found(base64.b64decode(buffer.translate(decode_trans)))
    
    def b32_simple(self, custom_alphabet):
        pad = 8 - (len(self.buffer) % 8)
        buffer = self.buffer
        if pad != 8:
            buffer = self.buffer + "="*pad
        decode_trans = string.maketrans(custom_alphabet, self.std_alphabet32)
        return self.check_found(base64.b32decode(buffer.translate(decode_trans)))


    def bruteForce(self):
        if (self.buffer[0] == "="):
            self.bool_base64 = False
            self.to_print.append("No base 64, inverse padding")
            self.bool_base32 = False
            self.to_print.append( "No base 32, inverse padding")

        for char in self.buffer:
            if(not char in self.std_alphabet85):
                self.bool_base85 = False
                self.to_print.append("Bad char: "+char+" No base 85")
                self.bool_base64 = False
                self.to_print.append("Bad char: "+char+" No base 64")
                self.bool_base32 = False
                self.to_print.append("Bad char: "+char+" No base 32")
                break
        
        if self.bool_base85:
            if self.buffer[0] == "<":
                self.to_print.append("Could be Base85 of Adobe")
            else:
                self.to_print.append("Could be Base85")

        if self.bool_base64:
            for char in self.buffer:
                if(not char in self.std_alphabet64 and char != "="):
                    self.bool_base64 = False
                    self.to_print.append("Bad char: "+char+" No base 64")
                    self.bool_base32 = False
                    self.to_print.append("Bad char: "+char+" No base 32")
                    break
        
        if self.bool_base64:
            self.to_print.append("Could be Base64")

        if self.bool_base32:
            for char in self.buffer:
                if(not char in self.std_alphabet32 and char != "="):
                    self.bool_base32 = False
                    self.to_print.append("Bad char: "+char+" No base 32")
                    break

        if self.bool_base64:
            self.to_print.append("Could be Base32")

        #Bruteforce
        if self.bool_base64:
            pad = 4 - (len(self.buffer) % 4)
            if pad == 4 or pad < 3:       
                for i in range (0,62):
                    custom_alphabet = self.std_alphabet64[len(self.std_alphabet64)-(i+2):62] + self.std_alphabet64[:len(self.std_alphabet64)-(i+2)] + self.std_alphabet64[62:]
                    self.final_decrypt['base']['64'][custom_alphabet] = self.b64_simple(custom_alphabet)
                for i in range (0,62):
                    custom_alphabet = self.std_alphabet64_url[len(self.std_alphabet64_url)-(i+2):62] + self.std_alphabet64_url[:len(self.std_alphabet64_url)-(i+2)] + self.std_alphabet64_url[62:]
                    self.final_decrypt['base']['64'][custom_alphabet] = self.b64_simple(custom_alphabet)
        
        if self.bool_base32:
            pad = 8 - (len(self.buffer) % 8)
            if pad == 8 or pad < 3:
                for i in range (0,32):
                    custom_alphabet = self.std_alphabet32[len(self.std_alphabet32)-i:] + self.std_alphabet32[:len(self.std_alphabet32)-i]
                    self.final_decrypt['base']['32'][custom_alphabet] = self.b32_simple(custom_alphabet)
        
        return self.final_decrypt

    def mprint(self):
        if self.is_reverse:
            print "###### Reverse Bases ######"
        else:
            print "###### Normal Bases ######"
        
        for val in self.to_print:
            print val
        
        print "Usefull URLS:"
        for val in self.usefull_urls:
            print val

        if self.final_decrypt['base']['64'] != {}:
            print "---> Base64 <---"
            for key in self.final_decrypt['base']['64'].keys():
                val = self.final_decrypt['base']['64'][key]
                if all(c in string.printable for c in val):
                    print val +"  -->  ( "+key+" )"

        if self.final_decrypt['base']['32'] != {}:
            print "---> Base32 <---"
            for val in self.final_decrypt['base']['32'].keys():
                val = self.final_decrypt['base']['64'][key]
                if all(c in string.printable for c in val):
                    print val +"  -->  ( "+key+" )"

        print "###### Bases END ######"
        print
