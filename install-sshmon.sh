#install sshmon
# do not run as sudo!

mkdir sshmon
cd sshmon
sudo apt install python3-pip
pip3 install load_dotenv
pip3 install discord-webhook
wget https://raw.githubusercontent.com/p27182/monitoring/main/sshmon.py
wget https://raw.githubusercontent.com/p27182/monitoring/main/sshmon.service
wget https://raw.githubusercontent.com/p27182/monitoring/main/.env
sudo mv sshmon.service /lib/systemd/system/sshmon.service
sudo systemctl daemon-reload
sudo systemctl enable sshmon
echo "Add the webhook url to .env file and start the sshmon service"
pause
#sudo systemctl start sshmon
