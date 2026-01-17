import ssl
import socket
from datetime import datetime

HOST = "www.smailshop.stoer.com"
PORT = 443

print("Checking SSL for:", HOST)
print("-" * 40)

try:
    context = ssl.create_default_context()
    with socket.create_connection((HOST, PORT), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            cert = ssock.getpeercert()
            print("SSL STATUS: OK ✅")
            print("Issued To:", cert.get("subject"))
            print("Issuer:", cert.get("issuer"))
            print("Valid From:", cert.get("notBefore"))
            print("Valid Until:", cert.get("notAfter"))
except Exception as e:
    print("SSL STATUS: FAILED ❌")
    print("Reason:", e)
