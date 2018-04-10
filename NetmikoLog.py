# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
import os

with open("commands.txt","r") as file:
	cmds = (line.rstrip() for line in file)
	cmds = list(cmd for cmd in cmds if cmd)
	cmds_len = len(cmds)


if not os.path.exists('logs'):
    os.makedirs('logs')

host = input('hostname:')
username = input('username:')
password = getpass.getpass('password:')

my_device = {
    'host': host,
    'username': host,
    'password': password,
    'device_type': 'cisco_xr',
}

try:
    net_connect = ConnectHandler(**my_device)
    f1 = open('logs/' + host + '.txt', "w+")
    f1.write('\n')
    for cmd in cmds:
        print(cmd.strip('\n'))
        output = net_connect.send_command(cmd,delay_factor=10,max_loops=100)
        f1.write('#'+cmd+'\n')
        f1.write(output)
        
	print('log collection completed')
    net_connect.disconnect()

except:
    print('Incorrect Username or password')