import re
import socket
from email import message_from_string

def extract_sender_ip(header):
    # Regular expression to find IPv4 addresses in the Received header
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    received_headers = re.findall(r'Received: from (.*?)\s*\(.*?([A-Za-z0-9\-\.]+)\)', header)
    
    for (from_host, from_ip) in received_headers:
        match = re.search(ip_pattern, from_ip)
        if match:
            sender_ip = match.group()
            return sender_ip
    return None

def get_location_from_ip(ip):
    try:
        host = socket.gethostbyaddr(ip)
        return host[0]
    except socket.herror:
        return "location"
        

def main():
    email_header = """
    Received: from azam244***@gmail.com () [192.168.1.1])
        by *****gmail.com (Postfix) with ESMTP id ABC123
        for <recipient@gmail.com>; Mon, 13 Aug 2023 10:00:00 -0400 (EDT)
    """
    
    sender_ip = extract_sender_ip(email_header)
    if sender_ip:
        location = get_location_from_ip(sender_ip)
        print(f"Sender's IP address: {sender_ip}")
        print(f"Sender's Location: {location}")
    else:
        print("No sender IP found in header.")

if __name__ == "__main__":
    main()
