import socket

print("Name : Yudha Primadiansyah")
print("Student ID : 1301218697")
print("Welcome to My Port Scanner")
host = input("Please input your target IP : ")
print("TCP Port Scanning FROM 1 TO 65535")
start = 1
end = 65535
for port in range(1, 65535):
    print("Checking Host {0} On Port : {1}".format(host,port))
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cek = c.connect_ex((host,port))
        if(cek == 0):
            print("\033[1;32;40m Host {0} Has Open Port : {1} \033[0m".format(host,port))
        c.close()
    except:
         print("Host {0} Has No Port : {1}".format(host,port))