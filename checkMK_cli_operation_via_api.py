#!/usr/local/bin/python

###########################################
#       Original checkMKrestapi.py V1 is: #
#       Created By Aditya Shukla          #
#       Date : 12th-AUG-2021              #
#       DO NOT CHANGE THE FILE            #
###########################################

import argparse
import requests 
from operator import add
from functools import reduce


def Main():

    url = "http://check-mk.any/central/check_mk/view.py?"

    if 'add' in args.operation:
        param = {
                '_username' : args.username,
                '_secret' : args.password,
                '_transid' : '-1',
                '_do_confirm' : 'yes',
                '_do_actions' : 'yes',
                'host' : args.phost,
                '_down_from_now' : 'yes',
                '_down_minutes' : args.time,
                '_down_comment' : args.comment,
                'view_name' : 'hoststatus'
            }

    if 'remove' in args.operation:
        param = {
                '_do_confirm' : 'yes',
                '_transid' : '-1',
                '_do_actions' : 'yes',
                '_username' : args.username,
                '_secret' : args.password,
                'view_name' : 'hoststatus',
                'host' : args.phost,
                '_down_remove' : 'Remove'
            }

    try:
        restApi = requests.post(url = url, data = param)
        print(restApi)
        print("API is successfully fetched. HTTP Code: " + str(restApi.status_code))
    except:
        print("API failed to fetched. HTTP Code: " + str(restApi.status_code))
    print(restApi.status_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--operation", help="Provide Operation name add/remove", required=True)
    parser.add_argument("-h", "--host", help="Operation to perform on hostname", required=True)
    parser.add_argument("-t", "--time", help="Time duration to add host in downtime", default=None, required=False)
    parser.add_argument("-c", "--comment", help="Comment to add host in downtime", default=None, required=False)
    parser.add_argument("-u", "--username", help="Provide automation username", required=True)
    parser.add_argument("-p", "--password", help="Provide automation user password", required=True)
    
    args = parser.parse_args()
    
    Main()