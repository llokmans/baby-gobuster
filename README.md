# baby-gobuster

A directory and file brute-forcer for web reconnaissance, inspired by gobuster and written from scratch in Python.

## What it does

1. Takes a target URL and a wordlist from the command line.
2. Requests `<url>/<word>` for every word in the list.
3. Prints each result colour-coded: **200** found (green), **403** forbidden but exists (yellow), anything else (red).
4. Counts the paths that exist and writes a timestamped `report.html` listing them.

A 403 counts as a hit on purpose: the server is admitting the path is there, it just won't let you in.

## Tech

Python · requests · argparse · colorama · datetime

## Run it

```
pip install requests colorama
python recon.py -u http://target.local -w wordlist.txt
```

| Flag | Meaning |
| --- | --- |
| `-u`, `--url` | Target URL (required) |
| `-w`, `--wordlist` | Path to the wordlist |

## Next steps

- Threading, so requests run in parallel instead of one at a time
- A timeout and error handling for unreachable hosts

> Only run this against systems you own or have written permission to test.
