import socket
import ssl

def create_ssl_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Wrap the socket with SSL/TLS encryption
    ssl_socket = ssl.wrap_socket(client_socket, ssl_version=ssl.PROTOCOL_TLS)
    return ssl_socket

def main():
    target_host = '32.57.446.**'
    target_port = 443  # HTTPS port
    
    ssl_socket = create_ssl_socket(target_host, target_port)
    
    # Now you can use 'ssl_socket' to send and receive encrypted data
    
    ssl_socket.close()

if __name__ == '__main__':
    main()
