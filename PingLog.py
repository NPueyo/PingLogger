# Import necessary libraries
import ping3
import datetime
import time
import os

# Function to ping an IP address and return the round-trip time
def ping(ip):
    try:
        # Execute the ping and get the round-trip time
        rtt = ping3.ping(ip)
        if rtt is not None:
            return True, rtt
        else:
            return False, None
    except Exception as e:
        return False, None

# Function to save the ping result to a log file
def save_log(log_file, ip, result):
    with open(log_file, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f'{timestamp}')  # Write the current timestamp
        file.write(f' IP: {ip}')  # Write the IP address
        if result[0]:
            file.write(f' Result: Success')  # Write the success message
            file.write(f' RTT: {result[1]} ms')  # Write the round-trip time
        else:
            file.write(f' Result: Error')  # Write the error message
            file.write(f' Details: {result[1]}')  # Write the error details
        file.write(f'\n')

# IP address to ping
ip = "192.168.1.1"

# Log file path on Windows desktop
log_file = os.path.join(os.path.expanduser("~"), "Desktop", "ping_log.txt")

# Continuous loop with 1-second interval
def Ping_f(ip,log_file):
    while True:
        try:
            result = ping(ip)  # Ping the IP address
            save_log(log_file, ip, result)  # Save the result to the log file
            print("Ping done and logged.")  # Print a success message
            time.sleep(1)  # Wait for 1 second
        except KeyboardInterrupt:
            print("Program stopped by user.")  # Print a message when the program is stopped
            break
