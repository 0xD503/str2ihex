#!/usr/bin/env python3

## TODO: add to str2ihex() 8/16/32/64 bit words support with hex/bin/oct representation
import sys
import argparse
from intelhex import IntelHex


# class Str2IHexConverter:
#     """Provides functional for conversion of character-coded binary numbers to
#     Intel Hex format files
#     """

#     def usage(self, program_name):
#         """Print usage info."""
#         print("usage: ", program_name, " OPTION ARG")
#         print("Arguments:")
#         return

#     def read_lines(self, in_file):
#         """Reads file and returns list of its lines."""
#         with open(in_file, 'r', encoding = "utf-8") as file:
#             lines_lst = []
#             for line in file:
#                 lines_lst.append(line.rstrip())
#         return lines_lst

#     def str2ihex(in_list):
#         """Takes a list of numbers in character-coded binary numbers
#         representation and returns filled instance of IntelHex() formatter.

#         Keyword arguments:
#         in_list -- list of strings to process
#         """
#         intel_hex = IntelHex()
#         for idx, line in enumerate(in_list):
#             try:
#                 intel_hex[idx * 8:idx * 8 + 8] = list(bytearray.fromhex(line))
#             except ValueError as excpt:
#                 print("Invalid input value: ", excpt)
#                 return None
#         return intel_hex

def usage(program_name):
    """Print usage info."""
    print("usage: ", program_name, " OPTION ARG")
    print("Arguments:")
    return

def read_lines(in_file):
    """Reads file and returns list of its lines."""
    with open(in_file, 'r', encoding = "utf-8") as file:
        lines_lst = []
        for line in file:
            lines_lst.append(line.rstrip())
    return lines_lst

def str2ihex(in_list):
    """Takes a list of numbers in character-coded bin/hex/oct numbers
    representation and returns filled instance of IntelHex() formatter.

    Keyword arguments:
    in_list -- list of strings to process
    """
    str_len = len(in_list[0])
    words_num = int(str_len / 2)
    intel_hex = IntelHex()
    for idx, line in enumerate(in_list):
        try:
            intel_hex[idx * words_num:idx * words_num + words_num] = list(bytearray.fromhex(line))
        except ValueError as excpt:
            print("Invalid input value: ", excpt)
            return None
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
