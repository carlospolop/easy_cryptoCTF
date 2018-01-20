# easy_cryptoCTF
Brute Force to easy encrypted strings and check if a string appear in any uncrypted string:
python easy_cryptoCTF.py -c <StringEncrypted> -f <inputfileEncrypted> -s <String_to_search> -x -b -e -t -d -n

## XOR(-x)
- [x] simple
- [x] double
- [x] Last char as key
- [x] Last xored char as key
- [x] Subs to key last char
- [x] Subs to key last xored char
- [x] Key plus last char
- [x] Key plus last xored char

## Bases(-b)
- [x] Base 64 (all positions of the typical alphabet)
- [x] Base 64 (all positions of the url safe alphabet)
- [x] Base 32 (all positions of the typical alphabet)
- [x] Check Base85

## Caesar(-e)
- [x] Ascii lowercase alphabet 
- [x] Ascii uppercase alphabet 
- [x] Ascii lowercase alphabet + ascii uppercase alphabet
- [x] Ascii lowercase alphabet + ascii uppercase alphabet + digits
- [x] Ascii uppercase alphabet + ascii lowercase alphabet + digits

## Scytale(-t)
## Autopwn of Featherduster(-d)

