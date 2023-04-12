import ping3
import datetime
import time
import os

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

def save_log(log_file, ip, result):
    with open(log_file, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f'{timestamp}')
        file.write(f' IP: {ip}')
        if result[0]:
            file.write(f' Result: Success')
            file.write(f' RTT: {result[1]} ms')


        else:
            file.write(f' Result: Error')
            file.write(f' Details: {result[1]}')
        file.write(f'\n')

# IP address to ping
ip = "192.168.1.1"

# Log file path on Windows desktop
log_file = os.path.join(os.path.expanduser("~"), "Desktop", "ping_log.txt")

# Continuous loop with 1-second interval
def Ping_f(ip,log_file):
    while True:
        try:
            result = ping(ip)
            save_log(log_file, ip, result)
            print("Ping done and logged.")
            time.sleep(1)
        except KeyboardInterrupt:
            print("Program stopped by user.")
            break
