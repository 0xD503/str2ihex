# str2ihex - Convert character-coded numbers to the Intel HEX format.

## Dependencies
- [intelhex](https://github.com/python-intelhex/intelhex)

## Termins
#### Character-coded number - number represented as string of chars, e.g.:
- "FF" (base 16) represents number 255, because 0xFF == 255;
- "1EA" (base 16) represents number 490, because 0x1EA == 490;
- "10" (base 16) represents number 16, because 0x10 == 16;
- "10" (base 2) represents number 4, because 0b10 == 4.

#### [Intel HEX](https://en.wikipedia.org/wiki/Intel_HEX) - object file format, that conveys binary information in ASCII text form.

## Description
Utility takes an input file, consisting of strings, that represent numbers;
It validates and processes input file. If validation succeeded, utility creates
Intel HEX format of data that was encoded in input file.

## Examples
1. Convert character-coded hexadecimal data to Intel HEX:

  `./scripts/str2ihex.py -b 16 -i path/to/input/file.txt -o path/to/output/file.hex`
  
  Possible input file in this case would be like:
<br>``10EAFFE3``</br>
    ``D76ACC29``</br>
    ``01234567``</br>
    ``1233441``</br>
    ``ABCDEF12``</br>
    
  **Note, that all strings should have the same size (or differ in size only by 1
  symbol)**
  
2. Convert character-coded binary data to Intel HEX:

  `./scripts/str2ihex.py -b 2 -i path/to/input/file.txt -o path/to/output/file.hex`

  Possible input file in this case would be like:
<br>``10011011``</br>
    ``11111110``</br>
    ``11111111``</br>
    ``01111111``</br>
    ``01111110``</br>
    ``00000001``</br>

  **Note, that all strings should have the same size (or differ in size only by 1
  symbol)**
