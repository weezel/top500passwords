#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import hashlib
from typing import List

passwords_file = "top500passwords.txt"
encrypts = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']


def do_encrypt(s: str, enc: str) -> str:
    h = hashlib.new(enc)
    h.update(s.encode("utf-8"))
    return h.hexdigest()


def get_top500_common_passwds(filename: str) -> List[str]:
    with open(filename, "r") as f:
        data = f.readlines()
    return data if data is not None else list()


def main():
    top500_passwds = get_top500_common_passwds(passwords_file)
    for passwd in top500_passwds:
        # Decrypted password
        print("{}".format(passwd.rstrip("\n")))
        # Encrypt password with different ciphers
        for enc in encrypts:
            print("(%s) %s" % (enc, do_encrypt(passwd, enc)))
        print()


if __name__ == '__main__':
    main()
