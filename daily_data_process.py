import logging
import subprocess
from datetime import datetime

# ------------------------------------------------------------------
# setup logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(module)s;%(levelname)s;%(asctime)s;%(message)s')

file_handler = \
    logging.FileHandler(f"//db-rb-fs001/data_qlik_desktop/data_source_apps/"
                        f"_logs/data_processing_{datetime.today().strftime('%d.%m.%Y')}.log")

file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# ------------------------------------------------------------------
# Start of daily data process

logger.info(f"Daily data process has been started")

# Download Email Attachments

run_getMailAttachments = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/get_mailAttachments.py', shell=True,
                   capture_output=True)

if run_getMailAttachments.returncode != 0:
    logger.error(f"Module get_mailAttachments did not ran successfully")
else:
    logger.info(f"Module get_mailAttachments did ran successfully")


# Move Email Attachments

run_moveMailAttachments = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/move_mailAttachments.py', shell=True,
                   capture_output=True)

if run_moveMailAttachments.returncode != 0:
    logger.error(f"Module move_mailAttachments did not ran successfully")
else:
    logger.info(f"Module move_mailAttachments did ran successfully")


# Move Opera Schedule Files

run_moveOperaSchedule = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/move_OperaSchedule.py', shell=True,
                   capture_output=True)

if run_moveOperaSchedule.returncode != 0:
    logger.error(f"Module move_OperaSchedule did not ran successfully")
else:
    logger.info(f"Module move_OperaSchedule did ran successfully")


# Remove old BUS_055 Files in actual_period

run_remove_old_BUS_055 = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/remove_old_BUS_055.py', shell=True,
                   capture_output=True)

if run_remove_old_BUS_055.returncode != 0:
    logger.error(f"Module remove_old_BUS_055 did not ran successfully")
else:
    logger.info(f"Module remove_old_BUS_055 did ran successfully")


# Remove old BUS_055_Sales Files only fridays

run_remove_old_BUS_055_Sales = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/remove_old_BUS_055_Sales.py',
                   shell=True, capture_output=True)

if run_remove_old_BUS_055_Sales.returncode != 0:
    logger.error(f"Module remove_old_BUS_055_Sales did not ran successfully")
else:
    logger.info(f"Module remove_old_BUS_055_Sales did ran successfully")

logger.info(f"Daily data process has been finished")

# ------------------------------------------------------------------
# End of daily data process


# ------------------------------------------------------------------
# Notification Email

run_sendEmailNotification = \
    subprocess.run('//db-rb-fs001/data_qlik_desktop/data_source_apps/'
                   '_scripts/daily_data_processing/send_emailNotification.py', shell=True,
                   capture_output=True)

if run_sendEmailNotification.returncode != 0:
    logger.error(f"Module send_emailNotification did not ran successfully")
else:
    logger.info(f"Module send_emailNotification did ran successfully")
