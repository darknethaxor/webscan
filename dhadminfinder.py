import requests
import threading
import argparse
import os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    lili = '\033[4m'
    wd = "\033[90;1m"  # dark
    GL = "\033[96;1m"  # Blue aqua
    BB = "\033[34;1m"  # Blue light
    YY = "\033[33;1m"  # Yellow light
    GG = "\033[32;1m"  # Green light
    WW = "\033[0;1m"  # White light
    Y = "\033[33;1m"  # Yellow
    G = "\033[32m"  # Green
    W = "\033[0;1m"  # White
    R = "\033[31;1m"  # Red
    C = "\033[36;1m"  # Cyan
    pur = "\033[35m"
    yel = "\033[93m"
    green = "\033[42m"
    orange = "\033[43m"
    orr = '\033[33m'
    OKCYAN = "\033[36m"
    lightblue = '\033[94m'
    CGREENBG2 = '\33[102m'
os.system('clear')
parser = argparse.ArgumentParser()
parser.add_argument("-u", help="target url", dest='target')
parser.add_argument("--path", help="custom path prefix", dest='prefix')
parser.add_argument("--type", help="set the type i.e. html, asp, php", dest='type')
parser.add_argument("--fast", help="uses multithreading", dest='fast', action="store_true")
args = parser.parse_args()

target = args.target
try:
    target = target.replace('https://', '')
except:
    print("error")
    quit()

target = target.replace('http://', '')
target = target.replace('/', '')
target = 'http://' + target
if args.prefix != None:
    target = target + args.prefix
try:
    r = requests.get(target + '/robots.txt')
    if '<html>' in r.text:
        print("\n")
        print (f"{bcolors.OKGREEN}\tWelcome{bcolors.ENDC}\n")
    else:
        print (f"{bcolors.YY}Wait Your Website Admin Pannel Will be Showd Soon{bcolors.ENDC}\n")
except:
    quit()
print(f"{bcolors.C}    ____             __              __        __  __                       {bcolors.ENDC}")
print(f"{bcolors.C}   / __ \____ ______/ /______  ___  / /_      / / / /___ __  ______  _____  {bcolors.ENDC}")
print(f"{bcolors.C}  / / / / __ `/ ___/ //_/ __ \/ _ \/ __/_____/ /_/ / __ `/ |/_/ __ \/ ___/  {bcolors.ENDC}")
print(f"{bcolors.C} / /_/ / /_/ / /  / ,< / / / /  __/ /_/_____/ __  / /_/ />  </ /_/ / /      {bcolors.ENDC}")
print(f"{bcolors.C}/_____/\__,_/_/  /_/|_/_/ /_/\___/\__/     /_/ /_/\__,_/_/|_|\____/_/       {bcolors.ENDC}")
print(f"{bcolors.C}{bcolors.lili}Darknethaxor{bcolors.ENDC}{bcolors.C} {bcolors.lili}Made By Farhan{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}--------------------------------------------------------------------------{bcolors.ENDC}\n")

def scan(links):
    for link in links:
        link = target + link
        r = requests.get(link)
        http = r.status_code
        if http == 200:
            print (f"{bcolors.OKGREEN}[*]Admin Pannel Found: %s{bcolors.ENDC}"% link)
        elif http == 404:
            print(f"{bcolors.BOLD}{bcolors.pur}[-] %s{bcolors.pur}" % link)
        elif http == 302:
            print (f"{bcolors.R} Potential EAR vulnerability found : {bcolors.ENDC}" + link)
        else:
            print (f"{bcolors.OKCYAN}[-] %s{bcolors.OKCYAN}"% link)
paths = [] #list of paths
def get_paths(type):
    try:
        with open('paths.txt','r') as wordlist:
            for path in wordlist:
                path = str(path.replace("\n",""))
                try:
                    if 'asp' in type:
                        if 'html' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'php' in type:
                        if 'asp' in path or 'html' in path:
                            pass
                        else:
                            paths.append(path)
                    if 'html' in type:
                        if 'asp' in path or 'php' in path:
                            pass
                        else:
                            paths.append(path)
                except:
                    paths.append(path)
    except IOError:
        print ('\033[1;31m[-]\033[1;m Wordlist not found!')
        quit()
if args.fast == True:
    type = args.type
    get_paths(type)
    paths1 = paths[:len(paths)/2]
    paths2 = paths[len(paths)/2:]
    def part1():
        links = paths1
        scan(links)
    def part2():
        links = paths2
        scan(links)
    t1 = threading.Thread(target=part1)
    t2 = threading.Thread(target=part2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
else:
    type = args.type
    get_paths(type)
    links = paths
    scan(links)
