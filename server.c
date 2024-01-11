#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <time.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <dirent.h>
#include "struct.h"
#include <time.h>

#define BUFF_SIZE 1024

Account* head = NULL;
Account* tail = NULL;

const char *directory = "play/";

void account(int id,char *username,char *password){
    Account* newAccount = (Account*)malloc(sizeof(Account));
    strcpy(newAccount->username, username);
    strcpy(newAccount->password, password);
    newAccount->id = id;
    newAccount-> battle = -1;
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
void ghiLog(Account* login, Message* receivedStruct) {
    char word[BUFF_SIZE + 1];
    switch (receivedStruct->header) {
        case SIGNIN:
            strcpy(word,"SIGNIN");
            break;
        case LOGIN:
            strcpy(word,"LOGIN");
            break;
        case LOGOUT:
            strcpy(word,"LOGOUT");
            break;
        case SENDBATTLE:
            strcpy(word,"SENDBATTLE");
            break;
        case ACCEPTBATTLE:
            strcpy(word,"ACCEPTBATTLE");
            break;
        case CANCELBATTLE:
            strcpy(word,"CANCELBATTLE");
            break;
        case STEP:
            strcpy(word,"STEP");
            FILE* file_1 = fopen(login->chesstxt, "a");
            fprintf(file_1, "%d %s\n",login->id, receivedStruct->message);
            fclose(file_1);
            break;
        case LOOSE:
            strcpy(word,"LOOSE");
            break;
        case GETSHIP:
            strcpy(word,"GETSHIP");
            FILE* file_2 = fopen(login->chesstxt, "a");
            fprintf(file_2, "%s %d %s\n",login->username,login->id, receivedStruct->message);
            fclose(file_2);
            break;
        default:
            return;
        }
        
    FILE* file = fopen("log.txt", "a");
    if (file == NULL) {
        perror("Could not open the file\n");
        return;
    }
    if (login) fprintf(file, "%d %s %s\n",login->id,word, receivedStruct->message);
    else fprintf(file, "%s %s\n",word, receivedStruct->message);
    fclose(file);
}
void extractChess(Account* login,const char *message){
    char word1[BUFF_SIZE + 1];
    char word2[BUFF_SIZE + 1];

    while (sscanf(message, "%s %s", word1, word2) == 2) {
        login->chess[atoi(word1)][atoi(word2)] = 1;
        message += strlen(word1) + strlen(word2) + 2;
    }
}
void writeFile() {
    FILE* file = fopen("nguoidung.txt", "w");
    Account* current = head;
    while (current) {
        fprintf(file, "%d %s %s \n",current->id, current->username, current->password);
        current = current->nextAccount;
    }
    fclose(file);
}
void resetChess(Account* login){
    int i,j;
    for(i=0;i<10;i++)
        for(j=0;j<10;j++)
            login->chess[i][j] = 0;
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


int makeAccount(const char *message){
    AccoutDOT* receivedStruct = extractUsernamePassword(message);
    if(findAccount(receivedStruct->username)){
        free(receivedStruct);
        return 1;
    }
    account(tail->id+1,receivedStruct->username,receivedStruct->password);
    free(receivedStruct);
    writeFile();
    return 0;
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
        free(receivedStruct);
        return NULL;
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
void findBattle(int id, char str[]){
    DIR *dir;
    int value1, value2;
    struct dirent *ent;
    char extractedString[50]; 
    char str1[256];
    if ((dir = opendir("./play")) != NULL) {
        while ((ent = readdir(dir)) != NULL) {
            if (strstr(ent->d_name, ".txt") != NULL) {
                char *dotPos = strchr(ent->d_name, '.');
                if (dotPos != NULL) {
                    size_t length = dotPos - ent->d_name;
                    strncpy(extractedString, ent->d_name, length);
                    extractedString[length] = '\0';

                }
                if (sscanf(extractedString, "%d_%d_%s", &value1, &value2, str1) == 3) {
                    if(value1 == id || value2 == id){
                        strcat(str, "./play/");
                        strcat(str, ent->d_name);
                        strcat(str, " ");
                        strcat(str, str1);
                        strcat(str, " ");
                    }
                }
            }
        
        }
    }
    closedir(dir);
}
   
void sendView(int id, char str[],Account* login){
    FILE *file;
    char line[256];  
    file = fopen(login->chesstxt, "r");
    if (file == NULL) {
        perror("Không thể mở tệp tin");
        return ;
    }

    for (int i = 1; i <= id; ++i) {
        if (fgets(line, sizeof(line), file) == NULL) {
            strcpy(str,"DONE");
            fclose(file);
            return;
        }
    }
    line[strlen(line)-1] = '\0';
    strcpy(str,line);
    fclose(file);
    return;
} 
int checkChess(Account* login,const char *message){
    char word1[BUFF_SIZE + 1];
    char word2[BUFF_SIZE + 1];

    sscanf(message, "%s %s", word1, word2);
    if (findId(login->battle)->chess[atoi(word1)][atoi(word2)] == 1)
        return 1; 
    else return 0;
}
void *handle_client_thread(void *arg){
    Message receivedStruct;
    int clientSocket,m;
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
        // printf("%d\n",receivedStruct.header);
        ghiLog(login,&receivedStruct);
        switch (receivedStruct.header)
        {
        case ENDCON:
            close(clientSocket);
            printf("End connect form %s\n",inet_ntoa(client_addr.sin_addr));
            return 0;
        case SIGNIN:
            if(makeAccount(receivedStruct.message) == 0){
                receivedStruct.header = SUSSCESSIGNIN;
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case LOGOUT:
            login->clientSocket = -1;
            login = NULL;
            
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
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
        case SENDBATTLE:
            login->battle = atoi(receivedStruct.message);
            login->status = 1;
            findId(login->battle)->status = 1;
            findId(login->battle)->battle = login->id;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case RECVBATTLE1:
            if(login->battle != -1){
                strcpy(receivedStruct.message,findId(login->battle)->username);
            }
            else{
                strcpy(receivedStruct.message,"-1");
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0); 
            break;
        case RECVBATTLE2:
            if(login->battle == -1){
                strcpy(receivedStruct.message,"-1");
            }
            else{
                if(login->status != 2){
                    strcpy(receivedStruct.message,"Waiting");
                }
                else
                    strcpy(receivedStruct.message,"ACCEPTBATTLE");
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0); 
            break;
        case CANCELBATTLE:
            login->status = 0;
            findId(login->battle)->status = 0;
            findId(login->battle)->battle = -1;
            login->battle = -1;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
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
        case ACCEPTBATTLE:
            login->status = 2;
            findId(login->battle)->status = 2;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case DONECHOOSE:
            login->status = 3;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case CANCELCHOOSE:
            login->status = 2;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case GETSHIP:
            extractChess(login,receivedStruct.message);
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case LOOSE:
            login->status = 0;
            login->battle = -1;
            login->chesstxt[0] = '\0';
            resetChess(login);
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case STEP:
            strcpy(login->move,receivedStruct.message);
            if (checkChess(login,receivedStruct.message) == 1)
                strcpy(receivedStruct.message,"TRUE");
            else {
                strcpy(receivedStruct.message,"NOT");
                login->status = 5;
                findId(login->battle)->status = 4;
            }
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case GETMOVE:
            if (strlen(findId(login->battle)->move)!=0){
                strcpy(receivedStruct.message,findId(login->battle)->move);
                findId(login->battle)->move[0] = '\0';
            }
            else strcpy(receivedStruct.message,"-1");
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case GETTURN:
            if (login->status == 3){
                srand(time(NULL));
                if (rand() % 2){
                    login->status = 4;
                    findId(login->battle)->status = 5;
                }
                else{
                    login->status = 5;
                    findId(login->battle)->status = 4;
                }
            }
            if (findId(login->battle)->wait == 1){
                strcpy(receivedStruct.message,"WAIT");
            }
            else if(findId(login->battle)->status == 0){
                login->battle = -1;
                login->status=0;
                login->chesstxt[0] = '\0';
                resetChess(login);
                strcpy(receivedStruct.message,"WIN");
            }
            else if(login->status == 4)
                strcpy(receivedStruct.message,"TRUE");
            else if(login->status == 5)
                strcpy(receivedStruct.message,"NOT");

            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case WAITING:
            login->wait = 1;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case NOWAITING:
            login->wait = 0;
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case ISPLAY:
            if(login->status == 3){   
                if (findId(login->battle)->status == 3){                       
                    strcpy(receivedStruct.message,"TRUE");
                    if (strlen(login->chesstxt) == 0) {
                        char filename[20]; 
                        time_t rawtime;
                        struct tm *timeinfo;
                        time(&rawtime);
                        timeinfo = localtime(&rawtime);
                        sprintf(filename, "%d_%d_%02d%02d%02d%02d.txt", login->id, login->battle,
                        timeinfo->tm_mon + 1, timeinfo->tm_mday,timeinfo->tm_hour, timeinfo->tm_min);
                        sprintf(login->chesstxt, "%s%s", directory, filename);
                        sprintf(findId(login->battle)->chesstxt, "%s%s", directory, filename);
                    }
                }
                else strcpy(receivedStruct.message,"NOT");
            }
            else if (findId(login->battle)->status == 0){
                    login->battle = -1;
                    login->status=0;
                    strcpy(receivedStruct.message,"WIN");
                }
            else  strcpy(receivedStruct.message,"NOT");
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case GETMATCH:
            findBattle(login->id,receivedStruct.message);
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case SENDTXT:
            strcpy(login->chesstxt,receivedStruct.message);
            login->chesstxt[strlen(login->chesstxt)-1] = '\0';
            send(clientSocket, &receivedStruct, sizeof(receivedStruct), 0);
            break;
        case SENDVIEW:
            m = atoi(receivedStruct.message);
            receivedStruct.message[0] = '\0';
            sendView(m,receivedStruct.message,login);
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
