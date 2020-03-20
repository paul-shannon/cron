#!/users/paul/anaconda/bin/python3
#----------------------------------------------------------------------------------------------------
import readline
import smtplib, ssl
#import requests
import subprocess
from subprocess import PIPE
#----------------------------------------------------------------------------------------------------
cmd = "/bin/bash -c 'source /users/paul/.bashrc; /usr/bin/make -f /users/paul/github/dailyPackageBuilds/makefile default -k 2>&1'"
results = subprocess.run(cmd, shell=True, universal_newlines=True, check=True, stdout=PIPE, stderr=PIPE)
print(results.stdout)

port = 465  # For SSL
password = open("/users/paul/crontests.password").read()
server = smtplib.SMTP_SSL("smtp.gmail.com", port) 
sender = "crontests.pshannon@gmail.com"
server.login(sender, password)

mailMessage = f"""Subject: TrenaProjectHG38.generic built and tested {results.returncode}

running script from cron: ~/github/cron/experiments/trenaBuilds/trenaBuilds.py
"""

server.sendmail(sender, sender, mailMessage)

