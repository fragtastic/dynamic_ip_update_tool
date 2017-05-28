#!/usr/bin/env python2

from urllib2 import urlopen

CONFIG = '/etc/dynamic_ip_tool/dynip.conf'
LASTIP = '/etc/dynamic_ip_tool/lastip'
URL = 'https://dynamicdns.park-your-domain.com/update?domain={domain}&password={password}&host={host}&ip={ip}'

ip_current = urlopen('http://ip.42.pl/raw').read()

with open(LASTIP, 'r+') as l:
    ip_last = l.read().strip('\n')
    if ip_current != ip_last:
        l.seek(0)
        l.write(ip_current)
        l.truncate()
        with open(CONFIG) as c:
            lines = [line.strip('\n').split(' ') for line in c]
            for line in lines:
                for host in line[2:]:
                    print('Updating host "{host}" on domain "{domain}" with ip "{ip}"'.format(domain=line[0], host=host, ip=ip_current))
                    urlopen(URL.format(domain=line[0], password=line[1], host=host, ip=ip_current)).read()
