import argparse
import requests
import urllib.parse
import subprocess
import psutil
import socket

"""
    This script is used to login/logout the eportal system.
    The key to the success of the login/logout operation is 
    to get the correct login and logout urls.

    To facilitate the quick update of the script's login/logout
    urls when the url address and parameters are changed on the 
    server side, we recommend to confer to the following guide:
    How-to-obtain-the-eportal-urls.md
"""

eportal_url = "http://10.254.7.4:801/eportal/portal"

def login(username, password, ip):
    """
    eportal login operation.
    """
    print("try login...")
    real_login_url = eportal_url + \
         "/login"\
          "?login_method=1"\
          "&user_account=%2C0%2C{}"\
          "&user_password={}"\
          "&wlan_user_ip={}"\
          "&wlan_user_ipv6="\
          "&wlan_user_mac=000000000000"\
          "&wlan_ac_ip="\
          "&wlan_ac_name="\
          "&ua="\
          "&term_type="\
          "&jsVersion=4.2"\
          "&terminal_type=1" \
          "&lang=en".format(username, password, ip)
    response = requests.get(real_login_url)
    return response.text

def logout(ip):
    """
    eportal logout operation.
    """
    print("try logout...")
    real_logout_url = eportal_url+\
          "/logout"\
          "?login_method=1"\
          "&user_account==drcom"\
          "&ac_logout=1"\
          "&register_mode=1"\
          "&wlan_user_ip={}"\
          "&wlan_user_ipv6="\
          "&wlan_vlan_id=1"\
          "&wlan_user_mac=000000000000"\
          "&wlan_ac_ip="\
          "&wlan_ac_name="\
          "&jsVersion=4.2"\
          "&lang=en".format(ip)
    response = requests.get(real_logout_url)
    return response.text

def get_default_interface_name():
    # Command to get routing table under Linux
    command = 'ip route show'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        # Parse the output to get the default interface name
        for line in result.stdout.splitlines():
            if "default" in line:  # find the line with default route
                # get the line like 'default via 192.168.1.1 dev eth0'
                parts = line.split()
                if len(parts) >= 5:
                    return parts[4]  # return the interface name
    return None

# mac 地址对于解绑定的时候可能有用，登陆时还用不到
def get_interface_addr(interface_name):
    # get all network interfaces
    interfaces = psutil.net_if_addrs()
    # Check whether the specified network card exists
    if interface_name not in interfaces:
        raise KeyError(f"{interface_name} not exist")

    # Traverse the address information of the specified network card
    for device in interfaces[interface_name]:
        if device.family == socket.AF_INET:  # Filter out IPv4 address
            ipv4_addr = device.address  
        # if device.family == socket.AF_INET6: # Filter out IPv6 address
        #     ipv6_addr = device.address
        # if device.family == socket.AF_PACKET: # Filter out mac address
        #     mac_addr = device.address
    # return ipv4_addr, ipv6_addr, mac_addr
    return ipv4_addr

def main():
    # Create a command line argument parser
    parser = argparse.ArgumentParser(description='eportal login/logout tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # login subcommand
    login_parser = subparsers.add_parser('login', help='login eportal')
    login_parser.add_argument('username', type=str, help='username')
    login_parser.add_argument('password', type=str, help='password')

    # logout subcommand
    logout_parser = subparsers.add_parser('logout', help='logout eportal')

    # parse command line arguments
    args = parser.parse_args()

    # get the ip address of the default network interface
    interface_name = get_default_interface_name()
    if interface_name == None :
        print("cannot identify default network interface")
        exit(1) 

    ipv4_addr= get_interface_addr(interface_name)

    # execute the appropriate command
    if args.command == 'login':
        username = urllib.parse.quote(args.username)
        password = urllib.parse.quote(args.password)
        login_result = login(username, password, ipv4_addr)
        print("login response:", login_result)
    elif args.command == 'logout':
        logout_result = logout(ipv4_addr)
        print("logout response:", logout_result)

if __name__ == '__main__':
    main()