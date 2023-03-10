#install sshmon
# do not run as sudo!

pip install discord-webhook
wget https://raw.githubusercontent.com/p27182/monitoring/main/sshmon.py
wget https://raw.githubusercontent.com/p27182/monitoring/main/sshmon.service

sudo mv sshmon.service /lib/systemd/system/sshmon.service
sudo systemctl daemon-reload
sudo systemctl enable sshmon
sudo systemctl start sshmon
