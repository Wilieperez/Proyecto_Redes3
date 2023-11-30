import json
from netmiko import ConnectHandler

#Comandos que se tienen que configurar manualmente
#
# -----R4-----
# enable
# conf terminal
# hostname R4
# ip domain name cisco.com
# line vty 0 4
# login local
# transport input ssh
# crypto key gen rsa
# 1024
# username cisco password cisco
# ip route 0.0.0.0 0.0.0.0 se 0/0/0
# int se 0/0/0
# ip add 10.0.0.10 255.255.255.252
# no shut

# -----R5-----
# enable
# conf terminal
# hostname R5
# ip domain name cisco.com
# line vty 0 4
# login local
# transport input ssh
# crypto key gen rsa
# 1024
# username cisco password cisco
# int gi 0/0
# ip add 10.0.0.2 255.255.255.252
# no shut

# -----R6-----
# enable
# conf terminal
# hostname R6
# ip domain name cisco.com
# line vty 0 4
# login local
# transport input ssh
# crypto key gen rsa
# 1024
# username cisco password cisco
# ip route 0.0.0.0 0.0.0.0 se 0/0/0
# int se 0/0/0
# ip add 10.0.0.6 255.255.255.252
# no shut

# -----R_Profe-----
# enable
# conf terminal
# hostname R_Profe
# ip domain name cisco.com
# line vty 0 4
# login local
# transport input ssh
# crypto key gen rsa
# 1024
# username cisco password cisco
# ip route 0.0.0.0 0.0.0.0 fa 0/0
# int gi 0/0
# ip add 10.0.0.18 255.255.255.252
# no shut

devices = [
    "10.0.0.2", #R5
    "10.0.0.10", #R4
    "10.0.0.18", #R_Profe
    "10.0.0.6" #R6
]

with open('Devices.JSON', 'r') as file:
    device_commands = json.load(file)

for device in devices:
    net_connect = ConnectHandler(device_type = "cisco_ios", ip = device, username = "cisco", password = "cisco")
    net_connect.enable()
    output = net_connect.send_config_set(device_commands[device])