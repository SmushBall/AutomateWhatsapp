from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from whatsapp_msg import send_msg


sched = BlockingScheduler()

# Schedule Joob_function to be caleld every 1 hour
sched.add_job(send_msg, 'interval', seconds =60)

sched.start()

