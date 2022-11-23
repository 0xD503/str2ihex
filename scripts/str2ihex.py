#!/usr/bin/env python3

## TODO: add to str2ihex() hex/bin/oct/dec representation support
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


def is_valid_number(string, encoding=16):
    """Returns True if string is valid character-coded number.

    Keyword arguments:
    string -- character-coded number
    encoding -- encoding scheme: 2 - bin, 8 - oct, 10 - dec, 16 - hex. Defaults to 16 (hex)
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
    """
    with open(in_file, 'r', encoding = "utf-8") as file:
        lines_lst = []
        for line in file:
            lines_lst.append(line.rstrip())
    return lines_lst

def str2ihex(in_list):
    """Takes a list of numbers in character-coded bin/hex/oct/dec numbers
    representation and returns filled instance of IntelHex() formatter.

    Keyword arguments:
    in_list -- list of strings to process
    """
    #str_len = len(in_list[0])
    try:
        str_len = len(in_list[0])
    except IndexError as excpt:
       print("IndexError EXCEPTION:", excpt)
       sys.exit()
    words_num = int(str_len / 2)
    intel_hex = IntelHex()
    for idx, line in enumerate(in_list):
        status = is_valid_number(line, 16)
        if status:
            intel_hex[idx * words_num:idx * words_num + words_num] = list(bytearray.fromhex(line))
        else:
            break
    return status, intel_hex


if __name__ == "__main__":
    ## Parse arguments
    parser = argparse.ArgumentParser(
        prog = "str2ihex",
        description = "Convert character-coded bin/hex/oct numbers to Intel "\
        "Hex format",
        epilog = input_format,
        formatter_class = argparse.RawTextHelpFormatter
    )
    parser.add_argument('-i', "--input", required=True)
    parser.add_argument('-o', "--output", required=True)
    args = parser.parse_args()

    ## Start conversion
    lines = read_lines(args.input)
    status, ihex = str2ihex(lines)
    if status:
        ihex.write_hex_file(args.output)
    sys.exit()
