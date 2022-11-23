#!/usr/bin/env python3

import unittest

import os, sys
#from str2ihex import scripts.str2ihex as s2ih
## caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, "scripts/")
import str2ihex as s2ih


class TestStr2HexConverter(unittest.TestCase):
    """String to Intel hex converter test suite"""

    INPUT_DIR = "./tests/inputs/"
    OUTPUT_DIR = "./out/"

    def test_number_validity(self):
        """Tests number validity checks"""
        self.assertTrue(s2ih.is_valid_number("DEAD"))
        self.assertTrue(s2ih.is_valid_number("DEA"))
        self.assertTrue(s2ih.is_valid_number("0xDEADC0DE"))
        self.assertFalse(s2ih.is_valid_number("0xDEADCODE"))

    def test_ihex_conversion(self):
        """Tests conversion of character-coded data to Intel Hex format"""
        directory = os.fsencode(self.INPUT_DIR)
        dir_content = os.listdir(directory)
        for f in dir_content:
            file_name = os.fsdecode(f)
            print(self.INPUT_DIR + file_name)
            print(self.OUTPUT_DIR + file_name.replace(".txt", ".hex"))
            print("=======================================================")
            #os.system("str2ihex -i
            ### if invalid input
            #if (file_name.find("invalid") == 0):


if __name__ == "__main__":
    unittest.main()
