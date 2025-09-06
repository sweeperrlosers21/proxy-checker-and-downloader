import asyncio
import aiohttp
import aiofiles
from tqdm.asyncio import tqdm_asyncio
from datetime import datetime
import textwrap
import sys
import socket
import random
import time

# Constants
OUTPUT_FILE = 'good_proxies.txt'
CONCURRENCY = 1000  # Higher concurrency for faster checking
TIMEOUT = 3  # Reduced timeout for faster checks
MAX_RETRIES = 2  # Retry failed checks
good_proxies = []

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ASCII Art Animation
def show_sweeper_animation():
    frames = [
        r"""
   ███████ ██     ██ ███████ ███████ ██████  ███████ ██████  
   ██      ██     ██ ██      ██      ██   ██ ██      ██   ██ 
   ███████ ██  █  ██ █████   █████   ██████  █████   ██████  
        ██ ██ ███ ██ ██      ██      ██      ██      ██   ██ 
   ███████  ███ ███  ███████ ███████ ██      ███████ ██   ██ 
   """,
        r"""
   ███████ ██     ██ ███████ ███████ ██████  ███████ ██████  
   ██      ██     ██ ██      ██      ██   ██ ██      ██   ██ 
   ███████ ██  █  ██ █████   █████   ██████  █████   ██████  
        ██ ██ ███ ██ ██      ██      ██      ██      ██   ██ 
   ███████  ███ ███  ███████ ███████ ██      ███████ ██   ██ 
                                  
        ██████  ███████                                      
       ██    ██ ██                                           
       ██    ██ █████                                        
       ██    ██ ██                                           
        ██████  ██                                           
   """,
        r"""
   ███████ ██     ██ ███████ ███████ ██████  ███████ ██████  
   ██      ██     ██ ██      ██      ██   ██ ██      ██   ██ 
   ███████ ██  █  ██ █████   █████   ██████  █████   ██████  
        ██ ██ ███ ██ ██      ██      ██      ██      ██   ██ 
   ███████  ███ ███  ███████ ███████ ██      ███████ ██   ██ 
                                  
        ██████  ███████                                      
       ██    ██ ██                                           
       ██    ██ █████                                        
       ██    ██ ██                                           
        ██████  ██                                           
                                  
       ██       ██████  ███████ ███████ ██████  ███████ ██ 
       ██      ██    ██ ██      ██      ██   ██ ██      ██ 
       ██      ██    ██ ███████ █████   ██████  ███████ ██ 
       ██      ██    ██      ██ ██      ██   ██      ██    
       ███████  ██████  ███████ ███████ ██   ██ ███████ ██ 
   """
    ]
    
    print(f"{Colors.HEADER}{Colors.BOLD}")
    for i, frame in enumerate(frames):
        print("\033[2J\033[H")  # Clear screen
        print(frame)
        if i == 0:
            print(f"{Colors.WARNING}                    🧹 INITIALIZING... 🧹{Colors.ENDC}")
        elif i == 1:
            print(f"{Colors.WARNING}                    🧹 SWEEPING... 🧹{Colors.ENDC}")
        elif i == 2:
            print(f"{Colors.FAIL}                    💀 READY TO SWEEP! 💀{Colors.ENDC}")
        time.sleep(1.0)
    print(f"{Colors.ENDC}")
    time.sleep(0.5)

# Proxy sources (HTTP, SOCKS4, SOCKS5)
PROXY_SOURCES = [
    # HTTP
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/http.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http.txt',
    'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    # API plain
    'https://api.proxyscrape.com/v2/?request=get&protocol=http&timeout=1000&country=all',
    'https://www.proxy-list.download/api/v1/get?type=http',
    # SOCKS4
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
    # SOCKS5
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
]

def print_banner():
    banner = f"""
    {Colors.HEADER}{'*' * 70}
    {Colors.BOLD}💀 SWEEPER OF LOSERS - ULTIMATE PROXY HUNTER 💀{Colors.ENDC}
    {Colors.OKBLUE}Scrapes proxies from multiple sources and eliminates the weak ones
    {Colors.OKGREEN}Sources: {len(PROXY_SOURCES)} | Concurrency: {CONCURRENCY} | Timeout: {TIMEOUT}s
    {Colors.WARNING}Hunt started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    {Colors.FAIL}🧹 Time to separate winners from LOSERS! 🧹
    {'*' * 70}{Colors.ENDC}
    """
    print(textwrap.dedent(banner))

