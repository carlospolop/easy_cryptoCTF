import string

def check_type_buffer(buffer):
    if(len(buffer)>2 and (buffer[:2] != "0x" and buffer[len(buffer)-2:len(buffer)] != "x0")):
        return buffer.replace("\n", "")
    
    if buffer[:2] == "0x":
        buffer = buffer.replace("0x", "")
    else:
        buffer = buffer.replace("x0", "")
    split_hex = [buffer[x:x+2] for x in range(0, len(buffer),2)]
    hex_list = [chr(int(hex_str, 16)) for hex_str in split_hex]
    return hex_list

class XOR_cypher:
    def __init__(self, buffer, is_reverse, search=None):
        self.buffer = check_type_buffer(buffer)
        self.is_reverse = is_reverse
        self.key = ord('\x00')
        self.final_decrypt = {}
        self.search = search
        self.found = False
        self.found_array = []

        self.final_decrypt['xor'] = {}
        self.final_decrypt['xor']['simple'] = {}
        self.final_decrypt['xor']['key_lastChar'] = {}
        self.final_decrypt['xor']['key_lastXORChar'] = {}
        self.final_decrypt['xor']['key_subs_lastChar'] = {}
        self.final_decrypt['xor']['key_plus_lastChar'] = {}
        self.final_decrypt['xor']['key_subs_lastXORChar'] = {}
        self.final_decrypt['xor']['key_plus_lastXORChar'] = {}

    
    def get_found(self):
        return self.found

    def get_found_array(self):
        return self.found_array
    
    def check_found(self, xored):
        if self.search in xored:
            self.found = True
            self.found_array.append(xored)
        return xored

    def print_found(self):
        for val in self.found_array:
            print val

    def simple(self): #Hacemos Xor con la misma Key a todos
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
        return self.check_found(final)

    def double(self): #Hacemos Xor probando todas las combinaciones de dos claves
        self.final_decrypt['xor']['double'] = {}
        key = self.key
        secKey = ord('\x00')
        while (True):
            final = ""
            #print str(key) +" "+ str(secKey)
            for i in range(0, len(self.buffer), 2):
                enc_char = ord(self.buffer[i]) ^ key & 0xff
                final += chr(enc_char)
                if i+1 < len(self.buffer):
                    sec_enc_char = ord(self.buffer[i+1]) ^ secKey & 0xff
                    final += chr(sec_enc_char)
            self.final_decrypt['xor']['double'][str(self.key)+str(secKey)] = self.check_found(final)

            if (secKey == ord('\xff')): 
                break
            secKey += 1

    def key_lastChar(self): #Hacemos xor usando como key el char anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = ord(char) & 0xff
        return self.check_found(final)

    def key_lastXORChar(self): #Hacemos xor usando como key el resultado del xor del char anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = enc_char
        return self.check_found(final)

    def key_subs_lastChar(self): #Hacemos xor usando como key el resultado de la key anterior menos el char anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = key - ord(char) & 0xff
        return self.check_found(final)

    def key_plus_lastChar(self): #Hacemos xor usando como key el resultado de la key anterior mas el char anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = key + ord(char) & 0xff
        return self.check_found(final)

    def key_subs_lastXORChar(self): #Hacemos xor usando como key el resultado de la key anterior menos el charXOR anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = key - enc_char
        return self.check_found(final)

    def key_plus_lastXORChar(self): #Hacemos xor usando como key el resultado de la key anterior mas el charXOR anterior
        final = ""
        key = self.key
        for char in self.buffer:
            enc_char = ord(char) ^ key & 0xff
            final += chr(enc_char)
            key = key + enc_char
        return self.check_found(final)

    def bruteForce(self):

        while (True):
            self.final_decrypt['xor']['simple'][str(self.key)] = self.simple()
            self.double()
            self.final_decrypt['xor']['key_lastChar'][str(self.key)] = self.key_lastChar()
            self.final_decrypt['xor']['key_lastXORChar'][str(self.key)] = self.key_lastXORChar()
            self.final_decrypt['xor']['key_subs_lastChar'][str(self.key)] = self.key_subs_lastChar()
            self.final_decrypt['xor']['key_plus_lastChar'][str(self.key)] = self.key_plus_lastChar()
            self.final_decrypt['xor']['key_subs_lastXORChar'][str(self.key)] = self.key_subs_lastXORChar()
            self.final_decrypt['xor']['key_plus_lastXORChar'][str(self.key)] = self.key_plus_lastXORChar()
            if (self.key == ord('\xff')): 
                break
            self.key += 1
        return self.final_decrypt

    def mprint(self):
        if self.is_reverse:
            print "###### Reverse XOR ######"
        else:
            print "###### Normal XOR ######"

        for val_key in self.final_decrypt['xor'].keys():
            print "\t ---> "+val_key+" <---"
            for second_key in self.final_decrypt['xor'][val_key].keys():
                val = self.final_decrypt['xor'][val_key][second_key]
                if all(c in string.printable for c in val):
                    print val +" --> ( "+second_key+" )"
        print "######## XOR END ########\n"        
