# dynamic_ip_update_tool
Updates a Namecheap dynamic record.

## Installation
Place `dynamic_ip_tool.py` wherever you should for your distro.
Debian $PATH for root is `/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`. So `/usr/local/sbin/dynamic_ip_tool.py` should be fine.
Create folder `sudo mkdir /etc/dynamic_ip_tool` and place your config inside.

## Config
The configuration file at `/etc/dynamic_ip_tool/dynip.conf` should only be readable and writable by root.

Example configuration file. Multiple hosts can be specified on the same line.
```
DOMAIN1 PASSWORD1 HOST11 HOST12 HOST13 HOST14
DOMAIN2 PASSWORD2 HOST21 HOST22 HOST23 HOST24
```

## Usage
Just run it in cron however often you feel like it. Once a minute or every few should be fine.\
Add your line to crontab with `sudo crontab -e`.

Every minute `* * * * * dynamic_ip_tool.py`\
Every 5 minutes `*/5 * * * * dynamic_ip_tool.py`\
See https://crontab.guru/ for help with crontab and more examples.
