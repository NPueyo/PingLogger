def test_ping():
    """
    Test the ping function with a known IP.
    """
    ip = "8.8.8.8"  # Google's public DNS server
    result = ping(ip)
    assert result[0] == True  # The ping should be successful
    assert isinstance(result[1], float)  # The round-trip time should be a float

def test_save_log(tmpdir):
    """
    Test the save_log function.
    """
    ip = "8.8.8.8"
    result = (True, 20.0)  # A dummy result
    log_file = tmpdir.join("log.txt")  # Use a temporary file for the log

    save_log(log_file, ip, result)

    # Check the contents of the log file
    with open(log_file, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 1  # There should be one line in the log file
        assert lines[0].startswith(datetime.datetime.now().strftime("%Y-%m-%d"))  # The log should start with the current date
        assert f' IP: {ip}' in lines[0]  # The log should contain the IP address
        assert ' Result: Success' in lines[0]  # The log should contain the result
        assert f' RTT: {result[1]} ms' in lines[0]  # The log should contain the round-trip time