import csv
from collections import defaultdict

def analyze_login_logs(filename):
    failed_attempts = defaultdict(int)

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["status"].lower() == "failed":
                failed_attempts[row["username"]] += 1

    print("=== Login Security Report ===")

    if not failed_attempts:
        print("No failed login attempts found.")
        return

    for username, attempts in failed_attempts.items():
        if attempts >= 3:
            print(
                f"ALERT: {username} had "
                f"{attempts} failed login attempts."
            )

if __name__ == "__main__":
    analyze_login_logs("login_logs.csv")
