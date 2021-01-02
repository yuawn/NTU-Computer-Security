all: src/bof.c src/orw.c src/casino.c
	gcc src/bof.c -o ./bof/share/bof -no-pie -fno-stack-protector
	gcc src/orw.c -o ./orw/share/orw -no-pie -fno-stack-protector -z execstack -lseccomp
	gcc src/casino.c -o ./casino/share/casino -no-pie -z execstack

clean:
	rm bof/share/bof orw/share/orw casino/share/casino