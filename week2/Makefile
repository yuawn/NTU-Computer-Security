all: src/rop.c src/ret2plt.c src/ret2libc.c src/casino++.c
	gcc src/rop.c -o ./rop/share/rop -no-pie -fno-stack-protector --static
	gcc src/ret2plt.c -o ./ret2plt/share/ret2plt -no-pie -fno-stack-protector
	gcc src/ret2libc.c -o ./ret2libc/share/ret2libc -no-pie -fno-stack-protector
	gcc src/casino++.c -o ./casino++/share/casino++ -no-pie

clean:
	rm rop/share/rop ret2plt/share/ret2plt ret2libc/share/ret2libc casino++/share/casino++