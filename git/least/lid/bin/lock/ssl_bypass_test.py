import requests
import urllib3

urllib3.disable_warnings()

HTTPS_URL = "https://www.smailshop.stoer.com/.2m/domain"
HTTP_URL  = "http://www.smailshop.stoer.com/.2m/domain"

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
