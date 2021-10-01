from socket import *
import ssl
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
   
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end
    recv = clientSocket.recv(1024).decode()
    #    print(recv)
    # #
    if recv[:3] != '220':
      print('220 reply not received from server.')
   
    ssl_version=ssl.PROTOCOL_SSLv23
    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    if recv1[:3] != '250':
      print('250 reply not received from server.')

    mailFromCommand = 'MAIL FROM: TEST1\r\n'
    clientSocket.send(mailFromCommand.encode())
    startTlsCommand = 'STARTTLS\r\n'
    recv2 = clientSocket.recv(1024).decode()
 
    if recv2[:3] != '250':
      print('250 reply not received from server.')

    rcptToCommand = 'RCPT TO: TEST2\r\n'
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()

    if recv4[:3] != '354':
      print('354 reply not received from server.')

    clientSocket.send(msg.encode())
 
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()

    if recv5[:3] != '250':
      print('250 reply not received from server.')

    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
  
if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
