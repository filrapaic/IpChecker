import requests
import json
import csv

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

def Get_Result():    
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': '<YOUR API KEY GOES HERE>'
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
    decodedResponse = json.loads(response.text)
    try:
        output = decodedResponse['data']['ipAddress']+";"+str(decodedResponse['data']['abuseConfidenceScore'])+";"+decodedResponse['data']['countryCode']+";"+decodedResponse['data']['domain']+";"+decodedResponse['data']['isp']+";" + "\n"
        print (output)
        destination.write(output)
    except Exception: 
        output = str(ip)+","+" - ;"+"-;"+" - ;"+" - ;"+"\n"
        print (output)
        destination.write(output)
    
source = open("iplist.txt",'r')
destination = open("output2.txt",'a')
reader = csv.reader(source)
single_ip = [row for row in reader]
number_ip = len(single_ip)

for i in range(number_ip):
    ip = single_ip[i]
    Get_Result()

source.close()
destination.close()
    
print ("All done!")

