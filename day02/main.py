safe_ctr = 0                        # Number of safe reports
unsafe_ctr = 0                      # Number of unsafe reports

# Is the report safe?
def analyze_report(level):
    report_status = 0               # 1 is safe, 0 is unsafe
    is_increasing = True       
    is_decreasing = True

# Test if the report is increasing properly
    for i in range(len(level) - 1):  
        if not (level[i] < level[i + 1] and 1 <= (level[i + 1] - level[i]) <= 3):   # Is the report strictly increasing by 3 or less? 
            is_increasing = False
            break

# Test if the report is decreasing properly 
    for i in range(len(level) - 1):  
        if not (level[i] > level[i + 1] and 1 <= (level[i] - level[i + 1]) <= 3):   # Is the report strictly decreasing by 3 or less?
            is_decreasing = False
            break 

# Is the report safe or not?          
    if is_increasing or is_decreasing:
        report_status = 1
    else:
        report_status = 0

    return report_status  

# Determine if a previously unsafe report is actually safe
# Can the originally unsafe report be made safe with only 1 exception? 
def problem_dampener(level):
    for i in range(len(level)):
        new_report = level[:i] + level[i+1:]        # Append new list with everything up to i and everything past i (exclusionary)
        correction = analyze_report(new_report)     # Re-analyze the new report
        if (correction == 1):                   
            new_status = 1
            break
        else:
            new_status = 0

    return new_status

with open("input.txt", "r") as file:                # Open 'input.txt' in read-mode

 
    report = [list(map(int, report.split())) for report in file if report.strip()]
    # report.split() splits each line into a list of strings separated by white space
    # map(int, ...) converts each string created by line.split into an int
    # list(map(...)) converts the map object into a list 
    # report.strip() ensures that empty lines are skipped 

for level in report:                                # For each line in 'input.txt'
    report_status = analyze_report(level)
    if (report_status == 0):
        damp_status = problem_dampener(level)       # Double check with the dampener
        if (damp_status == 1):
            safe_ctr += 1
        else:
            unsafe_ctr += 1
    else:
        safe_ctr += 1
    
print(f"There are: {safe_ctr} safe reports")
print(f"There are: {unsafe_ctr} unsafe reports")