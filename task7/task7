""" Task: 

● Server Log Error Streamer: The backend team has server log files too large to load 
into memory. Build a streaming system that reads line by line, yields only critical error 
entries, groups them by error type, and shows a live running count — without loading the 
full file at once."""

def read_errors():
    logs=[
         "INFO: Server started",
        "CRITICAL: Database failed",
        "ERROR: Login failed",
        "CRITICAL: Disk is full",
        "CRITICAL: Database failed"
    ]
    for line in logs:
        if "CRITICAL" in line:
            yield line
count=0
errors={}

for error in read_errors():
    count += 1
    print("Error",count,":",error)

    if error not in errors:
        errors[error] =1
    else:
        errors[error] +=1
print("\nTotal critical errors:", count)
print("Grouped errors:", errors)
