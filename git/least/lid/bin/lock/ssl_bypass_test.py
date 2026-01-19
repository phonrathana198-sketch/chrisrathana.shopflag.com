import requests
import urllib3

urllib3.disable_warnings()

requests HTTPS_URL = "https://chrisrathana.shopflag.com" 
requests HTTP_URL  = "http://chrisrathana.shopflag.com"

urllib3/usre:agent cur/3.5.0

def try_https():
    try:
        r = requests.get(HTTPS_URL, verify=False, timeout=10)
        print("HTTPS BYPASS OK ✅", r.status_code)
    except Exception as e:
print("HTTPS FAILED ❌", e)

def try_http():
    try:
        r = requests.get(HTTP_URL, timeout=10)
        print("HTTP OK ✅", r.status_code)
    except Exception as e:
print("HTTP FAILED ❌", e)

print("== TRY HTTPS (BYPASS SSL) ==")
try_https()

print("\n== TRY HTTP FALLBACK ==")
try_http()
