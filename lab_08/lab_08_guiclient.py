
import tkinter as tk
import tkinter.messagebox as tkmsgbox
import tkinter.scrolledtext as tksctxt
import socket

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    
        #-------------------------------------------------------------------
        # row 1: connection stuff (and a clear-messages button)
        #-------------------------------------------------------------------
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")
        #
        self.ipPortLbl = tk.Label(self.groupCon, text='IP:port', padx=10)
        self.ipPortLbl.pack(side="left")
        #
        self.ipPort = tk.Entry(self.groupCon, width=20)
        self.ipPort.insert(tk.END, 'localhost:60003')
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) connect
        self.ipPort.bind('<Return>', connectHandler)
        self.ipPort.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")
        #
        self.connectButton = tk.Button(self.groupCon,
            command = connectButtonClick, width=10)
        self.connectButton.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")
        #
        self.clearButton = tk.Button(self.groupCon, text='clr msg',
            command = clearButtonClick)
        self.clearButton.pack(side="left")

        
        #-------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        #-------------------------------------------------------------------
        self.msgText = tksctxt.ScrolledText(height=15, width=42,
            state=tk.DISABLED)
        self.msgText.pack(side="top")

        
        #-------------------------------------------------------------------
        # row 3: sending messages
        #-------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        #
        self.textInLbl = tk.Label(self.groupSend, text='message', padx=10)
        self.textInLbl.pack(side="left")
        #
        self.textIn = tk.Entry(self.groupSend, width=38)
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) send
        self.textIn.bind('<Return>', sendMessage)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text = 'send',
            command = sendButtonClick)
        self.sendButton.pack(side="left")
        
        
        # set the focus on the IP and Port text field
        self.ipPort.focus_set()

def clearButtonClick():
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.delete(1.0, tk.END)
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

def connectButtonClick():
    # forward to the connect handler
    connectHandler(g_app)

def sendButtonClick():
    # forward to the sendMessage method
    sendMessage(g_app)

# the connectHandler toggles the status between connected/disconnected
def connectHandler(master):
    if g_bConnected:
        disconnect()
    else:
        tryToConnect()

# a utility method to print to the message field        
def printToMessages(message):
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.insert(tk.END, message + '\n')
    # scroll to the end, so the new message is visible at the bottom
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

# if attempt to close the window, it is handled here
def on_closing():
    if g_bConnected:
        if tkmsgbox.askokcancel("Quit",
            "You are still connected. If you quit you will be"
            + " disconnected."):
            myQuit()
    else:
        myQuit()

# when quitting, do it the nice way    
def myQuit():
    disconnect()
    g_root.destroy()

# utility address formatting
def myAddrFormat(addr):
    return '{}:{}'.format(addr[0], addr[1])

# disconnect from server (if connected) and
# set the state of the programm to 'disconnected'

def disconnect():
    global g_bConnected
    global g_sock

    if g_bConnected == True:
        g_bConnected = False
        g_sock.close()
        g_sock = None
    g_app.connectButton['text'] = 'connect'
    
    
# attempt to connect to server    
def tryToConnect():
    # we need to modify the following global variables
    global g_bConnected
    global g_sock

    if g_bConnected:
        printToMessages("youre already connected")

    else:
        g_sock = socket.socket(family= socket.AF_INET,type= socket.SOCK_STREAM)

        try:
            ipaddr = g_app.ipPort.get()
            print(ipaddr)
            ipaddr= ipaddr.split(':')
            g_sock.connect((ipaddr[0],int(ipaddr[1])))
            g_bConnected = True 
            g_app.connectButton['text'] = 'disconnect'
        except:
            printToMessages("faild to connect to {}:{}".format(ipaddr[0],ipaddr[1]))


# attempt to send the message (in the text field g_app.textIn) to the server
def sendMessage(master):

    if g_bConnected:
        try:
            messige = g_app.textIn.get()
            g_sock.sendall(bytearray(messige,'ascii'))
        except:
            printToMessages("could not send")
    else:
        printToMessages("You need to connect to a server first ;)")


# poll messages
def pollMessages():
    g_root.after(g_pollFreq, pollMessages)


    if g_bConnected:
        g_sock.setblocking(False)
        try: 

            data = g_sock.recv(1024)
            printToMessages(data.decode('ascii'))
        except socket.error as error: 
            pass


# by default we are not connected
g_bConnected = False
g_sock = None

# set the delay between two consecutive calls to pollMessages
g_pollFreq = 200 # in milliseconds

# launch the gui
g_root = tk.Tk()
g_app = Application(master=g_root)

# make sure everything is set to the status 'disconnected' at the beginning
disconnect()

# schedule the next call to pollMessages
g_root.after(g_pollFreq, pollMessages)

# if attempt to close the window, handle it in the on-closing method
g_root.protocol("WM_DELETE_WINDOW", on_closing)

# start the main loop
# (which handles the gui and will frequently call pollMessages)
g_app.mainloop()
