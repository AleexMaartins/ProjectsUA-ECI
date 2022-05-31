from email import header
import select
import socket
import json
import sys
import os
import csv
from common_comm import send_dict, recv_dict, sendrecv_dict
from pathlib import Path

users = {}
clients_aux = {}

def new_msg (client_sock):
    msg = recv_dict(client_sock)
    op = msg['op']
   
    if op == "START": 
        client_id = msg['client_id']
        if client_id in users.keys():
            response = { "op": "START", "status": False, "error": "Existent Client" }
            send_dict(client_sock, response)
        else:
            print("New Client connected. ID: " + client_id)
            response = { "op": "START", "status": True }
            send_dict(client_sock, response)
            users[client_id] = []
            clients_aux[client_sock] = client_id

    elif op == "NUMBER":
        client_id = clients_aux.get(client_sock)
        if client_id not in users.keys():
            response = { "op": "NUMBER", "status": False, "error": "Inexistent Client" }
            send_dict(client_sock, response)
        else:
                response = { "op": "NUMBER", "status": True }
                send_dict(client_sock, response)
                list = users.get(client_id)
                list.append(msg['number'])
                users[client_id] =  list

    elif op == "STOP": 
        client_id = clients_aux.get(client_sock)

        if client_id not in users.keys(): 
            response = { "op": "STOP", "status": False, "error": "Inexistent Client" }
            send_dict(client_sock, response)
        else:
            if users.get(client_id) == []:
                response = { "op": "STOP", "status": False, "error": "Insuficient Data" }
                send_dict(client_sock, response)
            else:
                list = users.get(client_id)            
                minimum = min(list) 
                maximum = max(list) 
                create_file(client_sock,list, minimum, maximum)
                response = { "op": "STOP", "status": True, "min": minimum, "max": maximum } 
                send_dict(client_sock, response)

    elif op == "QUIT":
        client_id = clients_aux.get(client_sock)
        if client_id not in users.keys():
            response = { "op": "QUIT", "status": False, "error": "Inexistent Client" }
            send_dict(client_sock, response)
        else:
            response = { "op": "QUIT", "status": True }
            send_dict(client_sock, response)



def create_file (client_sock,list, min_n, max_n):
    client_id = clients_aux.get(client_sock)

    #get current directory
    directory = os.getcwd()
    
    my_file = Path(directory + "/report.csv")
    
    if not my_file.is_file():
        f = open(directory + "/report.csv", 'w')
    else:
        f = open(directory + "/report.csv", 'a')
    header = ["client_id"," list"," min "," max:"]
    data = [client_id,list,min_n,max_n]
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(header)
    writer.writerow(data)

    # close the file
    f.close()

def clean_client(client_sock):
    client_id = clients_aux.get(client_sock)
    users.pop(client_id)    
    clients_aux.pop(client_sock)
    


def main():
    if len(sys.argv) != 2:
        print("Error.Wrong number of arguments.")
        print("Use: python3 server.py <port>")
        sys.exit(1)
    port = int(sys.argv[1])
    if port <= 0:
        print("Port must be bigger then 0")
        sys.exit(1)
    

    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", port))
    #listening to the server
    s.listen()
    print("Running...")

    clients = []

    while 1:
        try:
            available = select.select ([s] + clients, [], [])[0]
        except ValueError:
            # Sockets may have been closed, check for that
            for client_sock in clients:
                if client_sock.fileno () == -1: client_sock.remove (client_sock) # closed
            continue # Reiterate select

        for client_sock in available:
            # New client?
            if client_sock is s:
                newclient, addr = s.accept ()
                clients.append (newclient)
            # Or an existing client
            else:
                # See if client sent a message
                if len (client_sock.recv (1, socket.MSG_PEEK)) != 0:
                    # client socket has a message
                    ##print ("server" + str (client_sock))
                    new_msg (client_sock)
                else: # Or just disconnected
                    clients.remove (client_sock)
                    clean_client (client_sock)
                    client_sock.close ()
                    break # Reiterate select
                  
if __name__ == "__main__":
	main()
