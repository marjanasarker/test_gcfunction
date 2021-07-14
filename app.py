from crontab import CronTab
import main 
cron = CronTab(user='username')
job = cron.new(command='python main.py')
job.minute.every(1)

cron.write()