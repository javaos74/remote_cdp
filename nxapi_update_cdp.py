#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import requests
import json
import util
import os 
import scpclient
from contextlib import closing
import paramiko


def scp_update_cdp_code( hostip, userid, passwd):
	retval = False
	ssh_client = paramiko.SSHClient()
	ssh_client.load_system_host_keys()
	try:
		ssh_client.connect( hostip, username=userid, password=passwd)
		with closing( scpclient.Write( ssh_client.get_transport(), '.')) as scp:
			scp.send_file( 'update_cdp.py', True)
		retval = True
	except Exception:
		print 'failed to scp update_cdp.py'
	return retval


def update_cdp(hostip, userid, passwd):
	retval = True
	target_cmd = "python bootflash:update_cdp.py"
	target_cmd = util.remove_last_semicolon(target_cmd)
	resp = requests.post( util.get_nxapi_endpoint( hostip), data=json.dumps( util.get_conf_payload( target_cmd)), headers=util.myheaders,auth=(userid,passwd)).json()
	outputs = resp['ins_api']['outputs']['output']
	#print outputs
	if not 'Success' in outputs['msg']:
		retval = False
	print 'update_cdp on %s is %s' %(hostip, retval)
	return retval


if __name__ == '__main__':
	roles  = util.load_config( sys.argv[1]) #hosts.yaml
	for role in roles.keys():
		for host in roles[role]:
			scp_update_cdp_code( host, os.environ['NEXUS_USER'], os.environ['NEXUS_PASSWD'])
			update_cdp( host, os.environ['NEXUS_USER'], os.environ['NEXUS_PASSWD'])

