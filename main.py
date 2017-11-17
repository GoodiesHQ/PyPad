#!/usr/bin/env python3
from __future__ import print_function

from pypad import ansi_x923
from pypad import iso_10126
from pypad import pkcs7
from pypad import zero

message = b"Testing"

for padder in [ansi_x923, iso_10126, pkcs7, zero]:
    print("Algorithm:", padder.__name__)
    print("Original: ", repr(message))
    print("Padded 1: ", repr(padder.pad(message, 0x10)))
    print("Padded 2: ", repr(padder.pad(message, 0x10)))
    print("Padded 3: ", repr(padder.pad(message, 0x10)))
