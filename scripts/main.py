#!/usr/bin/env python3

## TODO: add to str2ihex() hex/bin/oct/dec representation support
import sys
import argparse
from intelhex import IntelHex


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
        sys.exit()
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
    str_len = len(in_list[0])
    words_num = int(str_len / 2)
    intel_hex = IntelHex()
    for idx, line in enumerate(in_list):
        is_valid_number(line, 16)
        intel_hex[idx * words_num:idx * words_num + words_num] = list(bytearray.fromhex(line))
    return intel_hex


if __name__ == "__main__":
    ## Parse arguments
    parser = argparse.ArgumentParser(
        prog = "str2ihex",
        description = "Convert character-coded bin/hex/oct numbers to Intel"\
        "Hex format",
        #epilog = "Possible input file formats:\n  - character-coded hexadecimal numbers:"
        epilog = ""
    )
    parser.add_argument('-i', "--input", required=True)
    parser.add_argument('-o', "--output", required=True)
    args = parser.parse_args()

    ## Start conversion
    lines = read_lines(args.input)
    ihex = str2ihex(lines)
    ihex.write_hex_file(args.output)
    sys.exit()
