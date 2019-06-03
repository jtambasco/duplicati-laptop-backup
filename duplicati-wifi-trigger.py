#!/usr/bin/env python3

import os
import datetime
import pathlib
import time

# Backup command downloaded from the web interface
duplicati_command = 'put your duplicati command from the web interface here'

# Time [s] to allow to ensure mounting is done
wait = 30

# Directory to check if mounted (exists) before calling duplicati
directory = '/mnt/xxx'

# User that is running duplicati
user = 'your username'

# Directory to save log files
dispatch_directory = '/home/%s/duplicati-laptop-backup/' % user

time.sleep(wait)

# Script files
prefix = os.path.basename(__file__)
log_file = dispatch_directory + prefix + '.log'
done_file = dispatch_directory + prefix + '.done'

# Check if backup ran today already
done_today = True
if os.path.exists(done_file):
    print('Done file exists...')
    t = os.path.getmtime(done_file)
    date = datetime.date.fromtimestamp(t)
    today_date = datetime.date.today()
    if date != today_date:
        done_today = False
else:
    print('Done file does not exist...')
    done_today = False

# Check if backup location is mounted
print('Checking if directory is mounted...')
mounted = os.path.isdir(directory)

# Run duplicati if necessary
do_backup = not done_today and mounted
print('done_today: ' + str(done_today) + ', Mounted: ' + str(mounted))
print('Perform backup? ' + str(do_backup))
if do_backup:
    print('Running backup...')
    os.system(duplicati_command + ' > ' + log_file)

    # Check logfile for successful backup
    last_line_log = subprocess.check_output(['tail', '-1', log_file]).decode().strip()
    if last_line_log == 'Backup completed successfully!':
        # Create done file
        print('Backup successful.')
        print('Creating done file...')
        pathlib.Path(done_file).touch()
    else:
        print('Backup unsuccessful.')
elif not mounted:
    print('Drive not mounted.')
elif done_today:
    print('Backup already run for today.')

print('Exiting...')
