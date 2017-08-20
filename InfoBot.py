#!/usr/bin/env python
# -*- coding: utf-8 -*- ANIRUDH TRIGUNAYAT, VAREN AGGARWAL, DEEPANSH YADAV -*-

from __future__ import print_function

import pyttsx
import os
import sys
import json
import MySQLdb
from prettytable import PrettyTable
import apiai
 

CLIENT_ACCESS_TOKEN = '61459d55984a4b0b9b4cae21c648c61f'

def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:
        print(u"> ", end=u"")
        user_message = raw_input()

        if user_message == u"exit":
         break

        request = ai.text_request()
        request.query = user_message

        engine = pyttsx.init()

        response = json.loads(request.getresponse().read())

        result = response['result']
        parameters=result['parameters']

        action = result.get('action')
        actionIncomplete = result.get('actionIncomplete', False)

	if(parameters is None):
		temp=response['result']['fulfillment']['speech']
		print(u"< %s" % temp)
		#engine.say(temp)
		#engine.runAndWait()
	
	else:
		tracType=parameters.get('Type')
		tracModel=parameters.get('Model')
		issue=parameters.get('issue')
		hp=parameters.get('number')
		if(hp is not None and len(hp)!=0):
			hp=int(parameters.get('number'))	
		if( (issue is None) and (tracType is not None and len(tracType)!=0) and (tracModel is not None and len(tracModel)!=0) ):
			if (tracType=='Ferrari'):
				flag=False
				# Open database connection
				db = MySQLdb.connect("127.0.0.1","root","root","chatbot" )
				# prepare a cursor object using cursor() method
				cursor = db.cursor()
				# Prepare SQL query to INSERT a record into the database.
				sql = "SELECT * FROM ferrari WHERE model_no = '%s'" % (tracModel)	
				
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				
				#model_no, engine_hp, cylinders,bore, stroke, cc
				table = PrettyTable(["Model_No","Engine_HP","Cylinders","Bore (mm)","Stroke(mm)","Cubic_Capacity(cc)"])

				tup=[]
				for row in results:
					tup.append(row[0])
					tup.append(row[1])
					tup.append(row[2])
					tup.append(row[3])
					tup.append(row[4])
					tup.append(row[5])
					
					table.add_row(tup)
					print("< Here is the information asked:")
					#engine.say('Here is the information asked')
					#engine.runAndWait()
					print(table)
					flag=True
					break;
				if (flag==False):
					temp="No such record found!"
					print (temp)
					#engine.say(temp)
					#engine.runAndWait()
				
				db.close()

			elif (issue=='issue'): 
				tracType=tracModel=None

				while( (tracType is not None) and (tracModel is not None) ):
					temp=response['result']['fulfillment']['speech']
					print(u"< %s" % temp)
					#engine.say(temp)
					#engine.runAndWait()


				# now will  keep running the loop until the issue is solved then will, enter in database.
				#while()

			elif (tracType=='Powertrac'):
				flag=False
				# Open database connection
				db = MySQLdb.connect("127.0.0.1","root","root","chatbot" )
				# prepare a cursor object using cursor() method
				cursor = db.cursor()
				# Prepare SQL query to INSERT a record into the database.
				sql = "SELECT * FROM powertrac WHERE model_no = '%s'" % (tracModel)	
				
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				
				#model_no, engine_hp, cylinders,bore, stroke, cc
				table = PrettyTable(["Model_No","Engine_HP","Cylinders","Bore (mm)","Stroke(mm)","Cubic_Capacity(cc)","Rated RPM"])

				tup=[]
				for row in results:
					tup.append(row[0])
					tup.append(row[1])
					tup.append(row[2])
					tup.append(row[3])
					tup.append(row[4])
					tup.append(row[5])
					tup.append(row[6])
					
					table.add_row(tup)
					print("< Here is the information asked:")
					#engine.say('Here is the information asked')
					#engine.runAndWait()
					print(table)
					flag=True
					break;
				if (flag==False):
					temp="No such record found!"
					print (temp)
					#engine.say(temp)
					#engine.runAndWait()
				
				db.close()
			elif (tracType=='Farmtrac'):
				flag=False
				# Open database connection
				db = MySQLdb.connect("127.0.0.1","root","root","chatbot" )
				# prepare a cursor object using cursor() method
				cursor = db.cursor()
				# Prepare SQL query to INSERT a record into the database.
				sql = "SELECT * FROM farmtrac WHERE model_no = '%s'" % (tracModel)	
				
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				
				#model_no, engine_hp, cylinders,bore, stroke, cc
				table = PrettyTable(["Model_No","Engine_HP","Cylinders","Bore (mm)","Stroke(mm)","Cubic_Capacity(cc)"])

				tup=[]
				for row in results:
					tup.append(row[0])
					tup.append(row[1])
					tup.append(row[2])
					tup.append(row[3])
					tup.append(row[4])
					tup.append(row[5])
					
					table.add_row(tup)
					print("< Here is the information asked:")
					#engine.say('Here is the information asked')
					#engine.runAndWait()
					print(table)
					flag=True
					break;
				if (flag==False):
					temp="No such record found!"
					print (temp)
					#engine.say(temp)
					#engine.runAndWait()
				
				db.close()
		#elif(issue is not None and len(issue)!=0 and issue=='issue'):
		#	print("OK")
		elif ( (hp is not None) and (hp!=0) ):
			# Open database connection
			db = MySQLdb.connect("127.0.0.1","root","root","chatbot" )
			# prepare a cursor object using cursor() method
			cursor = db.cursor()
			maxV=minV=0
			if(hp<20):
				temp='There is no implement compatible with your tractor\'s horse power, Sorry!'
				print(temp)
				#engine.say(temp)
				#engine.runAndWait()
			else:
				
				if(hp>=20 and hp<25):
					minV=20
					maxV=24
				elif(hp>=25 and hp<30):
					minV=25
					maxV=29
				elif(hp>=30 and hp<35):
					minV=30
					maxV=34
				elif(hp>=35 and hp<40):
					minV=35
					maxV=39
				elif(hp>=40 and hp<45):
					minV=40
					maxV=44
				elif(hp>=45 and hp<50):
					minV=45
					maxV=49
				elif(hp>=50 and hp<55):
					minV=50
					maxV=54
				elif(hp>=55 and hp<60):
					minV=55
					maxV=59
				elif(hp>=60):
					minV=60
					maxV=100

				# Prepare SQL query to INSERT a record into the database.
				print("<It seems like your tractor matches with the %d tractor implements.\n<The following implements can be added to your tracotr!\n" % (minV))
				sql = "SELECT * FROM implements WHERE hp>=%d && hp<=%d" % (minV,maxV)
				
				#engine.say('It seems like your tractor matches with the %d tractor implements.' % (minV))
				#engine.say('The following implements can be added to your tracotr!')
				#ngine.run()
	
				# Execute the SQL command
				cursor.execute(sql)
				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
	
				#model_no, engine_hp, cylinders,bore, stroke, cc

				table = PrettyTable(["HP", "Cultivator", "Trail_Type_Harrow", "Mountain_Type_Harrow", "Disc_Plough"," Rotavator"])

				tup=[]
				for row in results:
					tup.append(row[0])
					tup.append(row[1])
					tup.append(row[2])
					tup.append(row[3])
					tup.append(row[4])
					tup.append(row[5])
			
				table.add_row(tup)
				print(table)			
			db.close()
		else:
			temp=response['result']['fulfillment']['speech']
			print(u"< %s" % temp)
			#engine.say(temp)
			#engine.runAndWait()

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
                    #engine.say("Sending Message")
					#engine.runAndWait()
                    break



while 1:
	try:
			if (__name__ == '__main__'):
    				main()
    				break
	except:
		print("< Sorry could not get you.")
		#engine.say('Sorry could not get you.')
		#engine.runAndWait()
