import ssl
import socket
import requests
import urllib3
import certifi

urllib3.disable_warnings()

HOST = "www.smailshop.stoer.com"
HTTPS_URL = "https://www.smailshop.stoer.com/.2m/domain"
HTTP_URL  = "http://www.smailshop.stoer.com/.2m/domain"


def check_ssl():
    print("\n[1] SSL CERTIFICATE CHECK")
    try:
        context = ssl.create_default_context()
        with socket.create_connection((HOST, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=HOST) as ssock:
                cert = ssock.getpeercert()
                print("SSL STATUS: OK ✅")
                print("Subject:", cert.get("subject"))
                print("Issuer:", cert.get("issuer"))
                print("Valid From:", cert.get("notBefore"))
                print("Valid Until:", cert.get("notAfter"))
    except Exception as e:
        print("SSL STATUS: FAILED ❌")
        print("Reason:", e)


def bypass_ssl():
    print("\n[2] HTTPS BYPASS (TEST ONLY)")
    try:
        r = requests.get(HTTPS_URL, verify=False, timeout=10)
        print("HTTPS BYPASS OK ✅", r.status_code)
    except Exception as e:
        print("HTTPS FAILED ❌", e)

    print("\nHTTP FALLBACK")
    try:
        r = requests.get(HTTP_URL, timeout=10)
        print("HTTP OK ✅", r.status_code)
    except Exception as e:
        print("HTTP FAILED ❌", e)


def ca_fix():
    print("\n[3] CA STORE FIX (certifi)")
    try:
        r = requests.get(HTTPS_URL, verify=certifi.where(), timeout=10)
        print("CA FIX OK ✅", r.status_code)
    except Exception as e:
        print("CA FIX FAILED ❌", e)


def menu():
    while True:
        print("\n===== SSL RESCUE TOOL =====")
        print("1. Check SSL Certificate")
        print("2. Bypass SSL + HTTP Fallback (TEST)")
        print("3. Fix using certifi CA")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            check_ssl()
        elif choice == "2":
            bypass_ssl()
        elif choice == "3":
            ca_fix()
        elif choice == "0":
            print("Exit.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
