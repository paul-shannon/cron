library(mailR)
library(yaml)
config <-  yaml.load(readLines("~/cron-support.yaml"))
mailkey <- config$mailkey
log.dir <- "/etc/shinyproxy-2.2.1/container-logs"
file.names <- list.files(log.dir, full.names=FALSE, pattern="*_stdout.log")
length(file.names)
file.info(file.path(log.dir, file.names[[1]]))$ctime

age <- lapply(file.names, function(file)
                 as.double(difftime(Sys.time(), file.info(file.path(log.dir, file))$ctime,
                           units="hours")))
names(age) <- file.names

new.files <- which(unlist(age) <= 1)
if(length(new.files) > 0){
   new.logs <- file.names[new.files]
   line.counts <- unlist(lapply(new.logs, function(file) system(sprintf("wc -l %s", file.path(log.dir, file)), intern=TRUE)))
   # msg <- paste(new.logs, collapse="\n")
   msg <- paste(line.counts, collapse="\n")
   send.mail(from = "crontests.pshannon@gmail.com",
             to = "pshannon@systemsbiology.org",
             replyTo = "crontests.pshannon@gmail.com",
             subject = sprintf("%d shinyProxy runs in last hour", length(new.files)),
             body = msg,
             smtp = list(host.name="smtp.gmail.com",
                         port=465,
                         user.name="crontests.pshannon@gmail.com",
                         passwd=mailkey,
                         ssl=TRUE),
             authenticate=TRUE,
             send=TRUE)
   } # if new logs
