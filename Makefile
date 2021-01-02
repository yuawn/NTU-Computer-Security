all: 
	make -C week1
	make -C week2
	make -C week3

clean:
	make -C week1 clean
	make -C week2 clean
	make -C week3 clean