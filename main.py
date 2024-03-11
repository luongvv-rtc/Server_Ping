# CNE335 Winter 2024
# Student name: Van Vuong
# Automate Ping Assignment

import os
import paramiko

class Server:

    def __init__(self, server_ip, key_pair, username):
        # TODO -
        self.server_ip = server_ip
        self.key_pair = key_pair
        self.username = username

def ping(self):
    # TODO - Use os module to ping the server
    result = os.system("ping -n 5 %s" % self.server_ip)
    return result


if __name__ == 'main':
    Ec2 = Server('18.236.67.210', 'KP_Web', 'root')
