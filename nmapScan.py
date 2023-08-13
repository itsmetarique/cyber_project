import subprocess
import re

def run_nmap_scan(ip_range):
    try:
        nmap_output = subprocess.check_output(['nmap', '-O', ip_range], universal_newlines=True)
        return nmap_output
    except subprocess.CalledProcessError as e:
        print("Error executing Nmap:", e)
        return None

def parse_nmap_output(output):
    devices = {
        'Windows': 0,
        'Linux': 0
    }

    lines = output.split('\n')
    for line in lines:
        if 'Running:' in line:
            if 'Windows' in line:
                devices['Windows'] += 1
            elif 'Linux' in line:
                devices['Linux'] += 1

    return devices

def main():
    #my Ip in range
    ip_range = '192.168.56.1/24'
      # Adjust this to your network's IP range
    nmap_output = run_nmap_scan(ip_range)

    if nmap_output:
        devices = parse_nmap_output(nmap_output)
        print("Windows devices:", devices['Windows'])
        print("Linux devices:", devices['Linux'])

if __name__ == "__main__":
    main()
