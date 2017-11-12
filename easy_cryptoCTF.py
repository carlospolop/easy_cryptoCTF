#!/usr/bin/python
import sys, os, getopt

from xor_cypher import XOR_cypher
from bases_decoder import Bases_BF
from caesar_decoder import Caesar_BF
from vigenere_decoder import Vigenere_BF

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hc:s:f:",["ifile=","command=","search="])
    except getopt.GetoptError:
        print ' -c <StringEncrypted> -f <inputfileEncrypted> -s <String_to_search>'
        sys.exit(2)

    toDecrypt = ""
    search = ""
    outputfile = ""
    for opt, arg in opts:
        if opt == '-h':
            print ' -c <StringEncrypted> -f <inputfileEncrypted> -s <String_to_search>'
            sys.exit()
        elif opt in ("-c", "--command"):
            toDecrypt = arg
        elif opt in ("-f", "--ifile"):
            inputfile = arg
            if (os.path.isfile(inputfile)):
                with open(inputfile, 'r') as f:
                    toDecrypt = f.read()
            else:
                print "Not a file: "+inputfile
                sys.exit(-1)
        elif opt in ("-s", "--search"):
            search = arg


    if toDecrypt == "":
        print " -c <StringEncrypted> -f <inputfileEncrypted> -s <String_to_search>"
        sys.exit(-1)

    toDecrypt_i = toDecrypt[::-1]
    final_decrypt = {}

    # XOR MODULE
    xorbf = XOR_cypher(toDecrypt, search)
    final_decrypt_xor = xorbf.bruteForce()
    xorbf.mprint()

    xorbf_i = XOR_cypher(toDecrypt_i, search)
    final_decrypt_xor_i = xorbf_i.bruteForce()
    xorbf_i.mprint()

    # BASE MODULE
    bbf = Bases_BF(toDecrypt, search)
    final_decrypt_bases = bbf.bruteForce()
    bbf.mprint()

    bbf_i = Bases_BF(toDecrypt_i, search)
    final_decrypt_bases_i = bbf_i.bruteForce()
    bbf_i.mprint()

    # Caesar MODULE
    cbf = Caesar_BF(toDecrypt, search)
    final_decrypt_caesar = cbf.bruteForce()
    cbf.mprint()

    cbf_i = Caesar_BF(toDecrypt_i, search)
    final_decrypt_caesar_i = cbf_i.bruteForce()
    cbf.mprint()

    # Vigenere MODULE
    vbf = Vigenere_BF(toDecrypt, "password", search)
    final_decrypt_vigenere = vbf.bruteForce()
    vbf.mprint()

    vbf_i = Vigenere_BF(toDecrypt_i, "password", search)
    final_decrypt_vigenere_i = vbf_i.bruteForce()
    vbf_i.mprint()


    #Search MODULE
    if search != "":
        print "###### SEARCH ######"
        if xorbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN FIRST XOR"
            xorbf.print_found()
        if xorbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN SECOND(reverse) XOR"
            xorbf_i.print_found()
        if bbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN FIRST BASES"
            bbf.print_found()
        if bbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN SECOND(reverse) BASES"
            bbf_i.print_found()
        if cbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN FIRST CAESAR"
            cbf.print_found()
        if cbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN SECOND(reverse) CAESAR"
            cbf_i.print_found()
        if vbf.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN FIRST VIGENERE"
            vbf.print_found()
        if vbf_i.get_found():
            print "!/\!/\!/\!/\!/\!/\! SEARCH FOUND IN SECOND(reverse) VIGENERE"
            vbf_i.print_found()


if __name__ == "__main__":
   main(sys.argv[1:])