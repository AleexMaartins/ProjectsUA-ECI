import socket
import json
import sys
from common_comm import send_dict, recv_dict, sendrecv_dict

list=[]

def start(s, client_id):
    start_request = { "op": "START", "client_id": client_id }
    msg = sendrecv_dict(s, start_request)

    if(msg['status']== False):
        print(msg['error'])
        sys.exit(0)
    print("Server started successfully")
    return None
    
def number(s,number):
    number_request = { "op": "NUMBER", "number": number }
    response = sendrecv_dict (s, number_request)

    if(response['status']== False):
        print(response['error'] + " Make sure to start the client first")
        return None
    
    print("Number added successfully")
    return None

def stop(s):
    stop_request = { "op": "STOP" }
    response = sendrecv_dict (s, stop_request)

    if(response['op']== "STOP"): 
        if(response['status']== False):
            msg = response['error']
            if(msg == "Inexistent Client"):
                print(msg + " Make sure to start the client first\n" )
            if(msg == "Insuficient Data"):
                print(msg + " Make sure to add numbers first" )
            return None
        else:
            print("list: " + str(list) +", min: " + str(response['min']) + ", max: " + str(response['max']))
            sys.exit(0)

def quit(s):
    quit_request = { "op": "QUIT" }
    response = sendrecv_dict (s, quit_request)
    
    if(response['status']== False):
        print(response['error'] + " Make sure to start the client first")
        return None
    
    print("Client quitted successfully")
    s.close()
    sys.exit(0)
    
 

def run_client(client_id, port, host):
    #create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to server
    s.connect ((host, port))
    start(s, client_id)
    print("Operations: STOP/QUIT\n")    
    while 1:
        op = str(input("Add number-> ")).upper()
        if op == "STOP":
            stop(s)
        elif op == "QUIT":
            quit(s)
        else:
            #we're using try-except because, in case of "op" not beeing int the program would crash
            try:
                op = int(op)
                list.append(op)
                number(s,op)
            except:
                print("Input a legit operation")
                continue
            

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Error.Wrong number of arguments.")
        print("Use: python3 client.py <client id> <port> [machine]")
        sys.exit(1)

    client_id = sys.argv[1]
    port = int(sys.argv[2])

    
    if port <= 0:
        print("Port must be bigger then 0")
        sys.exit(1)
    
    host = "localhost"
    if len(sys.argv) == 4:
        host = sys.argv[3]
        if not valid_ip(host):
            print("Invalid ip")
            sys.exit(1)


    run_client(client_id, port, host)
    sys.exit(0)
if __name__ == "__main__":
	main()



"""
fazer start logo ao inicio
lista, min e max no stop
nao é suposto dar 2 stop
fazer clean_client no stop e quit
update no report.csv com cada stop ao inves de apagar
"""