
import requests, sys

def request(url):
   try:
     return requests.get("http://" + url)
   except requests.exceptions.ConnectionError:
      pass


target_url = str(sys.argv[1]) 

with open("file_and_dir_wordlist.txt", "r") as wordlist:
   for line in wordlist:
      word = line.strip()
      test_url = target_url + "/" + word
      response = request(test_url)
      if response:
         print("[+] Subdomain discovered --> " + test_url)