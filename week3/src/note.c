#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include <stdint.h>
#define MAX 10


void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
}


uint64_t read_long(){
    char buf[0x10];
    __read_chk( 0 , buf , 0xf , 0x10 );
    return atol( buf );
}


char* notes[MAX];

void add(){
    for( int i = 0 ; i < MAX ; ++i ){
        if( !notes[i] ){
            printf( "Size: " );
            uint64_t size = read_long();

            notes[i] = malloc( size );

            printf( "Note: " );
            read( 0 , notes[i] , size - 1 );

            puts( "Done!" );
            return;
        }
    }
    puts( "Full!" );
}


void show(){
    printf( "Which note do you want to show?\nIndex: " );
    uint64_t idx = read_long();

    if( idx >= MAX ){
        puts( "Invalid index." );
        return;
    }

    if( notes[idx] ){
        printf( "Note %d:\n%s\n" , idx , notes[idx] );
    }
    else{
        puts( "No such note!" );
    }
}


void delete(){
    printf( "Which note do you want to delete?\nIndex: " );
    uint64_t idx = read_long();

    if( idx >= MAX ){
        puts( "Invalid index." );
        return;
    }

    if( notes[idx] ){
        free( notes[idx] ); // dangling pointer, vulnerable!
        // notes[idx] = NULL; // The proper way
    }
    else{
        puts( "No such note!" );
    }
}


void menu(){
    puts( "1. Add a note" );
    puts( "2. Show a note" );
    puts( "3. Delete a note" );
    puts( "4. Exit" );
    puts( "> " );
}


int main(){

    init();
    
    while(1){
        menu();

        uint64_t n = read_long();

        switch( n ){
            case 1:
                add();
                break;
            case 2:
                show();
                break;
            case 3:
                delete();
                break;
            default:
                puts( "Invalid choice." );
                break;
        }
    }
    
    return 0;
}