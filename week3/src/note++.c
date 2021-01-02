#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <stdint.h>
#define MAX 10


void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
}


int read_int(){
    char buf[0x10];
    __read_chk( 0 , buf , 0xf , 0x10 );
    return atoi( buf );
}

int read_input( char *buf , unsigned int size ){
    int ret = __read_chk( 0 , buf , size , size );
    if(ret <= 0){
        puts("read error");
        _exit(1);
    }
    if(buf[ret-1] == '\n'){
        buf[ret-1] = '\0';
    }
    return ret;
}


struct Note{
    int is_freed;
    char *data;
    char description[48];
};

struct Note notes[MAX];

void add(){
    for( int i = 0 ; i < MAX ; ++i ){
        if( !notes[i].data || notes[i].is_freed ){

            printf( "Size: " );
            unsigned int size = read_int();

            if( size > 0x78 ){
                puts( "Too big!" );
                return;
            }

            notes[i].data = malloc( size );
            memset( notes[i].data , 0 , size ); // no information leak

            printf( "Note: " );
            read_input( notes[i].data , size - 1 );

            printf( "Description of this note: " );
            
            // fixed overflow
            // scanf( "%s" , notes[i].description ) // overflow
            scanf( "%48s" , notes[i].description ); // safe

            notes[i].is_freed = 0;

            puts( "Done!" );
            return;
        }
    }
    puts( "Full!" );
}


void list(){
    for( int i = 0 ; i < MAX ; ++i ){
        if( notes[i].data && !notes[i].is_freed ){
            printf( "Note %d:\n  Data: %s\n  Desc: %s\n" , i , notes[i].data , notes[i].description );
        }
    }
    puts("");
}


void delete(){
    printf( "Which note do you want to delete?\nIndex: " );
    uint64_t idx = read_int();

    if( idx >= MAX ){
        puts( "Invalid index." );
        return;
    }

    if( !notes[idx].data ){
        puts( "No such note!" );
        return;
    }

    if( notes[idx].is_freed ){
        puts( "Double free! Bad hacker :(" );
        _exit(-1);
    }

    free( notes[idx].data );
    notes[idx].is_freed = 1;
}


void menu(){
    puts( "1. Add a note" );
    puts( "2. List notes" );
    puts( "3. Delete a note" );
    puts( "4. Exit" );
    puts( "> " );
}


int main(){

    init();
    
    while(1){
        menu();

        int n = read_int();

        switch( n ){
            case 1:
                add();
                break;
            case 2:
                list();
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