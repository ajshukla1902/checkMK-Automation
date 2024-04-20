#!/usr/local/bin/python

###########################################
#       Original checkMKrestapi.py V1 is: #
#       Created By Aditya Shukla          #
#       Date : 12th-AUG-2021              #
#       DO NOT CHANGE THE FILE            #
###########################################

import argparse
import requests

def send_request(url, params):
    try:
        response = requests.post(url=url, data=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

def main():
    url = "http://check-mk.any/central/check_mk/view.py?"

    params = {
        '_username': args.username,
        '_secret': args.password,
        '_transid': '-1',
        '_do_actions': 'yes',
        'view_name': 'hoststatus',
        'host': args.host,
    }

    if args.operation == 'add':
        params.update({
            '_do_confirm': 'yes',
            '_down_from_now': 'yes',
            '_down_minutes': args.time,
            '_down_comment': args.comment,
        })
        params['_down_remove'] = ''  # Remove downtime flag for add operation

    elif args.operation == 'remove':
        params['_do_confirm'] = 'yes'
        params['_down_remove'] = 'Remove'

    else:
        print("Invalid operation. Use 'add' or 'remove'.")
        return

    response = send_request(url, params)
    if response:
        print(f"API response: {response}")
        print(f"API request successful. HTTP Code: {response.status_code}")
    else:
        print("API request failed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--operation", help="Provide Operation name add/remove", choices=['add', 'remove'], required=True)
    parser.add_argument("-t", "--time", help="Time duration to add host in downtime", type=int, default=None)
    parser.add_argument("-c", "--comment", help="Comment to add host in downtime", default=None)
    parser.add_argument("-u", "--username", help="Provide automation username", required=True)
    parser.add_argument("-p", "--password", help="Provide automation user password", required=True)
    parser.add_argument("-host", help="Operation to perform on hostname", required=True)  # Changed from -h to avoid conflict

    args = parser.parse_args()
    main()
