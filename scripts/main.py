#!/usr/bin/env python3

## TODO: add to str2ihex() 8/16/32/64 bit words support with hex/bin/oct representation
import sys
import argparse
from intelhex import IntelHex


def usage(program_name):
    """Print usage info."""
    print("usage: ", program_name, " OPTION ARG")
    print("Arguments:")

def read_lines(in_file):
    """Reads file and returns list of its lines."""
    with open(in_file, 'r', encoding = "utf-8") as file:
        lines_lst = []
        for line in file:
            lines_lst.append(line.rstrip())
    return lines_lst

def str2ihex(in_list):
    """Takes a list of numbers in character-coded binary numbers representation
    and returns filled instance of IntelHex() formatter

    Keyword arguments:
    in_list -- list of strings to process
    """
    intel_hex = IntelHex()
    for idx, line in enumerate(in_list):
        try:
            intel_hex[idx * 8:idx * 8 + 8] = list(bytearray.fromhex(line))
            #continue
        except ValueError as excpt:
            print("Invalid input value: ", excpt)
            return None
    return intel_hex


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit()

    lines = read_lines(sys.argv[1])
    ihex = str2ihex(lines)
    ihex.write_hex_file(sys.argv[2])
    sys.exit()