async def fetch_with_retry(session, url, retries=2):
    last_error = None
    for attempt in range(retries):
        try:
            async with session.get(url, timeout=15) as response:
                if response.status == 200:
                    return await response.text()
                raise Exception(f"HTTP {response.status}")
        except Exception as e:
            last_error = e
            if attempt < retries - 1:
                await asyncio.sleep(1)
    return last_error

async def scrape_proxies():
    proxies = []
    print(f"{Colors.OKBLUE}[+] 🔍 Hunting proxies from {len(PROXY_SOURCES)} sources...{Colors.ENDC}")
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in PROXY_SOURCES:
            tasks.append(fetch_with_retry(session, url))
        
        results = await tqdm_asyncio.gather(
            *tasks, 
            desc=f"{Colors.OKBLUE}🔍 Hunting{Colors.ENDC}", 
            unit="source",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"
        )
        
        for url, result in zip(PROXY_SOURCES, results):
            if isinstance(result, Exception):
                domain = url.split('/')[2] if len(url.split('/')) > 2 else url
                print(f"{Colors.WARNING}[!] 💀 {domain} is a LOSER: {str(result)[:70]}{Colors.ENDC}")
                continue
                
            try:
                lines = [p.strip() for p in result.splitlines() if ':' in p]
                proxies.extend(lines)
                domain = url.split('/')[2] if len(url.split('/')) > 2 else url
                print(f"{Colors.OKGREEN}[✓] 🎯 {len(lines):<5} potential targets from {domain}{Colors.ENDC}")
            except Exception as e:
                print(f"{Colors.FAIL}[!] 💀 Error processing {url.split('/')[2]}: {str(e)[:50]}{Colors.ENDC}")
    
    proxies = list(set(proxies))  # Remove duplicates
    print(f"\n{Colors.BOLD}{Colors.OKGREEN}[+] 🎯 Total hunting targets: {len(proxies)}{Colors.ENDC}\n")
    return proxies

async def check_proxy(proxy, sem, pbar):
    for _ in range(MAX_RETRIES):
        try:
            async with sem:
                async with aiohttp.ClientSession(
                    connector=aiohttp.TCPConnector(ssl=False, limit=0),
                    timeout=aiohttp.ClientTimeout(total=TIMEOUT)
                ) as session:
                    async with session.get(
                        'http://httpbin.org/ip',
                        proxy=f'http://{proxy}'
                    ) as resp:
                        if resp.status == 200:
                            good_proxies.append(proxy)
                            pbar.set_postfix_str(f"{Colors.OKGREEN}Live: {len(good_proxies)}{Colors.ENDC}")
                            return
        except (aiohttp.ClientError, asyncio.TimeoutError, socket.gaierror):
            continue
    pbar.update()

async def save_proxies():
    async with aiofiles.open(OUTPUT_FILE, 'w') as f:
        await f.write('\n'.join(good_proxies))
    
    print(f"\n{Colors.BOLD}{Colors.OKGREEN}[✓] 🏆 {len(good_proxies)} WINNERS survived the sweep! Saved to {OUTPUT_FILE}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}🧹 Sweep completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.ENDC}")
    print(f"{Colors.FAIL}💀 The LOSERS have been eliminated! 💀{Colors.ENDC}")

async def main():
    show_sweeper_animation()
    print_banner()
    
    try:
        proxies = await scrape_proxies()
        if not proxies:
            print(f"{Colors.FAIL}[!] 💀 No proxies found - all sources are LOSERS!{Colors.ENDC}")
            return

        sem = asyncio.Semaphore(CONCURRENCY)
        print(f"{Colors.OKBLUE}[+] 🧹 Time to separate {len(proxies)} proxies into LIVE and DEAD...{Colors.ENDC}")

        with tqdm_asyncio(total=len(proxies), 
                        desc=f"{Colors.OKBLUE}☠️  Reaping the dead{Colors.ENDC}", 
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]") as pbar:
            tasks = [check_proxy(p, sem, pbar) for p in proxies]
            await asyncio.gather(*tasks)

        await save_proxies()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[!] 🛑 Sweep interrupted by user{Colors.ENDC}")
        if good_proxies:
            await save_proxies()
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.FAIL}[!] 💀 Fatal error: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())
