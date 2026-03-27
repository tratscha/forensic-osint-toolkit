from geopy.distance import geodesic

def run():
    print("[+] Checking plausibility...")

    points = [
        (51.18202, 6.44958),
        (51.21505, 6.47747),
    ]

    distance = geodesic(points[0], points[1]).km

    print(f"Distance: {distance:.2f} km")

    if distance < 10:
        print("[+] Movement plausible")
    else:
        print("[-] Movement suspicious")