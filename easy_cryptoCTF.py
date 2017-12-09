#!/usr/bin/python
import sys, os, getopt
from subprocess import Popen, PIPE

from decoders import XOR_cypher, Bases_BF, Caesar_BF, Scytale_BF #,Vigenere_BF

def main(argv):
    hlp = " -c <StringEncrypted> -f <inputfileEncrypted> -s <String_to_search> -x -b -e -t -f -n"
    try:
        opts, args = getopt.getopt(argv,"hc:s:f:xbetdn",["console=","search=","ifile=","xor","base","caesar","scytale","featherduster","noprint"])
    except getopt.GetoptError:
        print hlp
        sys.exit(2)

    general_urls = ["Cyberchef: https://gchq.github.io/CyberChef/", "Muchos decoders: https://www.dcode.fr/tools-list", "BrainFuck:  http://esoteric.sange.fi/brainfuck/impl/interp/i.html", "Vigenere: https://www.guballa.de/vigenere-solver"]
    toDecrypt, search, outputfile = "", "", ""
    is_input_file, try_all, try_xor, try_base, try_caesar, try_scytale, print_each = False, True, False, False, False, False, True

    for opt, arg in opts:
        if opt == '-h':
            print hlp
            sys.exit()

        elif opt in ("-c", "--command"):
            toDecrypt = arg

        elif opt in ("-f", "--ifile"):
            inputfile = arg
            if (os.path.isfile(inputfile)):
                is_input_file = True
                with open(inputfile, 'r') as f:
                    toDecrypt = f.read()
            else:
                print "Not a file: "+inputfile
                sys.exit(-1)

        elif opt in ("-x","--xor"):
            try_all = False
            try_xor = True

        elif opt in ("-b","--base"):
            try_all = False
            try_base = True

        elif opt in ("-e","--caesar"):
            try_all = False
            try_caesar = True
        
        elif opt in ("-t","--scytale"):
            try_all = False
            try_scytale = True

        elif opt in ("-d","--featherduster"):
            try_all = False
            try_featherduster = True

        elif opt in ("-s", "--search"):
            search = arg
        
        elif opt in ("-n", "--noprint"):
            print_each = False


    if toDecrypt == "":
        print hlp
        sys.exit(-1)

    toDecrypt_i = toDecrypt[::-1]

    # XOR MODULE
    xorbf = XOR_cypher(toDecrypt, False, search)
    xorbf_i = XOR_cypher(toDecrypt_i, True, search)
    if try_all or try_xor:
        final_decrypt_xor = xorbf.bruteForce()
        final_decrypt_xor_i = xorbf_i.bruteForce()
            

    # BASE MODULE
    bbf = Bases_BF(toDecrypt, False, search)
    bbf_i = Bases_BF(toDecrypt_i, True, search)
    if try_all or try_base:
        final_decrypt_bases = bbf.bruteForce()
        final_decrypt_bases_i = bbf_i.bruteForce()
            

    # Caesar MODULE
    cbf = Caesar_BF(toDecrypt, False, search)
    cbf_i = Caesar_BF(toDecrypt_i, True, search)
    if try_all or try_caesar:
        final_decrypt_caesar = cbf.bruteForce()            
        final_decrypt_caesar_i = cbf_i.bruteForce()
            

    # Scytale MODULE
    sbf = Scytale_BF(toDecrypt, False, search)
    sbf_i = Scytale_BF(toDecrypt_i, True, search)
    if try_all or try_scytale:
        final_decrypt_scytale = sbf.bruteForce()            
        final_decrypt_scytale_i = sbf_i.bruteForce()

    # Featherduster MODULE
    f_stdout,f_stderr = "", ""
    if (try_all or try_featherduster) and is_input_file:
        pw = Popen("echo autopwn | featherduster "+ inputfile, stdout=PIPE, stderr=PIPE, shell=True)
        f_stdout,f_stderr = pw.communicate()


    # Vigenere MODULE
    # Falta anadirle is_reverse
    #vbf = Vigenere_BF(toDecrypt, "password", search)
    #final_decrypt_vigenere = vbf.bruteForce()
    #vbf.mprint()

    #vbf_i = Vigenere_BF(toDecrypt_i, "password", search)
    #final_decrypt_vigenere_i = vbf_i.bruteForce()
    #vbf_i.mprint()



    ######## Print output #########
    print "###### General Usefull URLs ######"
    for url in general_urls:
        print url
    print "###### End URLs ######"

    #Search MODULE
    if search != "":
        print "###### Search ######"
        if xorbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN NORMAL XOR"
            xorbf.print_found()
        if xorbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN XOR USING REVERSE STRING"
            xorbf_i.print_found()

        if bbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN NORMAL BASES"
            bbf.print_found()
        if bbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN BASES USING REVERSE STRING"
            bbf_i.print_found()

        if cbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN NORMAL CAESAR"
            cbf.print_found()
        if cbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN CAESAR USING REVERSE STRING"
            cbf_i.print_found()

        if sbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN NORMAL SCYTALE"
            sbf_i.print_found()
        if sbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN SCYTALE USING REVERSE STRING"
            sbf_i.print_found()
        #if vbf.get_found():
        #    print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN FIRST VIGENERE"
        #    vbf.print_found()
        #if vbf_i.get_found():
        #    print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN VIGENERE USING REVERSE STRING"
        #    vbf_i.print_found()
        print "###### End Search ######"
        print

    print "###### FeatherDuster ######"
    if f_stderr:
        print " ---> ERROR <---"
        print f_stderr
    print f_stdout
    print "###### End FeatherDuster ######"
    print

    if print_each:
        xorbf.mprint()
        xorbf_i.mprint()
        bbf.mprint()
        bbf_i.mprint()
        cbf.mprint()
        cbf_i.mprint()
        sbf.mprint()
        sbf_i.mprint()

if __name__ == "__main__":
   main(sys.argv[1:])