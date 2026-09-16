from collections import Counter
from pathlib import Path
import re

log_file = Path("logs/auth.log")

failed_ips = Counter()
successful_logins = 0
failed_logins = 0

with log_file.open("r", errors="ignore") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1

            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if match:
                ip_address = match.group(1)
                failed_ips[ip_address] += 1

        elif "Accepted password" in line:
            successful_logins += 1

print("===== SIEM Security Log Report =====")
print(f"Total failed logins: {failed_logins}")
print(f"Total successful logins: {successful_logins}")

print("\nFailed login attempts by IP:")

for ip, count in failed_ips.items():
    print(f"{ip}: {count} attempts")

print("\nSecurity Assessment:")

for ip, count in failed_ips.items():
    if count >= 3:
        print(f"[HIGH] Possible brute-force activity from {ip}")
    elif count >= 2:
        print(f"[MEDIUM] Multiple failed logins from {ip}")
    else:
        print(f"[LOW] Single failed login from {ip}")
