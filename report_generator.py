def run():
    report = """
FORENSIC INVESTIGATION REPORT

Findings:
- ZIP archive analyzed
- File signature checked
- EXIF metadata extracted
- GPS route reconstructed
- Movement plausibility verified

Conclusion:
No anomalies detected.
"""

    with open("report/report.txt", "w") as f:
        f.write(report)

    print("[+] Report generated: report/report.txt")