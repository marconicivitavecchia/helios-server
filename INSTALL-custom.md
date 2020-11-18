# Start at boot on ubuntu
```sh
cp systemd-files/helios.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable helios
systemctl start helios
```
