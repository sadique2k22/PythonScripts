import subprocess
import time

# Sleep for 2 seconds
time.sleep(2)

# Swipe command
swipe_command = "input touchscreen swipe 1000 500 100 500 100"

# Execute the command
for i in range(600):
    subprocess.run(swipe_command, shell=True)