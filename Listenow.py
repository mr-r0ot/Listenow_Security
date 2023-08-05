from tkinter import *;import socket;Project="Listenow";Version="1.4";root=Tk();root.title(Project)
def send_packet_output(host,port,pyl,recv_size=4096):
    host=(host.get())
    port=(port.get())
    pyl=(pyl.get("1.0", END))
    try:
        host=(socket.gethostbyname(host))
    except:
        pass
    host=(str(host))
    port=(int(port))
    pyl=(str(pyl))
    try:
        server_addres = (host,port)
        clint_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clint_socket.connect(server_addres)
        clint_socket.send(pyl.encode())
        respons = clint_socket.recv(recv_size)
        respons = (respons.decode())
        clint_socket.close()
    except:
        respons="Time Out."    
    r = Tk()
    r.title(f"Respons host:{host} port:{port}")
    Label(r, text=f"Respons host:{host} port:{port}", fg='black', font=('arial', 9, 'bold')).pack()
    za = Text(r)
    za.insert(END, respons)
    za.pack()
    r.mainloop()
Label(root, text=f"Listenow ({Version}) NICOLA", fg='red', font=('arial', 11, 'bold')).pack();Label(root, text="Host", fg='black', font=('arial', 9, 'bold')).pack()
host = Entry(root, highlightthickness=20, font=('arial', 10, 'bold'))
host.pack();Label(root, text="Port", fg='black', font=('arial', 9, 'bold')).pack()
port = Entry(root, highlightthickness=20, font=('arial', 10, 'bold'))
port.pack();pyl = Text(root)
pyl.insert(END, """
GET / HTTP/1.1
""")
pyl.pack();Button(root, padx=12, pady=8, bd=8, fg='black', font=('arial', 9, 'bold'),text="Send",command=lambda:send_packet_output(host,port,pyl,recv_size=4096)).pack();root.mainloop(
