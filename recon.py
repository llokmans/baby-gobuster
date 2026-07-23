import argparse #importing the argparse when we want the python script to accept inputs from the terminal.
import requests
import datetime
from colorama import Fore, Style
parser = argparse.ArgumentParser(description='Web Reconnaissance Tool') # we create the container first and then we add the arguments that we want to accept from the terminal.

# we then define the arguments that we want to accept from the terminal. In this case, we want to accept a URL and a wordlist.
parser.add_argument('-u', '--url', required=True, help='Target URL for reconnaissance') 
parser.add_argument('-w', '--wordlist', help='Path to the wordlist for directory and file enumeration')
target_url = parser.parse_args().url
scan_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current date and time for the report
# read the arguments from the terminal and store them in a variable called args.
args = parser.parse_args()

# we then read the wordlist file and store the words in a list called wordlist.
with open(args.wordlist, 'r') as file:
    wordlist = [line.strip() for line in file]
counter = 0 # pyright: ignore[reportUndefinedVariable]

results = []



# we then loop through the wordlist and make a request to the target URL with each word in the wordlist.
for word in wordlist:
    
    full_url = f"{args.url}/{word}"
    response = requests.get(full_url)
    if response.status_code == 200:
        counter += 1
        print(f"{Fore.GREEN}[{response.status_code}] {full_url}{Style.RESET_ALL}")
        results.append((response.status_code, full_url))
    elif response.status_code == 403:
        counter += 1
        print(f"{Fore.YELLOW}[{response.status_code}] {full_url} - Forbidden{Style.RESET_ALL}")
        results.append((response.status_code, full_url))
    else:
        print(f"{Fore.RED}[{response.status_code}] {full_url}{Style.RESET_ALL}")
        
        
print(f"\nScan Complete. Found {counter} accessible paths.")


with open("report.html", "w") as report_file:
    report_file.write("<html>\n<head>\n<title>Reconnaissance Report</title>\n")
    report_file.write("<style>\n")
    report_file.write("  body { background-color: #0f141c; color: #e1e4e8; font-family: 'Courier New', monospace; padding: 25px; }\n")
    report_file.write("  .header { border-bottom: 2px dashed #28a745; padding-bottom: 15px; margin-bottom: 20px; }\n")
    report_file.write("  h1 { color: #28a745; font-size: 22px; margin: 0 0 10px 0; }\n")
    report_file.write("  .meta { color: #79c0ff; font-size: 14px; margin-bottom: 5px; }\n")
    report_file.write("  ul { list-style-type: none; padding: 0; }\n")
    report_file.write("  li { margin: 8px 0; color: #85e89d; }\n") # Green prefix
    report_file.write("  .path { color: #ffea00; font-weight: bold; }\n") # Yellow paths
    report_file.write("</style>\n</head>\n<body>\n")
    

    report_file.write("  <div class='header'>\n")
    report_file.write("    <h1>[+] RECONNAISSANCE REPORT</h1>\n")
    report_file.write(f"    <div class='meta'><b>TARGET:</b> {target_url}</div>\n")
    report_file.write(f"    <div class='meta'><b>DATE:</b> {scan_date}</div>\n")
    report_file.write("  </div>\n")
    
    
    report_file.write("  <h2>[i] Discovered Paths:</h2>\n  <ul>\n")
    for result in results:
        report_file.write(f"    <li>[{result[0]}] {result[1]}</li>\n")
    report_file.write("  </ul>\n")
    
   
    
    report_file.write("</body>\n</html>")