import requests
import json

# Replace 'YOUR_API_KEY' with your actual NVD API key
API_KEY = 'sk************************'
BASE_URL = 'https://services.nvd.nist.gov/rest/json/cves/1.0'

def get_vulnerabilities(cpe_string):
    url = f'{BASE_URL}?cpeMatchString={cpe_string}&addOns=cves'
    headers = {'User-Agent': 'Your User Agent', 'API_KEY': API_KEY}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return data

def main():
    cpe_string = 'cpe:/o:ubuntu:ubuntu:20.04'  # Example CPE string for Ubuntu 18.04
    vulnerabilities = get_vulnerabilities(cpe_string)

    # Process and analyze the vulnerabilities
    for item in vulnerabilities['result']['CVE_Items']:
        cve_id = item['cve']['CVE_data_meta']['ID']
        cvss_score = item['impact']['baseMetricV2']['cvssV2']['baseScore']
        print(f"CVE ID: {cve_id}, CVSS Score: {cvss_score}")

if __name__ == '__main__':
    main()
