#!/usr/bin/env python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try :
    ssh.connect('warp.ifh.de', username='bonnefoy', password='test')
except paramiko.ssh_exception.AuthenticationException:
    print("authentication failed")
