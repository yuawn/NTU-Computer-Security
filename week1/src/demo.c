#include<stdio.h>
#include<stdlib.h>

int main(){

    char buf[0x100];
    read( 0 , buf , 0x100 );

    puts( "Hello World!" );

    return 0;
}