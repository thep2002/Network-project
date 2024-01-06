#ifndef STRUCT_H
#define STRUCT_H

#define MAX_MESSAGE_SIZE 128

typedef struct Account {
    char username[33];
    char move[10];
    char password[257];
    int chess[10][10];
    int id;
    int battle;
    int status;
    int clientSocket;
    struct Account* nextAccount;
} Account;

typedef enum{
LOGIN, 
SIGNIN, 
STEP, 
SUSSCESLOGIN, 
FALSELOGIN, 
LOBBY, 
LOGOUT,
SENDBATTLE,
RECVBATTLE1,
RECVBATTLE2,
FALSE,
CANCELBATTLE,
ACCEPTBATTLE,
DONECHOOSE,
CANCELCHOOSE,
ISPLAY,
GETSHIP,
GETTURN,
LOOSE,
GETMOVE,
} Header;

typedef struct AccoutDOT
{
    char username[33];
    char password[257];
}AccoutDOT;

typedef struct {
    Header header;
    char message[MAX_MESSAGE_SIZE];
} Message;
#endif
