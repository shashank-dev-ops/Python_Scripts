import time

wait_time = 1
max_retries = 2
attempt = 0

while attempt < max_retries:
    print("Attempt", attempt + 1, "wait_time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2  # Double the wait time
    attempt += 1 # Increment the attempt counter