#!/usr/bin/env python3

## Copyright (c) 2022 Ruslan Vostretsov
## All rights reserved.
## This file is a part of project str2ihex which is released under BSD 3-Clause
## license. Go to https://github.com/0xD503/str2ihex for full license details


import unittest

import os, sys
import filecmp as fcmp

sys.path.insert(1, "scripts/")
import str2ihex as s2ih


class TestStr2HexConverter(unittest.TestCase):
    """String to Intel hex converter test suite"""

    INPUT_DIR = "tests/inputs/"
    EXP_OUT_DIR = "tests/expected_output/"

    def test_number_validity(self):
        """Tests number validity checks"""
        self.assertTrue(s2ih.is_valid_number("DEAD"))
        self.assertTrue(s2ih.is_valid_number("DEA"))
        self.assertTrue(s2ih.is_valid_number("0xDEADC0DE"))
        self.assertFalse(s2ih.is_valid_number("0xDEADCODE"))
        self.assertFalse(s2ih.is_valid_number("0xD1ADCODE"))

    def test_ihex_conversion(self):
        """Tests conversion of character-coded data to Intel Hex format"""
        directory = os.fsencode(self.INPUT_DIR)
        dir_content = os.listdir(directory)
        for f in dir_content:
            f_name = os.fsdecode(f)
            in_f = self.INPUT_DIR + f_name
            exp_out_f = self.EXP_OUT_DIR + f_name.replace(".txt", ".hex")
            out_f = "out/" + f_name.replace(".txt", ".hex")
            if s2ih.convert_str2ihex(in_f, out_f, 16):
                #print("Comparing {0} and {1} files...".format(exp_out_f, out_f))
                self.assertTrue(fcmp.cmp(out_f, exp_out_f))



if __name__ == "__main__":
    unittest.main()
