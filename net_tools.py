import subprocess

def get_ping(address):
    print(address)
    ping = subprocess.check_output(["ping", "-c", "1", address]) 
    if ping:
        print("The server at " + address + " could be pinged")
    else:
        print("The server at " + address + " cannot be pinged - Aborting")
        
