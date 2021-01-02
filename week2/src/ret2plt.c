#include<stdio.h>
#include<stdlib.h>

void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
}

int main(){

    init();

    system( "echo 'Say hello to stack :D'" );

    char buf[0x30];
    gets( buf );

    return 0;
}