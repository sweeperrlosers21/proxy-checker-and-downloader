# 💀 SWEEPER OF LOSERS - Ultimate Proxy Hunter 🧹

<div align="center">

```
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
```

**⚡ The Ultimate High-Speed Proxy Scraper & Validator ⚡**

*Separating the LIVE from the DEAD since 2025* 

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-REAPING-red.svg)
![Developed By](https://img.shields.io/badge/developed%20by-Sweeper%20of%20Losers%2021-purple.svg)

</div>

---

## 🎯 What is This?

**SWEEPER OF LOSERS** is a ruthless, high-performance proxy scraper and validator that hunts down proxies from multiple sources and separates the **LIVE** ones from the **DEAD** ones. No mercy for slow or broken proxies!

### ⚡ Key Features:
- 🔥 **Lightning Fast**: 1000+ concurrent connections
- 🎯 **Multi-Source Hunting**: Scrapes from 20+ proxy sources
- 💓 **Live/Dead Detection**: Instantly identifies working proxies
- 🧹 **Zero Tolerance**: Eliminates dead proxies without mercy
- 📊 **Real-time Progress**: Beautiful progress bars and live counters
- 💀 **Dramatic Interface**: Intimidating ASCII art and death-themed UI

---

## 🚀 Quick Start

### Prerequisites
```bash
python 3.7+
pip install aiohttp aiofiles tqdm
```

### Installation & Usage
```bash
# Clone the repository
git clone https://github.com/yourusername/sweeper-of-losers.git
cd sweeper-of-losers

# Install dependencies
pip install -r requirements.txt

# Start the hunt
python proxy_hunter.py
```

### Output
- **Live proxies** saved to `good_proxies.txt`
- **Real-time statistics** in terminal
- **Dramatic progress tracking** with emojis

---

## 🎮 How It Works

1. **🔍 HUNTING PHASE**: Scrapes proxies from 20+ sources simultaneously
2. **⚔️ BATTLE PHASE**: Tests each proxy with 1000+ concurrent connections  
3. **💓 LIFE CHECK**: Validates proxies against `httpbin.org/ip`
4. **🧹 REAPING PHASE**: Eliminates dead proxies, saves the survivors
5. **🏆 VICTORY**: Displays final count of LIVE vs DEAD

### Performance Stats:
- **Concurrency**: 1000 simultaneous checks
- **Timeout**: 3 seconds (no mercy for slow ones)
- **Retry Logic**: 2 attempts maximum
- **Sources**: HTTP, SOCKS4, SOCKS5 protocols

---

## 📋 Proxy Sources

The reaper hunts from these victim pools:

### HTTP Sources:
- TheSpeedX/PROXY-List
- clarketm/proxy-list  
- monosans/proxy-list
- UptimerBot/proxy-list
- ShiftyTR/Proxy-List
- mmpx12/proxy-list
- roosterkid/openproxylist
- And 8+ more sources...

### API Sources:
- ProxyScrape API
- Proxy-List Download API

### SOCKS Sources:
- SOCKS4 & SOCKS5 from multiple repositories

---

## ⚙️ Configuration

Edit these constants in the script:

```python
CONCURRENCY = 1000    # Concurrent connections (higher = faster)
TIMEOUT = 3           # Timeout per proxy check (seconds)  
MAX_RETRIES = 2       # Retry attempts for failed proxies
OUTPUT_FILE = 'good_proxies.txt'  # Output filename
```

---

## 💀 Sample Output

```
💀 SWEEPER OF LOSERS - ULTIMATE PROXY HUNTER 💀
Scrapes proxies from multiple sources and eliminates the dead ones
Sources: 21 | Concurrency: 1000 | Timeout: 3s
Hunt started at: 2025-01-15 14:30:22
🧹 Time to separate LIVE from DEAD! 🧹

[+] 🔍 Hunting proxies from 21 sources...
[✓] 🎯   847 potential victims from raw.githubusercontent.com
[✓] 🎯   1205 potential victims from api.proxyscrape.com

[+] 🎯 Total potential victims: 12,847

[+] 🧹 Time to separate 12,847 proxies into LIVE and DEAD...
☠️ Reaping the dead: 100%|████████████| 12847/12847 [02:15<00:00, 94.8it/s] 💓 LIVE: 342

[✓] 💓 342 proxies are ALIVE! Saved to good_proxies.txt
🧹 Sweep completed at: 2025-01-15 14:32:37
☠️ The DEAD ones have been eliminated! ☠️
```

---

## 📊 Statistics

Typical performance metrics:
- **Scraping Speed**: ~5-10 seconds for all sources
- **Checking Speed**: ~50-100 proxies per second
- **Success Rate**: 2-5% (most proxies are dead)
- **Memory Usage**: <100MB RAM
- **CPU Usage**: High during checking phase

---

## 🛠️ Advanced Usage

### Custom Proxy Sources
Add your own sources to the `PROXY_SOURCES` list:
```python
PROXY_SOURCES.append('https://your-custom-proxy-source.com/proxies.txt')
```

### Different Output Formats
Modify the `save_proxies()` function for custom output formats (JSON, CSV, etc.)

### Integration
Use the results in your applications:
```python
with open('good_proxies.txt', 'r') as f:
    live_proxies = [line.strip() for line in f.readlines()]
```

---

## 🤝 Contributing

Want to make the reaper more deadly? Contributions welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/MoreDeadlyReaping`)
3. Commit changes (`git commit -m 'Add feature: More deadly reaping'`)
4. Push to branch (`git push origin feature/MoreDeadlyReaping`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This tool is for educational and testing purposes only. The developer (**Sweeper of Losers 21**) is not responsible for any misuse. Use proxies responsibly and respect websites' terms of service.

**Note**: Many free proxies are unstable or malicious. Always verify proxy sources and use with caution.

---

## 📜 License

```
MIT License - Feel free to reap and sow as you wish
```

---

## 👑 Developed By

**🧹 SWEEPER OF LOSERS 21 🧹**

*"In a world full of dead proxies, be the reaper."*

---

<div align="center">

**⭐ Star this repository if you survived the reaping! ⭐**

**🔗 Repository: https://github.com/sweeperrlosers21/proxy-checker-and-downloader**

**💀 Remember: Only the LIVE deserve to survive 💀**

*Last updated: January 2025*

</div>
