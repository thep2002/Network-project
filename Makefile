all: server client

server: server.c
	gcc -pthread server.c -o server

client: client.c
	gcc client.c -o client

.PHONY: clean

clean:
	rm -f server client
	