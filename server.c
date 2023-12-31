#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include "struct.h"

#define BUFF_SIZE 1024

Account* head = NULL;
Account* tail = NULL;

void account(int id,char *username,char *password){
    Account* newAccount = (Account*)malloc(sizeof(Account));
    strcpy(newAccount->username, username);
    strcpy(newAccount->password, password);
    newAccount->id = id;
    newAccount-> recvBattle = -1;
    newAccount->status = 0;
    newAccount->nextAccount = NULL;
    newAccount->clientSocket = -1;
    
    if (!head) {
        head = newAccount;
        tail = newAccount;
    } else {
        tail->nextAccount = newAccount;
        tail = newAccount;
    }
}

AccoutDOT* extractUsernamePassword(const char *message) {
    AccoutDOT* receivedStruct = (AccoutDOT*)malloc(sizeof(AccoutDOT));

    char word[BUFF_SIZE+1];
    int i=0;

    while (sscanf(message, "%s", word) == 1) {
        if(i==0) strcpy(receivedStruct->username,word);
        else strcpy(receivedStruct->password,word);
        i++;
        message += strlen(word) + 1;
    }
    
    return receivedStruct;
}  

void nhapThongTin() {
    FILE* file = fopen("nguoidung.txt", "r");
    if (file == NULL) {
        perror("Could not open the file\n");
        return;
    }
    char username[33];
    char password[257];
    int id;

    while (fscanf(file, "%d %32s %256s ",&id, username, password) != EOF) {
        account(id,username,password);
    }
    fclose(file);
}

void writeFile() {
    FILE* file = fopen("nguoidung.txt", "w");
    Account* current = head;
    while (current) {
        fprintf(file, "%s %s \n", current->username, current->password);
        current = current->nextAccount;
    }
    fclose(file);
}

Account* findAccount(char usernameNew[33]) {
    Account* current = head;
    while (current) {
        if (!strcmp(current->username, usernameNew)) {
            return current;
        }
        current = current->nextAccount;
    }
    return NULL;
}

Account* findClient(int client) {
    Account* current = head;
    while (current) {
        if (current->clientSocket == client) {
            return current;
        }
        current = current->nextAccount;
    }
    return NULL;
}

Account* findId(int id) {
    Account* current = head;
    while (current) {
        if (current->id == id) {
            return current;
        }
        current = current->nextAccount;
    }
    return NULL;
}

int checkPassword(Account* current, char passwordNew[50]) {
    if (strcmp(current->password, passwordNew)) {
        return 0;
    }
    return 1;
}
void makeAccount(const char *message){
    AccoutDOT* receivedStruct = extractUsernamePassword(message);
    account(tail->id+1,receivedStruct->username,receivedStruct->password);
    free(receivedStruct);
    writeFile();
}

Account* loginAccount(char *message){
    AccoutDOT* receivedStruct = extractUsernamePassword(message);
    Account* login = findAccount(receivedStruct->username);
    if(login){
        if(!strcmp(login->password,receivedStruct->password)){
            if(login->clientSocket != -1) {
                free(receivedStruct);
                return NULL;
            }
            free(receivedStruct);
            return login;
        }
    }
    else{
        free(receivedStruct);
        return NULL;
    }   
}
void findLobby(int clientSocket,char str[]){
    Account* current = head;
    char buffer [5];
    while (current) {
        if (current->clientSocket == clientSocket) {
            current = current->nextAccount;
            continue;
        }
        if (current->status == 0 && current->clientSocket != -1) {
            sprintf(buffer, "%d", current->id);
            strcat(str, buffer);
            strcat(str, " ");
            strcat(str, current->username);
            strcat(str, " ");
            memset(buffer,0,sizeof(buffer));
        }
        current = current->nextAccount;
    }
}

void *handle_client_thread(void *arg){
    Message receivedStruct;
    int clientSocket;
    struct sockaddr_in client_addr;
    socklen_t len = sizeof(client_addr);
    clientSocket = *((int*)arg);
    if (getpeername(clientSocket, (struct sockaddr*)&client_addr, &len) == -1) {
        perror("Error getting client address");
        close(clientSocket);
        pthread_exit(NULL);
    }
    Account* login;
    while(1){
        recv(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
        // printf("%d %s\n",receivedStruct.header,receivedStruct.message);
        switch (receivedStruct.header)
        {
        case SIGNIN:
            makeAccount(receivedStruct.message);
            break;
        case LOGIN:
            login = loginAccount(receivedStruct.message);
            if(login){
                login->clientSocket = clientSocket;
                receivedStruct.header = SUSSCESLOGIN;
            }
            else{
                receivedStruct.header = FALSELOGIN;
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case LOGOUT:
            login = NULL;
            break;
        case SENDBATTLE:
            findId(atoi(receivedStruct.message))->recvBattle = login->id;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case RECVBATTLE1:
            if(login->recvBattle != -1){
                strcpy(receivedStruct.message,findId(login->recvBattle)->username);
                send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0); 
            }
            break;
        case RECVBATTLE2:
            if(login->recvBattle != -1){
                strcpy(receivedStruct.message,findId(login->recvBattle)->username);
                send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0); 
            }
            break;
        case LOBBY:
            if(findClient(clientSocket)){
                memset(&receivedStruct, 0, sizeof(receivedStruct));
                receivedStruct.header = LOBBY;
                findLobby(clientSocket,receivedStruct.message);
            }
            else {
                receivedStruct.header = FALSE;
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        
        default:
            break;
        }
        
    }
 }
int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <port>\n", argv[0]);
        return 1;
    }

    nhapThongTin(); 

    int port = atoi(argv[1]);
    int serverSocket, clientSocket;
    socklen_t len;
    ssize_t end;
    struct sockaddr_in server_addr, client_addr;

    if ((serverSocket = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Error: Socket creation failed");
        return 2;
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(serverSocket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error: Bind failed");
        close(serverSocket);
        return 3;
    }

    if (listen(serverSocket, 5) < 0) {
        perror("Error: Listen failed");
        close(serverSocket);
        return 4;
    }

    printf("Server listening on port %d...\n", port);
    while (1) {
        len = sizeof(client_addr);
        clientSocket = accept(serverSocket, (struct sockaddr*)&client_addr, &len);
        if (clientSocket < 0) {
            perror("Error: Accept failed");
            continue;
        }
        printf("You got a connection from %s\n", inet_ntoa(client_addr.sin_addr));
        pthread_t tid;
        if (pthread_create(&tid, NULL, handle_client_thread, (void*)&clientSocket) != 0) {
            perror("Error: Could not create thread");
            close(clientSocket);
            continue;
        }
        pthread_detach(tid);
    }
    close(serverSocket);
    return 0;
}
