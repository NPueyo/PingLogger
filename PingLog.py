import ping3
import datetime
import time
import os
import argparse


# Function to ping an IP address and return the round-trip time
def ping(ip):
    """
    Function to ping an IP address and return the round-trip time.
    Args:
        ip (str): The IP address to ping.
    Returns:
        tuple: A tuple containing a boolean indicating whether the ping was successful and the round-trip time or error message.
    """
    try:

        rtt = ping3.ping(ip)
        if rtt is not None:
            return True, rtt
        else:
            return False, "Ping request timed out."
    except ping3.NetworkError as e:
        return False, f"Network error: {e}"
    except Exception as e:
        return False, f"Error: {e}"


def save_log(log_file, ip, result):
    """
    Function to save the ping result to a log file.

    Args:
        log_file (str): The path to the log file.
        ip (str): The IP address that was pinged.
        result (tuple): The result of the ping.
    """
    with open(log_file, 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f'{timestamp} IP: {ip}') # Write the current timestamp and the IP address
        if result[0]:
            file.write(f' Result: Success RTT: {result[1]} ms') # Write the success message
        else:
            file.write(f' Result: Error Details: {result[1]}')   # Write the error message
        file.write(f'\n')

# CLI Parser
def parse_args():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Continuous ping and log script")
    parser.add_argument("--ip", default="192.168.1.1", help="IP address to ping")
    parser.add_argument("--log_file", default="ping_log.log", help="Path to the log file")
    return parser.parse_args()


def main():
    args = parse_args()
    ip = args.ip
    log_file = args.log_file

    while True:
        try:
            result = ping(ip)  # Ping the IP address
            save_log(log_file, ip, result) # Save the result to the log file
            print("Ping done and logged.") # Print a success message
            time.sleep(1) # Wait for 1 second
        except KeyboardInterrupt:
            print("Program stopped by user.")  # Print a message when the program is stopped
            break



if __name__ == "__main__":
    main()
