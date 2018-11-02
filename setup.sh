# add crontab for running every read seconds or something

# MAC run job: https://alvinalexander.com/mac-os-x/mac-osx-startup-crontab-launchd-jobs
# linux?: https://stackoverflow.com/questions/4880290/how-do-i-create-a-crontab-through-a-script or (crontab -l 2>/dev/null; echo "*/5 * * * * /path/to/job -with args") | crontab -

echo "Installing requirements"
pip3 install -r requirements.txt

echo "Making folder"
mkdir ~/.pyWebWatch

echo "Making service file executable"
chmod +x pyWebWatch.py
