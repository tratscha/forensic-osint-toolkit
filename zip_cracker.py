import zipfile
import itertools
import string

def run(zip_path):
    if not zip_path:
        print("Provide zip file")
        return

    print("[+] Starting brute-force attack...")

    chars = string.ascii_lowercase + string.digits

    for length in range(3, 6):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)

            try:
                with zipfile.ZipFile(zip_path) as zf:
                    zf.extractall(pwd=password.encode())
                    print(f"[+] Password found: {password}")
                    return
            except:
                pass

    print("[-] Password not found")