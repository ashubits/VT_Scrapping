from lxml.html import fromstringimport requestsfrom itertools import cycleimport traceback
def get_proxies():    url = 'https://free-proxy-list.net/'    response = requests.get(url)    parser = fromstring(response.text)    proxies = set()    for i in parser.xpath('//tbody/tr')[:10]:        if i.xpath('.//td[7][contains(text(),"yes")]'):            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])            proxies.add(proxy)    return proxies

#If you are copy pasting proxy ips, put in the list belowproxies = ['125.209.94.182:45304', '91.211.107.204:41258', '93.170.113.159:59024', '124.41.240.207:49623', '78.38.227.254:35158', '84.245.103.85:33446', '103.15.242.215:47424']#proxies = get_proxies()proxy_pool = cycle(proxies)i=1url1 = 'https://www.virustotal.com/ui/file_behaviours/'url2 = '_Tencent%20HABO/html'with open('Clean.txt', 'r') as f:    for line in f:        #Get a proxy from the pool        proxy = next(proxy_pool)        print("Request #%d"%i)        print(proxy)        i=i+1        url2.rstrip("\n\r")        url=str(url1 + line + url2)        url=url.replace("\n", "")        file= str('dynamic1/' + line + '.txt')        print(url)        print(file)        response = requests.get(url,proxies={"http": proxy, "https": proxy})        with open(file, 'w') as file:            file.write(r.text)            #print(response.json())        except:            #Most free proxies will often get connection errors. You will have retry    the entire request using another proxy to work.            #We will just skip retries as its beyond the scope of this tutorial and we  are only downloading a single url            print("Skipping. Connnection error")        if 'str' in line:            break
