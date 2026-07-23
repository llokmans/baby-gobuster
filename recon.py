import argparse
import requests
parser = argparse.ArgumentParser(description='Web Reconnaissance Tool')
parser.add_argument('-u', '--url', required=True, help='Target URL for reconnaissance')
parser.add_argument('-w', '--wordlist', help='Path to the wordlist for directory and file enumeration')

args = parser.parse_args()

with open(args.wordlist, 'r') as file:
    wordlist = [line.strip() for line in file]

for word in wordlist:
    full_url = f"{args.url}/{word}"
    response = requests.get(full_url)
    print(f"[{response.status_code}] {full_url}")


