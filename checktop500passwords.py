#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import hashlib
import sys

fname = "top500passwords.txt"
encrypts = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

def doencrypt(s):
    h = hashlib.new(enc)
    h.update(s)
    return h.hexdigest()


try:
    F = open(fname, "r")
    top500 = F.readlines()
    F.close()
except IOError:
    print "Cannot find file: %" % fname


for x in top500:
    # decrypted password
    print "%s" % x.rstrip("\n"),
    # encrypt password with different ways
    for enc in encrypts:
        print "(%s)%s" % (enc, doencrypt(x)),
    print ""

