#ifndef STRUCT_H
#define STRUCT_H

#define MAX_MESSAGE_SIZE 128

typedef struct Account {
    char username[33];
    char password[257];
    int id;
    int recvBattle;
    int sendBattle;
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
ACCEPTBATTLE
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
