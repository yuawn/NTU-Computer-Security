#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>


int lottery[6] = {0}, guess[6] = {0};
char name[0x10] = {0};
int age, seed;

void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
    seed = time(0);
}

int read_int(){
    char buf[0x10];
    __read_chk( 0 , buf , 0xf , 0x10 );
    return atoi( buf );
}

void welcome(){
    puts( "+--------------------+" );
    puts( "|       Casino       |" );
    puts( "+--------------------+" );
    puts( "" );
}


void casino(){

    srand( seed );
    for( int i = 0 ; i < 6 ; ++i ) lottery[i] = rand() % 100;

    int try = 2, idx;

    while( try-- ){
        printf( "\n$$$$$$$ Lottery $$$$$$$\n " );

        for( int i = 0 ; i < 6 ; ++i ){
            printf( "Chose the number %d: " , i );
            guess[i] = read_int();
        }

        printf( "Change the number? [1:yes 0:no]: " );
        if( read_int() == 1 ){
            printf( "Which number [1 ~ 6]: " );
            idx = read_int() - 1;
            printf( "Chose the number %d: " , idx );
            guess[idx] = read_int();
        }
        
        for( int i = 0 ; i < 6 ; ++i ){
            if( guess[i] != lottery[i] ) break;
            if( i == 5 ){
                puts( "You win! Hacker don't need luck :P" );
            }
        }
    }

    printf( "You lose.\nBye~\n " );
}


int main(){

    init();
    welcome();

    puts( "Show me your passport." );
    printf( "Your name: " );
    read( 0 , name , 0x100 ); // Oops

    printf( "Your age: " );
    age = read_int();

    if( age < 20 ){
        puts( "You can not enter the casino!" );
    }
    else{
        casino();
    }

    return 0;
}