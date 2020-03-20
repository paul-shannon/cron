#!/users/paul/anaconda/bin/python3
#----------------------------------------------------------------------------------------------------
import readline, smtplib, ssl
import requests
#----------------------------------------------------------------------------------------------------
targetURL = "http://apps.systemsbiology.net/app/Transcription_Factor_Protein_RNA_Erythropoiesis"
# targetURL = "https://oops.systemsbiology.net/app/Transcription_Factor_Protein_RNA_Erythropoiesis"
try:
   x = requests.head(targetURL)
except:
   print("failed to get %s" % targetURL)
   
port = 465  # For SSL
password = open("/users/paul/crontests.password").read()
server = smtplib.SMTP_SSL("smtp.gmail.com", port) 
sender = "crontests.pshannon@gmail.com"
server.login(sender, password)

scriptName = "hagfish:/users/paul/github/cron/scripts/check-tf-srm-shinyApp.py"


mailMessage = f"""Subject: tf+srm shiny app {x.status_code}

{targetURL}
http head request status: {x.status_code}

test script: {scriptName}

"""

server.sendmail(sender, sender, mailMessage)



