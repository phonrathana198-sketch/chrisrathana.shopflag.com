import requests
import certifi

url = "https://www.smailshop.stoer.com/.2m/domain"

try:
    r = requests.get(url, verify=certifi.where(), timeout=10)
    print("CA FIX OK ✅", r.status_code)
except Exception as e:
    print("CA FIX FAILED ❌", e)
