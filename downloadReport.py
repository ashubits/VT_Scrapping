import sys
import requests
from bs4 import BeautifulSoup
from random import choice

def get_proxy():
    url = 'https://www.sslproxies.org'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x:x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),map(lambda x:x.text, soup.findAll('td')[1::8]))))))}

argumentList = sys.argv
print(get_proxy())

#sha ='cada2cc33ac6a579520d7abd7aeb8a3d66e37b20b96679a20916f1367ad160a9'
print (argumentList)
with open('Malware.txt', 'r') as f:
    for sha in f:
        sha=sha.rstrip()
        print(sha)
        if 'str' in sha:
           break
        a=1
        while a:
            try:
                url = str('https://www.virustotal.com/ui/file_behaviours/' + sha +  '_Tencent%20HABO/html')
                proxy = get_proxy()
                print (proxy)
                print (url)
                r = requests.get(url, proxies=proxy, timeout=5, allow_redirects=True)
                a=0
                break
            except:
                pass
        outfile= str('dynamic/' + sha)
        open(outfile, 'wb').write(r.content)

f.close()
