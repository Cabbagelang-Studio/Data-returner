import socket,time

try:
    with open("config.json","r",encoding="ascii") as file:
        config=eval(file.read())
except:
    print("Using default config...")
    config={"port":22024,"max":5}


def main():
    # ipv4  # tcp-ip
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Listen
    sock.bind(('localhost', config["port"]))
    sock.listen(config["max"])

    print('start listening at %s!'%config["port"])
    while True:
        # Accept request
        conn, addr = sock.accept()
        # Get data
        data = conn.recv(config["port"])

        now=time.localtime()
        print("%s visited at [%s/%s/%s %s:%s:%s]"%(addr[0],now[0],now[1],now[2],now[3],now[4],now[5]))
        
        # Return content
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send(("{'ip':%s,'port':%s}"%(addr[0],addr[1])).encode('utf-8'))
        
        # Close connecting
        conn.close()


if __name__ == '__main__':
    main()
