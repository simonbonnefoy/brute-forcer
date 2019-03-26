#!/usr/bin/env python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try :
    ssh.connect(host username='user', password='test')
except paramiko.ssh_exception.AuthenticationException:
    print("authentication failed")
