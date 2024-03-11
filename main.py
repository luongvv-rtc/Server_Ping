# CNE335 Winter 2024
# Student name: Van Vuong
# Automate Ping Assignment

import os
import paramiko

class Server:

    def __init__(self, server_ip, rsa_key, upgrade, username):
        # TODO -
        self.server_ip = server_ip
        self.rsa_key = rsa_key
        self.upgrade = upgrade
        self.username = username

