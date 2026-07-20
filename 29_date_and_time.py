# Date and Time Handling in Python

from datetime import datetime, date, time, timedelta
import time as time_module

print("=== Date and Time Handling in Python - Enhanced ===\n")

# 1. Current Date and Time
print("=== 1. Current Date & Time ===")
now = datetime.now()
print(f"Current datetime : {now}")
print(f"Current date     : {date.today()}")
print(f"Current time     : {datetime.now().time()}")

# Formatted output
print(f"Formatted        : {now.strftime('%A, %B %d, %Y %I:%M %p')}")

# 2. Creating Specific Dates
print("\n=== 2. Creating Dates ===")
birthday = date(1995, 7, 20)
print(f"Birthday         : {birthday}")
print(f"Day of week      : {birthday.strftime('%A')}")

dt = datetime(2025, 12, 25, 10, 30, 0)
print(f"Christmas 2025   : {dt}")

# 3. Time Delta (Duration)
print("\n=== 3. Time Delta ===")
future = now + timedelta(days=30)
print(f"30 days from now : {future}")

past = now - timedelta(weeks=2, hours=5)
print(f"2 weeks 5 hours ago: {past}")

delta = future - now
print(f"Days until future: {delta.days}")

# 4. Parsing Strings to Dates
print("\n=== 4. Parsing Dates from Strings ===")
date_str1 = "2025-07-20"
date_str2 = "December 25, 2025"

parsed1 = datetime.strptime(date_str1, "%Y-%m-%d")
parsed2 = datetime.strptime(date_str2, "%B %d, %Y")

print(f"Parsed 1: {parsed1}")
print(f"Parsed 2: {parsed2.date()}")

# 5. Time Module (Unix time, delays)
print("\n=== 5. Time Module ===")
print(f"Current Unix timestamp: {int(time_module.time())}")

print("Sleeping for 1 second...")
time_module.sleep(1)
print("Awake now!")

# 6. Timezone Awareness (Basic)
print("\n=== 6. Timezone Handling ===")
from datetime import timezone

utc_now = datetime.now(timezone.utc)
print(f"UTC time         : {utc_now}")

# 7. Best Practices
print("\n=== Best Practices ===")
print("""
1. Always use datetime module for dates
2. Prefer datetime over date when time matters
3. Use timezone-aware objects for production
4. Store dates in UTC, convert for display
5. Use strftime for formatting, strptime for parsing
6. Consider pendulum or arrow libraries for complex needs
""")

print("\n=== Proper date/time handling is crucial for logs, scheduling, and data analysis! ===")