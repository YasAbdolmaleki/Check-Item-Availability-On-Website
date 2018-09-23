# Scrape a Website and Send Email When an Item is Back on Stock

CheckItemAvailability.py is a script that sends an email to you if an item on a webpage is back on stock.
This script is currenlty tailored for the [Louis Vuitton Pochette Accessories](https://eu.louisvuitton.com/eng-e1/products/pochette-accessoires-monogram-005656) purse in Monogram which is sold out most of the times and sometimes it becomes available online.
The script can be easily modified to be used for other websites.

# Instruction

You can schedule to run the python script in 2 ways:
1. use crontab: https://pypi.org/project/python-crontab/
  * trickier to use
  * checkout the useful commands bellow
  * job is run seemlessly
2. use schedule to call your function every min/hour/....: https://github.com/dbader/schedule
 * easier alternative
 * have to run python script manually

## Kinda useful python-crontab commands (Run ScriptScheduler)

##### read cron messages
`cat /var/mail/<USER NAME>`

`mail`

`sudo cron status`

`ps -ax|grep <PYTHON>`

##### delete cron messages
`d1-4`

##### edit cron job file
`crontab -e`

##### clears cron job file
`crontab -r`

##### other solution to remove jobs - didn't work
`sudo cron reload`

`sudo pkill <PID>`

`sudo kill -6 <PID>`

##### remove python script jobs
`ps -ax | grep python | pkill python`


[How to Scrape Websites](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe)
