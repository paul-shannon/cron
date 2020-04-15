#!/users/paul/anaconda/bin/python3
#----------------------------------------------------------------------------------------------------
import readline, smtplib, ssl
import requests
#----------------------------------------------------------------------------------------------------
def sendEmail(targetName, targetURL, statusCode):
   port = 465  # For SSL
   password = open("/users/paul/crontests.password").read()
   server = smtplib.SMTP_SSL("smtp.gmail.com", port) 
   sender = "crontests.pshannon@gmail.com"
   recipient = "pshannon@systemsbiology.org"
   server.login(sender, password)
   scriptName = "hagfish:/users/paul/github/cron/scripts/check-tf-srm-shinyApp.py"
   mailMessage = f"""Subject: test shiny apps - failure! {x.status_code}

{targetURL}
http head request status: {statusCode}

test script: {scriptName}

"""
   server.sendmail(sender, [recipient], mailMessage)

#----------------------------------------------------------------------------------------------------
targets = {"tms": "http://apps.systemsbiology.net/app/tms",
           "erythroProteinRNA":
             "http://apps.systemsbiology.net/app/Transcription_Factor_Protein_RNA_Erythropoiesis"}

for key in targets.keys():
   print("about to check %s" % key)
   targetURL = targets[key]
   success = True
   try:
      x = requests.head(targetURL)
   except:
      print("failed to get %s" % targetURL)
      success = False

   print("   success? %s" % success)
   if(not success):      
      sendEmail(key, targets[key], x.status_code)



