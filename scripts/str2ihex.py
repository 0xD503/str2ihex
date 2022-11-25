#!/usr/bin/env python3

## TODO: add to str2ihex() bin representation support and test appropriate test cases
## TODO: implement setup.py file
## TODO: implement __init__.py file
## TODO: Add README.md with brief docs
## TODO: Truncate base prefix (0x/0b/h)
## TODO: Add Big/Low endian variants
## TODO: Add copyleft signature
import sys
import argparse
from intelhex import IntelHex


input_format = "Expected input file format:\n"\
    "  NOTE: All lines in a file should have the same length. Base prefixes \n"\
    "        like 0x/0b are optional\n"\
    "\n"\
    "    - hex, 64-bit:\n"\
    "    DEADBEEFCAFEFEED\n"\
    "    0123456789ABCDEF\n"\
    "    ...\n"\
    "\n"\
    "\n"\
    "    - hex, 16-bit, with base prefix:\n"\
    "    0x0123\n"\
    "    0xABCD\n"\
    "    0x4444\n"\
    "    ...\n"\
    "\n"\
    "\n"\
    "    - bin, 8-bit:\n"\
    "    01001101\n"\
    "    11111011\n"\
    "    00000000\n"\
    "    11111111\n"\
    "    10101011\n"\
    "\n"\
    "\n"\
    "    - and the same principle for all others: bin/oct/dec/hex 8/16/32/64-bits\n"

syms_per_byte = {2: 8, 8: 3, 10: 3, 16: 2}


def remove_base(string):
    """Remove number base (radix) prefix/suffix (0x/0b/h) from input string

    Keyword arguments:
    string -- input charcter-encoded number

    Return values:
    string -- charcter-encoded number without base prefix/suffix
    """
    if len(string) > 0:
        if string[:2] in ("0x", "0b"):
            string = string.removeprefix("0x")
            string = string.removeprefix("0b")
        elif string[-1] == 'h':
            string = string.removesuffix('h')
    return string

def is_valid_number(string, encoding=16):
    """Returns True if string is valid character-coded number.

    Keyword arguments:
    string -- character-coded number
    encoding -- encoding scheme: 2 - bin, 8 - oct, 10 - dec, 16 - hex. Defaults to 16 (hex)

    Return values:
    status -- True, if string is valid character-encoded number
    """
    status = False
    try:
        int(string, encoding)
        status = True
    except ValueError as excpt:
        print("ValueError EXCEPTION:", excpt)
        #sys.exit()
    return status

def read_lines(in_file):
    """Reads file and returns list of its lines.

    Keyword arguments:
    in_file -- input file with character-coded numbers

    Return values:
    lines_lst -- list of truncated strings
    """
    with open(in_file, 'r', encoding = "utf-8") as file:
        lines_lst = []
        for line in file:
            line = line.rstrip()
            line = remove_base(line)
            lines_lst.append(line)
    return lines_lst

def str2ihex(in_list, base):
    """Takes a list of numbers in character-coded bin/hex/oct/dec numbers
    representation and returns filled instance of IntelHex() formatter.

    Keyword arguments:
    in_list -- list of strings to process
    base    -- character-coded number base

    Return values:
    success -- True, if succesfully converted strings, otherwise returns False
    intel_hex -- if operation succeded, it's valid IntelHex object
    """
    success = False
    intel_hex = IntelHex()
    try:
        ## set str_len to even number
        str_len = len(in_list[0])
        str_len += str_len % 2
    except IndexError as excpt:
       print("IndexError EXCEPTION:", excpt)
       return success, intel_hex
    bytes_num = int(str_len / syms_per_byte[base])
    for idx, line in enumerate(in_list):
        ## prepend line with 0 if it contains an odd number of characters
        if (len(line) % 2) == 1:
            line = line.zfill(len(line) + 1)
        if len(line) != str_len:
            success = False
            break
        success = is_valid_number(line, base)
        if success:
            intel_hex[idx * bytes_num:idx * bytes_num + bytes_num] = list(bytearray.fromhex(line))
        else:
            break
    return success, intel_hex

def convert_str2ihex(in_file, out_file, base):
    """Converts the content of input file to Intel HEX format and writes result
    to out_file

    Keyword arguments:
    in_file -- input file name
    out_file -- output file name
    base -- character-encoded numbers base in input file

    Return values:
    converted -- True if file conversion succeeded, otherwise False
    """
    converted = False
    lines = read_lines(in_file)
    status, ihex = str2ihex(lines, base)
    if status:
        ihex.write_hex_file(out_file)
        converted = True
    return converted



if __name__ == "__main__":
    ## Parse arguments
    parser = argparse.ArgumentParser(
        prog = "str2ihex",
        description = "Convert character-coded bin/hex/oct numbers to Intel "\
        "HEX format",
        epilog = input_format,
        formatter_class = argparse.RawTextHelpFormatter
    )
    parser.add_argument('-i', "--input", required=True)
    parser.add_argument('-o', "--output", required=True)
    parser.add_argument('-b', "--base", required=False)
    args = parser.parse_args()

    base = int()
    if not args.base:
        base = 16               ## Default encoding is hex
    else:
        base = int(args.base)
        if base not in (2, 16):
            print("Wrong base. Possible base values are 2/16")
            raise ValueError
        ## TODO: add bin base (not supported now), overwrite so far
        if base != 16:
            print("Only hex base is supported so far")
            raise ValueError

    ## Start conversion
    convert_str2ihex(args.input, args.output, base)
    sys.exit()
