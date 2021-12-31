import os
import shutil
from datetime import date, datetime
import logging

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

logger.addHandler(file_handler)

# ------------------------------------------------------------------
# Moving Suite8 H.ostel OTB file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/suite8/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/expected_otb_room_nights/H.ostel/'
dst2 = '//dwa-hq-ql001/QlikSenseDaten/Daily-Revenuemanagement-Summary/Hostel/hist_fore/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("OTB_h.ostel") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.copy2(src + entry.name, dst2 + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Suite8 H.ostel OTB file(s) has been moved")

# ------------------------------------------------------------------
# Moving Suite8 H.ostel DEFTEN File

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/suite8/'
dst = '//db-rb-fs001/Revenue_Anlyse/Strategy Sheet/non-Opera/H.ostel/Sources/DEFTEN_2021_2022/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("DEFTEN_") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Suite8 H.ostel DEFTEN file(s) has been moved")

# ------------------------------------------------------------------
# Moving Suite8 H.ostel Availability File

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/suite8/'
dst = '//db-rb-fs001/Revenue_Anlyse/Strategy Sheet/non-Opera/H.ostel/Sources/Availability_2021_2022/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("Availability_2021_2022") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} Suite8 H.ostel Availability file(s) has been moved")

# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Moving r_a rev flash files

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/revenue_flash_report/new_reports/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("rev_flash") != -1:
            shutil.copy2(src + entry.name, dst + entry.name)
            shutil.move(src + entry.name, src + "store/" + entry.name)
            file_counter += 1

logger.info(f"{file_counter} r_a rev flash file(s) has been moved")

# ------------------------------------------------------------------
# duetto forecast file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/duetto/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/duetto_forecast_dev/monthly/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ForecastSnapshot") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)
            file_date = date.fromisoformat(entry.name[0:10]).strftime("%d.%m.%Y")
            os.rename(src + entry.name,src + "ForecastSnapshotMonthly_" + file_date + ".csv")
            file_counter += 1

logger.info(f"{file_counter} duetto forecast file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("ForecastSnapshot") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} duetto forecast file(s) has been moved")

# ------------------------------------------------------------------
# duetto current rate file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/duetto/'
dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/drr_pilot/CurrentRate/'

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)
            if date.fromisoformat(entry.name[0:10]) != date.today():
                os.remove(src + entry.name)
                file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been removed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            os.rename(src + entry.name,src + "CurrentRateReport" + ".csv")
            file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("CurrentRate") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} duetto current rate file(s) has been moved")

# ------------------------------------------------------------------
# revenue past 91 days Jan Heimbeck file

src = '//db-rb-fs001/data_qlik_desktop/data_source_apps/_mailAttachments/r_a/'
dst = '//db-rb-fs001/revenue_Anlyse/Aktuelle Dailys/Jan Heimbeck/'

with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("revenue_past_91_days_D_A") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)
        if entry.is_file() and entry.name.find("revenue_past_91") != -1:
            shutil.copy2(src + entry.name, src + "store/" + entry.name)


file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("revenue_past_91_days_D_A") != -1:
            os.rename(src + entry.name, src + "revenue_past_91_days_D_A.csv")
            file_counter += 1
        if entry.is_file() and entry.name.find("revenue_past_91") != -1:
            os.rename(src + entry.name, src + "revenue_past_91_days.csv")
            file_counter += 1

logger.info(f"{file_counter} revenue past 91 days files have been renamed")

file_counter = 0
with os.scandir(src) as it:
    for entry in it:
        if entry.is_file() and entry.name.find("revenue_past_91_days_D_A") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1
        if entry.is_file() and entry.name.find("revenue_past_91") != -1:
            shutil.move(src + entry.name, dst + entry.name)
            file_counter += 1

logger.info(f"{file_counter} revenue past 91 days files have been moved")




