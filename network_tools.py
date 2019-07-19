import subprocess

def get_ping(address):
    try:
        ping = subprocess.check_output(["ping", "-c", "1", address]) 
        print("The server at " + address + " could be pinged")
        return True
    except subprocess.CalledProcessError:
        print("The server at " + address + " cannot be pinged - Aborting")
        return False
        
