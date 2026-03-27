# forensic-osint-toolkit
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Focus](https://img.shields.io/badge/Focus-Digital%20Forensics-red)
![OSINT](https://img.shields.io/badge/OSINT-Enabled-orange)
A Python-based toolkit for **Digital Forensics and Open Source Intelligence (OSINT)** investigations.
This project simulates a **real-world forensic investigation workflow**, including password cracking, file validation, metadata extraction, and movement analysis.

---

##  Project Background

This toolkit is based on a **forensic investigation scenario**:

> A set of suspicious files (including images and archives) was recovered from a system.
> The goal is to analyze the data, extract hidden information, and reconstruct user activity.

 **Note:**
Some parts of this project are based on an academic assignment.
Certain assumptions (e.g., password patterns, known formats) are intentionally used to simulate realistic forensic conditions.

---

##  Features

*  **ZIP Password Cracking (Brute Force)**
*  **Hidden File Detection (Magic Numbers)**
*  **EXIF Metadata Extraction**
*  **GPS Geolocation (OSINT)**
*  **Route Reconstruction**
*  **Movement Plausibility Analysis**
*  **Automated Investigation Report**

---

##  Installation

```bash
git clone https://github.com/tratscha/forensic-osint-toolkit.git
cd forensic-osint-toolkit
pip install -r requirements.txt
```

---

##  Usage

###  Crack ZIP Archive

```bash
python main.py --mode zip --file sample.zip
```

 **Important:**

* The brute-force attack assumes a **known password structure**
* This reflects real forensic scenarios where partial information is available

---

###  Detect Hidden File Type

```bash
python main.py --mode detect --file suspicious.bin
```

 Detects real file type using **magic numbers**, even if renamed

---

###  Extract EXIF Metadata

```bash
python main.py --mode exif --file image.jpg
```

 Extracts:

* GPS coordinates
* timestamps
* camera information

---

###  Route Reconstruction

```bash
python main.py --mode route
```

 Displays extracted GPS points
 Simulates movement path

---

###  Plausibility Check

```bash
python main.py --mode check
```

 Calculates distance between locations
 Verifies if movement is realistic

---

###  Generate Report

```bash
python main.py --mode report
```

 Creates:

```
report/report.txt
```

---

##  Investigation Workflow

1. Crack encrypted archive
2. Detect hidden file types
3. Extract metadata from images
4. Identify GPS locations
5. Reconstruct movement path
6. Validate plausibility
7. Generate forensic report

---

##  Assumptions & Limitations

To simulate realistic forensic conditions, the following assumptions are made:

*  Password structure for brute-force attacks is partially known
*  Sample files (ZIP/images) are not included for legal and size reasons
*  GPS data may be hardcoded for demonstration purposes
*  Flask app is a simplified prototype

 These choices are intentional and reflect **controlled forensic analysis scenarios**

---

##  Project Structure

```
modules/
│
├── zip_cracker.py        # Brute-force ZIP password recovery
├── file_detector.py      # File signature (magic number) analysis
├── exif_extractor.py     # Metadata extraction
├── route_analysis.py     # GPS route reconstruction
├── plausibility_check.py # Movement validation
└── report_generator.py   # Report creation
```

---

##  Skills Demonstrated

* Digital Forensics Techniques
* OSINT (Open Source Intelligence)
* Python Development
* Brute-force Attacks
* Metadata Analysis (EXIF)
* Geolocation & Mapping
* Data Validation & Analysis

---

##  Why This Project Matters

This project demonstrates how raw digital evidence can be transformed into actionable insights.

It simulates a real-world forensic workflow:
- Recovering hidden data
- Extracting metadata
- Reconstructing user movement
- Validating behavioral plausibility

 The focus is not just on coding, but on analytical thinking and investigation methodology .


---
##  Future Improvements

- Integrate automatic EXIF → GPS extraction pipeline
- Add interactive map visualization (Leaflet/OpenStreetMap)
- Improve brute-force strategy with wordlists
- Export reports as PDF
---
## Author

Berdigh Mohammed
Student at Hochschule Niederrhein

