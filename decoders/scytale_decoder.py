import string

class Scytale_BF:
    def __init__(self, buffer, is_reverse, search=None):
        self.buffer = buffer.replace("\n", "")
        self.is_reverse = is_reverse
        self.final_decrypt = {}
        self.search = search
        self.found = False
        self.found_array = []
        self.usefull_urls = ["https://www.dcode.fr/scytale-cipher"]

        self.final_decrypt['scytale'] = {}
    
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

    
    def simple_scytale(self,num_elem):
        result = ""
        split_list = [self.buffer[x:x+num_elem] for x in range(0, len(self.buffer),num_elem)]
        for cont_i in range(0,num_elem):
            for cont in range(0,len(split_list)):
                result += split_list[cont][cont_i]
        
        self.final_decrypt['scytale'][str(num_elem)] = self.check_found(result)

    
    def bruteForce(self):
        for i in range(2,len(self.buffer)/2):
            if len(self.buffer) % i == 0 and len(self.buffer) != i:
                self.simple_scytale(i)

        return self.final_decrypt


    def mprint(self):
        if self.is_reverse:
            print "###### Reverse Scytale ######"
        else:
            print "###### Normal Scytale ######"

        print "Usefull URLS:"
        for val in self.usefull_urls:
            print val
    
        for key in self.final_decrypt['scytale'].keys():
            val = self.final_decrypt['scytale'][key]
            print val +" --> ( "+key+" )"
        print "###### Scytale END ######"
        print