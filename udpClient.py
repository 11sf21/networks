import socket

target_host = "127.0.0.1"
target_port = 12000

# create a socket object
# SOCK_DGRAM means UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
# We simply call sendto(), passing in the data and the server we want to
# send the data to. Because UDP is a connectionless protocol, there is no
# call to connect() beforehand.
client.sendto("AAABBAAAABCCC", (target_host, target_port))

# receive some data
# We call recvfrom() to receive UDP data, it returns both the data and
# the details of the remote host and port
data, addr = client.recvfrom(4096)

print data
#print "The address is:", addr
