#!/users/pshannon/anaconda3/bin/python3
#----------------------------------------------------------------------------------------------------
import readline
import smtplib, ssl
import subprocess
from subprocess import PIPE
#----------------------------------------------------------------------------------------------------
cmd = "/bin/bash -c 'source /users/pshannon/.bashrc; /usr/bin/make -k -f /users/pshannon/github/dailyPackageBuilds/makefile TrenaProjectArabidopsisRoot  2>&1'"
output = PIPE
#output = None
results = subprocess.run(cmd, shell=True, universal_newlines=True, check=False, stdout=output, stderr=output)
print("subprocess.run complete, results: %d", results)
print(results.stdout)

port = 465  # For SSL
password = open("/users/pshannon/crontests.password").read()
server = smtplib.SMTP_SSL("smtp.gmail.com", port) 
sender = "crontests.pshannon@gmail.com"
server.login(sender, password)

mailMessage = f"""Subject: khaleesi trena build (arabidopsis) {results.returncode}

running script from cron on khaleesi: ~/github/cron/experiments/trenaBuilds/trenaBuilds.py
"""

server.sendmail(sender, sender, mailMessage)

