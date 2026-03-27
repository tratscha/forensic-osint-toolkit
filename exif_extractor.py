import exifread

def run(file_path):
    if not file_path:
        print("Provide image file")
        return

    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)

    print("\n[+] EXIF DATA:")
    for tag in tags:
        print(f"{tag}: {tags[tag]}")