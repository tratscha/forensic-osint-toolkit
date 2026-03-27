def run(file_path):
    if not file_path:
        print("Provide file")
        return

    with open(file_path, "rb") as f:
        header = f.read(4)

    if header == b'\x50\x4B\x03\x04':
        print("[+] ZIP file detected")
    else:
        print("[-] Unknown file type")