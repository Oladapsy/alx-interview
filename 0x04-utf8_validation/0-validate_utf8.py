#!/usr/bin/python3
""" utf-8 validation"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7    # 10000000 in binary
    mask2 = 1 << 6    # 01000000 in binary

    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            """Count the number of leading 1s to determine
            the number of bytes in this character"""
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 2
            elif (byte & (mask1 >> 2)) == (mask1 | mask2):
                num_bytes = 3
            elif (byte & (mask1 >> 3)) == (mask1 | mask2 | (mask2 >> 1)):
                num_bytes = 4
            else:
                # Invalid UTF-8 start byte
                return False
        else:
            # Check that this byte is of the form 10xxxxxx
            if (byte & mask1) != mask1 or (byte & mask2) == 0:
                return False
            num_bytes -= 1

    return num_bytes == 0
