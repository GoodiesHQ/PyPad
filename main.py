#!/usr/bin/env python3
from __future__ import print_function

from pypad import ansi_x923
from pypad import iso_10126
from pypad import pkcs7
from pypad import zero

message = b"Testing"

for padder in [ansi_x923, iso_10126, pkcs7, zero]:
    print("{:<15}".format(padder.__name__), repr(padder.pad(message, 10)))

