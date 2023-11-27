#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from containernet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)
info('*** Adding controller\n')
net.addController('c0')
info('*** Adding docker containers\n')
d1 = net.addDocker('d1', ip='10.0.0.251', dimage="clientes", mem_limit="512m", memswap_limit="1536m")
d2 = net.addDocker('d2', ip='10.0.0.252', dimage="clientes", mem_limit="2024m", memswap_limit="3072m")
d3 = net.addDocker('d3', ip='10.0.0.252', dimage="clientes")
#d4 = net.addDocker('d2', ip='10.0.0.252', dimage="server") #implementar servidor e app do servidor.
info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
info('*** Creating links\n')
net.addLink(d1, s1)
net.addLink(s1, s2, cls=TCLink)
net.addLink(s2, d2)
info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()