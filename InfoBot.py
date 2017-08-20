#!/usr/bin/env python
# -*- coding: utf-8 -*- ANIRUDH TRIGUNAYAT, VAREN AGGARWAL, DEEPANSH YADAV -*-

from __future__ import print_function
from beautifultable import BeautifulTable
import os
import sys
import json
import csv

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )

import apiai

CLIENT_ACCESS_TOKEN = 'c258b3c2f04e464d9ae8cf641e8ccc7e'

def main():
  
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
            break

        request = ai.text_request()
        request.query = user_message

        response = json.loads(request.getresponse().read())

        result = response['result']
        parameters=result['parameters']

        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)
	
	if(len(parameters)==0):
		print(u"< %s" % response['result']['fulfillment']['speech'])
	
	else:
		issue=parameters.get('issue')
		if(issue is None):
			issue='False'
		tracType=parameters.get('Type')
		tracModel=parameters.get('Model')
		if( (issue=='False') and (tracType is not None) and (tracModel is not None) ):
			if (tracType=='Ferrari'):
				f_obj=open("Ferrari.csv", "r+").readlines()
				table = BeautifulTable()

				flag=False
				for i in f_obj :
					arr=i.split(';')
					if(arr[0]==tracModel):
						arr2=f_obj[0].split(';')
						arr2[len(arr2)-1]=""
						arr[len(arr)-1]=""
						table.column_headers = arr2
						table.append_row(arr)
						print (table)
						#for j in range(0,len(arr2)-1,1):
						#	print(arr2[j], end='\t')
						#print ("")		
						#for j in range(0,len(arr)-1,1):
						#	print (arr[j], end='\t')
						#print ('')			
						flag=True
						break;
				if (flag==False):
					print ("No such record found!")

			elif (tracType=='Powertrac'):
				f_obj=open("PowerTrac.csv", "r+").readlines()
				table = BeautifulTable()

				flag=False
				for i in f_obj :
					arr=i.split(';')
					if(arr[0]==tracModel):
						arr2=f_obj[0].split(';')
						arr2[len(arr2)-1]=""
						arr[len(arr)-1]=""
						table.column_headers = arr2
						table.append_row(arr)
						print (table)			
						flag=True
						break;
				if (flag==False):
					print ("No such record found!")
			elif (tracType=='Farmtrac'):
				f_obj=open("FarmTrac.csv", "r+").readlines()
				table = BeautifulTable()

				flag=False
				for i in f_obj :
					arr=i.split(';')
					if(arr[0]==tracModel):
						arr2=f_obj[0].split(';')
						arr2[len(arr2)-1]=""
						arr[len(arr)-1]=""
						table.column_headers = arr2
						table.append_row(arr)
						print (table)			
						flag=True
						break;
				if (flag==False):
					print ("No such record found!")
		else:
			print(u"< %s" % response['result']['fulfillment']['speech'])

        

        if action is not None:
            if action == u"send_message":
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()