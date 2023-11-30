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
# int fa 0/0
# ip add 10.0.0.18 255.255.255.252
# no shut

devices = [
    "10.0.0.2", #R5
    "10.0.0.10", #R4
    "10.0.0.18", #R_Profe
    "10.0.0.6" #R6
]

comands = [
    ["int se 0/0/0", #Configuraciones Router 5
    "ip add 10.0.0.9 255.255.255.252",
    "no shut",
    "int se 0/0/1",
    "ip add 10.0.0.5 255.255.255.252",
    "no shut",
    "int gi 0/0",
    "int gi 0/1",
    "ip add 10.0.0.17 255.255.255.252",
    "no shut",
    "ip route 10.0.10.0 255.255.248.0 10.0.0.18",
    "router ospf 10",
    "network 10.0.0.0 0.0.0.3 area 0",
    "network 10.0.0.4 0.0.0.3 area 1",
    "network 10.0.0.8 0.0.0.3 area 1",
    "network 10.0.0.16 0.0.0.3 area 0",
    "redistribute static"],

    ["no ip route 0.0.0.0 0.0.0.0 se 0/0/0", #Configuraciones Router 4
    "int serial 0/0/1",
    "no shut",
    "ip address 10.0.0.13 255.255.255.252",
    "int gi 0/0",
    "no shut",
    "int gi 0/1",
    "no shut",
    "router ospf 10",
    "network 10.0.0.8 0.0.0.3 area 1",
    "network 10.0.0.12 0.0.0.3 area 1",
    "network 10.0.30.0 0.0.0.255 area 1",
    "network 10.0.40.0 0.0.0.255 area 1",
    "passive-interface gi 0/0",
    "passive-interface gi 0/1",
    "int gi0/0.30",
    "encapsulation dot1q 30",
    "ip address 10.0.30.2 255.255.255.0",
    "standby version 2",
    "standby 30 ip 10.0.30.1",
    "standby 30 priority 1",
    "standby 30 preempt",
    "no shutdown",
    "encapsulation dot1q 40",
    "ip address 10.0.40.2 255.255.255.0",
    "standby version 2",
    "standby 40 ip 10.0.40.1",
    "standby 40 priority 150",
    "standby 40 preempt",
    "no shutdown",
    "ip dhcp excluded-address 10.0.30.1 10.0.30.10",
    "ip dhcp excluded-address 10.0.40.1 10.0.40.10",
    "ip dhcp pool VirtualBitches30",
    "network 10.0.30.0 255.255.255.0",
    "domain-name uag.mx",
    "dns-server 8.8.8.8",
    "default-router 10.0.30.1",
    "ip dhcp pool VirtualBitches40",
    "network 10.0.40.0 255.255.255.0",
    "domain-name uag.mx",
    "dns-server 8.8.8.8",
    "default-router 10.0.40.1"],

    ["no ip route 0.0.0.0 0.0.0.0 fa 0/0", #Configuraciones Router Profe
    "int fa 0/1",
    "no shut",
    "int fa 0/1.10",
    "encapsulation dot1q 10",
    "ip add 10.0.10.1 255.255.255.0",
    "int fa 0/1.20",
    "encapsulation dot1q 20",
    "ip add 10.0.20.1 255.255.255.0",
    "ip route 0.0.0.0 0.0.0.0 10.0.0.17"],

    ["no ip route 0.0.0.0 0.0.0.0 se 0/0/0", #Configuraciones Router 6
    "int se 0/0/1",
    "ip add 10.0.0.14 255.255.255.252",
    "no shut",
    "int gi 0/0",
    "no shut",
    "int gi 0/1",
    "no shut",
    "router ospf 10",
    "network 10.0.0.4 0.0.0.3 area 1",
    "network 10.0.0.12 0.0.0.3 area 1",
    "network 10.0.30.0 0.0.0.255 area 1",
    "network 10.0.40.0 0.0.0.255 area 1",
    "passive-interface gi 0/0",
    "passive-interface gi 0/1",
    "int gi0/0.30",
    "encapsulation dot1q 30",
    "ip address 10.0.30.3 255.255.255.0",
    "standby version 2",
    "standby 30 ip 10.0.30.1",
    "standby 30 priority 150",
    "standby 30 preempt",
    "no shutdown",
    "int gi0/1.40",
    "encapsulation dot1q 40",
    "ip address 10.0.40.3 255.255.255.0",
    "standby version 2",
    "standby 40 ip 10.0.40.1",
    "standby 40 priority 1",
    "standby 40 preempt",
    "no shutdown",
    "ip dhcp excluded-address 10.0.30.1 10.0.30.10",
    "ip dhcp excluded-address 10.0.40.1 10.0.40.10",
    "ip dhcp pool VirtualBitches30",
    "network 10.0.30.0 255.255.255.0",
    "domain-name uag.mx",
    "dns-server 8.8.8.8",
    "default-router 10.0.30.1",
    "ip dhcp pool VirtualBitches40",
    "network 10.0.40.0 255.255.255.0",
    "domain-name uag.mx",
    "dns-server 8.8.8.8",
    "default-router 10.0.40.1"]
]

for device in range(len(devices)):
    net_connect = ConnectHandler(device_type = "cisco_ios", ip = devices[device], username = "cisco", password = "cisco")
    net_connect.enable()
    output = net_connect.send_config_set(comands[device])