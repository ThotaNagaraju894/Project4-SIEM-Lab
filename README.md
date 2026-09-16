## Incident Response Recommendations

### Alert 1: Possible Brute-Force Activity

Source IP: 192.168.1.50  
Severity: HIGH

Recommended actions:

1. Investigate the source IP address.
2. Review the related authentication logs.
3. Check whether any login was successful after repeated failures.
4. Temporarily block the suspicious IP if confirmed malicious.
5. Reset affected user passwords if necessary.
6. Continue monitoring for additional login attempts.

### Alert 2: Multiple Failed Logins

Source IP: 192.168.1.60  
Severity: MEDIUM

Recommended actions:

1. Review the failed login events.
2. Confirm whether the attempts target the root account.
3. Check the time and frequency of the attempts.
4. Investigate the source system.
5. Monitor for repeated activity.

## SIEM Workflow

```text
Log Collection
      ↓
Log Analysis
      ↓
Suspicious Activity Detection
      ↓
Alert Severity Classification
      ↓
Incident Investigation
      ↓
Response Recommendations

