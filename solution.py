 from socket import *

    def smtp_client(port=1025, mailserver='127.0.0.1'):
        msg = "\r\n My message"
        endmsg = "\r\n.\r\n"

        clientSocket = socket(AF_INET, SOCK_STREAM)

        recv = clientSocket.recv(1024).decode()
    
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv1 = clientSocket.recv(1024).decode()
       
        mailfromCommand = 'MAIL FROM:<a@a.com>\r\n'
        clientSocket.send(mailfromCommand.encode())
        recv1 = clientSocket.recv(1024)
       
        rcpttoCommand = 'RCPT TO:<a@a.com>\r\n'
        clientSocket.send(rcpttoCommand.encode())
        recv1 = clientSocket.recv(1024)
       
        dataCommand = 'DATA\r\n'
 
        clientSocket.send(dataCommand.encode())
        recv1 = clientSocket.recv(1024)

        mailMessageEnd = '\r\n.\r\n'
        message=msg + mailMessageEnd
        clientSocket.send(message.encode())
        recv1 = clientSocket.recv(1024)

        quitCommand = 'QUIT\r\n'

        clientSocket.send(quitCommand.encode())
        recv1 = clientSocket.recv(1024)
        clientSocket.close()

    if __name__ == '__main__':
        smtp_client(1025, '127.0.0.1')