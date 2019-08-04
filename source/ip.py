
import subprocess

def local():
    command = 'ip addr | grep "global" | egrep -o "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" | head -n1'
    process = subprocess.run(command, shell=True, check=True, encoding='utf-8', stdout=subprocess.PIPE)
    ip = process.stdout.split()
    if not ip: raise RuntimeError("No Network Connection")
    return ip[0]
