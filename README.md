# Security Log Anomaly Detector

## Overview
A Python cybersecurity project that analyzes authentication logs and flags repeated failed login attempts. It demonstrates basic security monitoring, log analysis, and rule-based alerting.

## Problem
Repeated failed login attempts may indicate password guessing or another suspicious login pattern. This project uses sample authentication records to identify accounts that may need further investigation.

## Features
- Reads authentication records from a CSV file
- Counts failed login attempts for each username
- Flags usernames with three or more failed attempts
- Uses fictional data for safe testing

## Technologies
- Python
- CSV data processing
- Git and GitHub

## Project Files
- main.py — analyzes login records and prints alerts
- login_logs.csv — fictional sample authentication records

## Requirements
- Python 3

No third-party libraries are required for the current version.

## How to Run
1. Download or clone this repository.
2. Make sure main.py and login_logs.csv are in the same folder.
3. Open a terminal in that folder.
4. Run:

python main.py

## Expected Result
The sample data should trigger an alert for bob because the records contain three failed login attempts for that username.

## Limitations
This is an educational project using a simple rule-based detection method. It does not establish whether an account was compromised, and it is not a production security monitoring system.

## Future Improvements
- Add automated tests
- Analyze login patterns by IP address and time
- Explore machine-learning methods for identifying unusual activity

## Author
Iriza Celia Muyango
