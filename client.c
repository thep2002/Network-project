#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include "struct.h"

#define BUFF_SIZE 1024

Message* extractMessage(Message* Message, const char *message) {
    char word[BUFF_SIZE+1];
    int i = 0; 
    while (sscanf(message, "%s", word) == 1) {
        if(i==0) {
            if(!strcmp(word,"LOGIN")){
                Message->header = LOGIN;
            }
            if(!strcmp(word,"LOBBY")){
                Message->header = LOBBY;
            }
            if(!strcmp(word,"SENDBATTLE")){
                Message->header = SENDBATTLE;
            }
            if(!strcmp(word,"RECVBATTLE1")){
                Message->header = RECVBATTLE1;
            }
            if(!strcmp(word,"RECVBATTLE2")){
                Message->header = RECVBATTLE2;
            }
            if(!strcmp(word,"CANCELBATTLE")){
                Message->header = CANCELBATTLE;
            }
            if(!strcmp(word,"ACCEPTBATTLE")){
                Message->header = ACCEPTBATTLE;
            }
            if(!strcmp(word,"DONECHOOSE")){
                Message->header = DONECHOOSE;
            }
            if(!strcmp(word,"CANCELCHOOSE")){
                Message->header = CANCELCHOOSE;
            }
            if(!strcmp(word,"ISPLAY")){
                Message->header = ISPLAY;
            }
            if(!strcmp(word,"GETSHIP")){
                Message->header = GETSHIP;
            }      
            if(!strcmp(word,"LOOSE")){
                Message->header = LOOSE;
            }    
            if(!strcmp(word,"GETTURN")){
                Message->header = GETTURN;
            }    
            if(!strcmp(word,"GETMOVE")){
                Message->header = GETMOVE;
            }  
            if(!strcmp(word,"STEP")){
                Message->header = STEP;
            }   
            if(!strcmp(word,"WAITING")){
                Message->header = WAITING;
            }  
            if(!strcmp(word,"NOWAITING")){
                Message->header = NOWAITING;
            }    
            if(!strcmp(word,"GETMATCH")){
                Message->header = GETMATCH;
            }   
            if(!strcmp(word,"SENDVIEW")){
                Message->header = SENDVIEW;
            }  
            if(!strcmp(word,"SENDTXT")){
                Message->header = SENDTXT;
            }  
            if(!strcmp(word,"LOGOUT")){
                Message->header = LOGOUT;
            } 
            if(!strcmp(word,"SIGNIN")){
                Message->header = SIGNIN;
            } 
            if(!strcmp(word,"ENDCON")){
                Message->header = ENDCON;
            } 
        }
        else {
            strcat(Message->message,word);
            strcat(Message->message," ");
            }
        i++;
        message += strlen(word) + 1;
    }
    
    return Message;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <IP address> <port>\n", argv[0]);
        return 1;
    }

    const char *server_ip = argv[1];
    int port = atoi(argv[2]);

    int sockfd;
    char buff[BUFF_SIZE + 1];
    char mess[BUFF_SIZE + 1];
    struct sockaddr_in servaddr;

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;

    if (inet_pton(AF_INET, server_ip, &servaddr.sin_addr) <= 0) {
        perror("Invalid IP address");
        return 2;
    }

    servaddr.sin_port = htons(port);

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Error: Socket creation failed");
        return 3;
    }

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("Error: Connection failed");
        close(sockfd);
        return 4;
    }

    ssize_t end;
    printf("Connected to the server\n");
    fflush(stdout);
    Message receivedStruct;

    while (fgets(buff, sizeof(buff), stdin) != NULL) {
        memset(&receivedStruct, 0, sizeof(receivedStruct));
        extractMessage(&receivedStruct, buff);
        send(sockfd, &receivedStruct, sizeof(receivedStruct), 0);
        recv(sockfd, &receivedStruct, sizeof(receivedStruct), 0);
        switch (receivedStruct.header) {
            case SUSSCESLOGIN:
                printf("SUSSCESLOGIN\n");
                fflush(stdout);
                break;
            case FALSELOGIN:
                printf("FALSELOGIN\n");
                fflush(stdout);
                break;
            case FALSE:
                printf("FALSE\n");
                fflush(stdout);
                return 0;
            case LOBBY:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case SENDBATTLE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case RECVBATTLE1:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case RECVBATTLE2:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case CANCELBATTLE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case ACCEPTBATTLE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case DONECHOOSE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case CANCELCHOOSE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case GETSHIP:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case LOOSE:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case ISPLAY:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case GETTURN:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case SUSSCESSIGNIN:
                printf("SUSSCESSIGNIN\n");
                fflush(stdout);
                break;
            case GETMOVE:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case SENDTXT:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case STEP:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case WAITING:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case NOWAITING:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case LOGOUT:
                printf("TRUE\n");
                fflush(stdout);
                break;
            case GETMATCH:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case SENDVIEW:
                printf("%s\n",receivedStruct.message);
                fflush(stdout);
                break;
            case ENDCON:
                close(sockfd);
                return 0;
            case SIGNIN:
                printf("TRUE\n");
                fflush(stdout);
                break;
            default:
                break;
        }
        
    }  
    
    return 0;
}