#!/users/pshannon/local/py382/bin/python3
#----------------------------------------------------------------------------------------------------
import sys
import smtplib, ssl
import requests
from pathlib import Path
#----------------------------------------------------------------------------------------------------
targetURL = "http://apps.systemsbiology.net/app/Transcription_Factor_Protein_RNA_Erythropoiesis"
# targetURL = "https://oops.systemsbiology.net/app/Transcription_Factor_Protein_RNA_Erythropoiesis"
try:
   x = requests.head(targetURL)
except:
   print("failed to get %s" % targetURL)
   
homeDir = Path.home() 
passwordFile = homeDir / 'crontests.password'
password = open(passwordFile).read()

port = 465  # For SSL
server = smtplib.SMTP_SSL("smtp.gmail.com", port) 
sender = "crontests.pshannon@gmail.com"

server.login(sender, password)

scriptName = Path(__file__).resolve()


mailMessage = f"""Subject: khaleesi shinyApps check {x.status_code}

{targetURL}
http head request status: {x.status_code}

test script: {scriptName}

"""

server.sendmail(sender, sender, mailMessage)



