#include<stdio.h>
#include<stdlib.h>


void try_to_call_me(){
    system("sh");
}

int main(){

    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);

    puts( "Welcome to EDU CTF 2019." );

    char buf[0x30];
    gets( buf );

    return 0;
}