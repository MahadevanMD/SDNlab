"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.clean import Cleanup

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        # pod 0
        host01 = self.addHost( 'h01' )
        host02 = self.addHost( 'h02' )
        host03 = self.addHost( 'h03' )
        host04 = self.addHost( 'h04' )
        aggr01 = self.addSwitch( 's2001' )
        aggr02 = self.addSwitch( 's2002' )
        edge01 = self.addSwitch( 's3001' )
        edge02 = self.addSwitch( 's3002' )
        # Pod 1
        host11 = self.addHost( 'h11' )
        host12 = self.addHost( 'h12' )
        host13 = self.addHost( 'h13' )
        host14 = self.addHost( 'h14' )
        aggr11 = self.addSwitch( 's2003' )
        aggr12 = self.addSwitch( 's2004' )
        edge11 = self.addSwitch( 's3003' )
        edge12 = self.addSwitch( 's3004' )
        # Pod 2
        host21 = self.addHost( 'h21' )
        host22 = self.addHost( 'h22' )
        host23 = self.addHost( 'h23' )
        host24 = self.addHost( 'h24' )
        aggr21 = self.addSwitch( 's2005' )
        aggr22 = self.addSwitch( 's2006' )
        edge21 = self.addSwitch( 's3005' )
        edge22 = self.addSwitch( 's3006' )
        # Pod 3
        host31 = self.addHost( 'h31' )
        host32 = self.addHost( 'h32' )
        host33 = self.addHost( 'h33' )
        host34 = self.addHost( 'h34' )
        aggr31 = self.addSwitch( 's2007' )
        aggr32 = self.addSwitch( 's2008' )
        edge31 = self.addSwitch( 's3007' )
        edge32 = self.addSwitch( 's3008' )
        # Add core switches
        core0 = self.addSwitch( 's1001' )
        core1 = self.addSwitch( 's1002' )
        core2 = self.addSwitch( 's1003' )
        core3 = self.addSwitch( 's1004' )

        # Add links
        ## Pod 0 - host to edge
        self.addLink( host01, edge01, bw=100)
        self.addLink( host02, edge01, bw=100)
        self.addLink( host03, edge02, bw=100)
        self.addLink( host04, edge02, bw=100)
        # Pod 0 - edge to aggregation
        self.addLink( edge01, aggr01, bw=100)
        self.addLink( edge01, aggr02, bw=100)
        self.addLink( edge02, aggr01, bw=100)
        self.addLink( edge02, aggr02, bw=100)
        # Pod 0 - aggregation to core
        self.addLink( aggr01, core0, bw=1000, lost=2)
        self.addLink( aggr01, core1, bw=1000, lost=2)
        self.addLink( aggr02, core2, bw=1000, lost=2)
        self.addLink( aggr02, core3, bw=1000, lost=2)

        ## Pod 1 - host to edge
        self.addLink( host11, edge11, bw=100)
        self.addLink( host12, edge11, bw=100)
        self.addLink( host13, edge12, bw=100)
        self.addLink( host14, edge12, bw=100)
        # Pod 1 - edge to aggregation
        self.addLink( edge11, aggr11, bw=100)
        self.addLink( edge11, aggr12, bw=100)
        self.addLink( edge12, aggr11, bw=100)
        self.addLink( edge12, aggr12, bw=100)
        # Pod 1 - aggregation to core
        self.addLink( aggr11, core0, bw=1000, lost=2)
        self.addLink( aggr11, core1, bw=1000, lost=2)
        self.addLink( aggr12, core2, bw=1000, lost=2)
        self.addLink( aggr12, core3, bw=1000, lost=2)

        ## Pod 2 - host to edge
        self.addLink( host21, edge21, bw=100)
        self.addLink( host22, edge21, bw=100)
        self.addLink( host23, edge22, bw=100)
        self.addLink( host24, edge22, bw=100)
        # Pod 2 - edge to aggregation
        self.addLink( edge21, aggr21, bw=100)
        self.addLink( edge21, aggr22, bw=100)
        self.addLink( edge22, aggr21, bw=100)
        self.addLink( edge22, aggr22, bw=100)
        # Pod 2 - aggregation to core
        self.addLink( aggr21, core0, bw=1000, lost=2)
        self.addLink( aggr21, core1, bw=1000, lost=2)  
        self.addLink( aggr22, core2, bw=1000, lost=2) 
        self.addLink( aggr22, core3, bw=1000, lost=2)

        ## Pod 3 - host to edge
        self.addLink( host31, edge31, bw=100)
        self.addLink( host32, edge31, bw=100)
        self.addLink( host33, edge32, bw=100)
        self.addLink( host34, edge32, bw=100)
        # Pod 3 - edge to aggregation
        self.addLink( edge31, aggr31, bw=100)
        self.addLink( edge31, aggr32, bw=100)
        self.addLink( edge32, aggr31, bw=100)
        self.addLink( edge32, aggr32, bw=100)
        # Pod 3 - aggregation to core
        self.addLink( aggr31, core0, bw=1000, loss=2)
        self.addLink( aggr31, core1, bw=1000, loss=2)
        self.addLink( aggr32, core2, bw=1000, loss=2)
        self.addLink( aggr32, core3, bw=1000, loss=2)

def perfTest():
    topo = MyTopo()
    net = Mininet(topo=topo, link=TCLink, controller=None)
    net.addController('mycontroller',controller=RemoteController,ip='127.0.0.1')
    net.start()

    print('Dumping host connections')
    dumpNodeConnections(net.hosts)
    print('Testing network connectivity')
    net.pingFull()
    print('Testing bandwidth between pods')
    h01, h02, h31 = net.get('h01','h02','h31')
    # iperf server1 in pod 0
    h01.popen('iperf -s -u -i 1 > diff_pod', shell=True)
    # iperf server2 in pod 3
    h31.popen('iperf -s -u -i 1 > same_pod', shell=True)
    # iperf client send to server1 & server2
    h02.cmdPrint('iperf -c ' + h01.IP() + ' -u -t 10 -i 1 -b 100m')
    h02.cmdPrint('iperf -c ' + h31.IP() + ' -u -t 10 -i 1 -b 100m')
    net.stop()
    Cleanup()

if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
