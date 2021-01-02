#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>
#include <stdint.h>
#include <fcntl.h>
#define TIMEOUT 180
#define candidates_num 10


struct Candidate{
    char *name;
    uint8_t votes;
} candidates[candidates_num];

int vote = 0;
char buf[0xc8];

char* candidates_name[candidates_num] = {
    "Pusheen",
    "Angelboy",
    "Chinese Tsai",
    "Korean Cat",
    "Trump",
    "Nini ",
    "how2vote",
    "Rilakkuma",
    "John Cena",
    "Capoo"
};


void handler( int signum ){
    uint8_t max;
    for( int i = 0 ; i < candidates_num ; ++i ) max = candidates[i].votes > max ? candidates[i].votes : max;
    for( int i = 0 ; i < candidates_num ; ++i ){
        if( candidates[i].votes == max ){
            printf( "Congrat to %s !!!\n" , candidates[i].name );
            break;
        }
    }
    _exit(1);
}

int read_int(){
    char buf[0x10];
    __read_chk( 0 , buf , 0xf , 0x10 );
    return atoi( buf );
}


void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stdin,0,2,0);
    setvbuf(stderr,0,2,0);
    signal( SIGALRM , handler );
    alarm( TIMEOUT );
}


void banner(){
    puts( "+-------------------------------------------+" );
    puts( "|    EDU 2019 Election Voting System v1.0   |" );
    puts( "+-------------------------------------------+" );
}

void welcome(){
    banner();
    puts( "1. Login" );
    puts( "2. Register" );
    puts( "3. Exit" );
    puts( ">" );
}


void init_candidates(){
    for( int i = 0 ; i < candidates_num ; ++i ){
        candidates[i].name = candidates_name[i];
        candidates[i].votes = 0;
    }
}


void menu(){
    banner();
    puts( "1. Vote" );
    puts( "2. I want to say something to candidates" );
    puts( "3. Logout" );
    puts( ">" );
}



void voting(){
    int n , idx;
    char msg[0xe0];
    while(1){
        menu();
        n = read_int();
        switch( n ){
            case 1:
                if( !vote ){
                    puts( "You can not vote anymore :(" );
                    break;
                }
                puts( "Candidates:" );
                for( int i = 0 ; i < candidates_num ; ++i ){
                    printf( "%d. %s\tvotes: %u\n" , i , candidates[i].name , candidates[i].votes );
                }
                printf( "Your choice [0~9]: " );
                idx = read_int();
                if( idx < 0 || idx >= candidates_num ){
                    puts( "Invalid choice." );
                    break;
                }
                candidates[idx].votes += 1;
                vote -= 1;
                printf( "Done!\n%s: Thank you!\n" , candidates[idx].name );
                break;

            case 2:
                puts( "The more votes candidate has, the more message you can say!" );
                printf( "To [0~9]: " );
                idx = read_int();
                if( idx < 0 || idx >= candidates_num ){
                    puts( "Invalid choice." );
                    break;
                }
                printf( "To %s:\nMessage: " , candidates[idx].name );
                read( 0 , msg , candidates[idx].votes );
                puts( "Done!" );
                break;
                
            case 3:
                return;
                
            default:
                puts( ":)" );
                break;
        }   
    }
}

int main(){

    init();

    init_candidates();

    char token[0xb8] = {0};

    while(1){
        welcome();
        int n = read_int();

        switch( n ){
            case 1:
                printf( "Token: " );
                int len = read( 0 , buf , sizeof( buf ) );

                if( memcmp( buf , token , len ) ){
                    puts( "Invalid token." );
                    break;
                }

                voting();            
                break;
            case 2:
                printf( "Register an anonymous token: " );
                read( 0 , token , sizeof( token ) );

                vote = 10;
                puts( "Done!" );
                break;
            case 3:
                handler(0);
                break;
            default:
                puts( ":)" );
                break;
        }
    }
    return 0;
}