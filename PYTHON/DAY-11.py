from datetime import datetime

# Setting two dates
date1 = datetime(2025, 6, 1)
date2 = datetime(2025, 6, 9)

# Subtract to get the difference
diff = date2 - date1
print("Days between:", diff.days)