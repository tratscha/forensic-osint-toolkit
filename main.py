import argparse
from modules import zip_cracker, file_detector, exif_extractor
from modules import route_analysis, plausibility_check, report_generator

def main():
    parser = argparse.ArgumentParser(description="Forensic OSINT Toolkit")

    parser.add_argument("--mode", required=True,
                        choices=["zip", "detect", "exif", "route", "check", "report"],
                        help="Select tool mode")

    parser.add_argument("--file", help="Input file")

    args = parser.parse_args()

    if args.mode == "zip":
        zip_cracker.run(args.file)

    elif args.mode == "detect":
        file_detector.run(args.file)

    elif args.mode == "exif":
        exif_extractor.run(args.file)

    elif args.mode == "route":
        route_analysis.run()

    elif args.mode == "check":
        plausibility_check.run()

    elif args.mode == "report":
        report_generator.run()

if __name__ == "__main__":
    main()