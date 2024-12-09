safe_ctr = 0
unsafe_ctr = 0

# Open file and split by line
# Each line is a 'report'
with open("input.txt", "r") as file:
    report = [list(map(int, report.split())) for report in file if report.strip()]
    # line.split() splits each line into a list of strings separated by white space
    # map(int, ...) converts each string created by line.split into an int
    # list(map(...)) converts the map object into a list 
    # line.strip() ensures that empty lines are skipped 
    
# Figure out how many reports are unsafe
# Each report has a list of numbers called 'levels' (separated by spaces)
# Read first 'report' into a list
for level in report:
    if len(level) > 1:
        is_increasing = all(x < y for x, y in zip(level, level[1:]))
        is_decreasing = all(x > y for x, y in zip(level,level[1:]))
        safe_iteration = all(abs(x - y) <= 3 for x, y in zip(level, level[1:]))
        # zip() creates pairs of adjacent numbers for comparison
        # all() checks if all adjacent pairs satisfy the condition
        
# To be considered safe...
# Levels must ALL be either increasing or decreasing
# AND
# Any two adjacent levels differ by at least one and at most three
# If levels are all increasing or decreasing... 
# AND if sequential elements are increasing / decreasing by between 1 and 3 (inclusive)
# Report is SAFE
# Add 1 to 'safe_ctr'
# Move onto next report
        if ((is_increasing and safe_iteration) or (is_decreasing and safe_iteration)):
            safe_ctr += 1
# Else, the report is UNSAFE
        else:
            unsafe_ctr += 1
    else:
        unsafe_ctr += 1

print(f"There are: {safe_ctr} safe reports")
print(f"There are: {unsafe_ctr} unsafe reports")

