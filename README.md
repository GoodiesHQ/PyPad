# pypad
A simple python module for various padding schemes.

## Padding Schemes:
A review of each padding scheme. Note that if the original data is aligned to the block size, each padding scheme will add a full block of data.

**Note:** All examples are using a 0x10 (16) byte block size, but these algorithms support a block size of up to 0x100.

#### ANSI x.923
Pads the bytes `\x00` in repetition followed by the number of bytes (including itself) were used in padding. Since the greated value stored in the last byte is 0xff, this algorithm has a limited block size to 256 (`0x100`).

    Algorithm: pypad.ansi_x923
    Original:  b'Testing'
    Padded  :  b'Testing\x00\x00\x00\x00\x00\x00\x00\x00\x09'  # (\x09 = \t)

#### ISO 10127
Similar to ANSI x.923. The only difference is that random bytes are generated for use in padding instead of `\x00`

    Original:  b'Testing'
    Padded 1:  b'Testing\x95\xb8<el,\x10\x1c\t'
    Padded 2:  b'Testing\xb2\x13\x82\xf5\x8f\n\xf9\x1c\t'
    Padded 3:  b'Testing\x1b\xfax\xe7D\xe4\x82e\t'
    
#### PKCS#7
Repeats the number of bytes padded, N, N times. An example makes more sense:

    Original:  b'Testing'
    Padded 1:  b'Testing\x09\x09\x09\x09\x09\x09\x09\x09\x09'


## How To Use:

Each padding scheme provides three internal components:

| Module | Pad | Unpad | Max Block Size |
|-----------|-----|-------|----------------|
|ansi_x923 | pad(<br>buf: bytes, <br>block_size: int=0x100<br>) | unpad(<br>buf: bytes<br>) |0x100 (256)|
|iso_10126 | pad(<br>buf: bytes, <br>block_size: int=0x100<br>) | unpad(<br>buf: bytes<br>) |0x100 (256)|
|pkcs7 | pad(<br>buf: bytes, <br>block_size: int=0x100<br>) | unpad(<br>buf: bytes<br>) |0x100 (256)|
|zero | pad(<br>buf: bytes,<br>block_size: int=0,<br>byte: bytes=b'\x00'<br>) | unpad(<br>buf: bytes,<br>byte: bytes=None<br>) |N/A|

An example:

    from __future__ import print_function
    # Note: 'random' is an alias for iso_10126
    # from pypad import random
    
    from pypad import ansi_x923
    from pypad import iso_10126
    from pypad import pkcs7
    from pypad import zero
    
    message = b"This is a test message"
    block_size = 0x10
    
    for padder in (ansi_x923, iso_10126, pkcs7, zero):
        print("Algorithm:", padder.__name__.split(".")[-1])
        print("Original :", repr(message))
        print("Padded   :". repr(padder.pad(message, block_size)))
        print()
