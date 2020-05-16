from l3ns.ldc import DockerNode, DockerSubnet
from l3ns import defaults
from l3ns.base.network import Network, NetworkConcurrent
import os

dockers = []
nodes = 4 
defaults.network = Network('15.0.0.0/8')

s = DockerSubnet(name='polygon', size=10)

# create network nodes
# node1 = DockerNode('node1', image='env_neo_go_image',
#                         ports={'20333/tcp': 20333, '30333/tcp': 30333, '20001/tcp': 20001},
#                         volumes={os.getcwd()+'/config/protocol.privnet.docker.one.yml':{'bind':'/config/protocol.privnet.docker.yml', 'mode':'ro'}, os.getcwd()+'/config/wallet1.json':{'bind':'/wallet1.json', 'mode':'ro'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
# node2 = DockerNode('node2', image='env_neo_go_image',
#                         ports={'20334/tcp': 20334, '30334/tcp': 30334, '20002/tcp': 20002},
#                         volumes={os.getcwd()+'/config/protocol.privnet.docker.two.yml':{'bind':'/config/protocol.privnet.docker.yml', 'mode':'ro'}, os.getcwd()+'/config/wallet2.json':{'bind':'/wallet2.json', 'mode':'ro'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
# node3 = DockerNode('node3', image='env_neo_go_image',
#                         ports={'20335/tcp': 20335, '30335/tcp': 30335, '20003/tcp': 20003},
#                         volumes={os.getcwd()+'/config/protocol.privnet.docker.one.yml':{'bind':'/config/protocol.privnet.docker.yml', 'mode':'ro'}, os.getcwd()+'/config/wallet1.json':{'bind':'/wallet3.json', 'mode':'ro'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
# node4 = DockerNode('node4', image='env_neo_go_image',
#                         ports={'20336/tcp': 20336, '30336/tcp': 30336, '20004/tcp': 20004},
#                         volumes={os.getcwd()+'/config/protocol.privnet.docker.one.yml':{'bind':'/config/protocol.privnet.docker.yml', 'mode':'ro'}, os.getcwd()+'/config/wallet1.json':{'bind':'/wallet4.json', 'mode':'ro'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')

node1 = DockerNode('node1', image='env_neo_go_image',
                        ports={'20333/tcp': 20333, '30333/tcp': 30333, '20001/tcp': 20001},
                        volumes={os.getcwd()+'/config/protocol.privnet.docker.one.yml':{'bind':'/config/protocol.privnet.yml', 'mode':'ro'}, os.getcwd()+'/.docker/wallets/wallet1.json':{'bind':'/wallet1.json','mode':'rw'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
node2 = DockerNode('node2', image='env_neo_go_image',
                        ports={'20334/tcp': 20334, '30334/tcp': 30334, '20002/tcp': 20002},
                        volumes={os.getcwd()+'/config/protocol.privnet.docker.two.yml':{'bind':'/config/protocol.privnet.yml', 'mode':'ro'}, os.getcwd()+'/.docker/wallets/wallet2.json':{'bind':'/wallet2.json','mode':'rw'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
node3 = DockerNode('node3', image='env_neo_go_image',
                        ports={'20335/tcp': 20335, '30335/tcp': 30335, '20003/tcp': 20003},
                        volumes={os.getcwd()+'/config/protocol.privnet.docker.three.yml':{'bind':'/config/protocol.privnet.yml', 'mode':'ro'}, os.getcwd()+'/.docker/wallets/wallet3.json':{'bind':'/wallet3.json', 'mode':'rw'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')
node4 = DockerNode('node4', image='env_neo_go_image',
                        ports={'20336/tcp': 20336, '30336/tcp': 30336, '20004/tcp': 20004},
                        volumes={os.getcwd()+'/config/protocol.privnet.docker.four.yml':{'bind':'/config/protocol.privnet.yml', 'mode':'ro'}, os.getcwd()+'/.docker/wallets/wallet4.json':{'bind':'/wallet4.json','mode':'rw'}}, command='/usr/bin/privnet-entrypoint.sh node --config-path /config --privnet')

dockers.append(node1)
dockers.append(node2)
dockers.append(node3)
dockers.append(node4)

for i in range(nodes):
    s.add_node(dockers[i])
        #dockers[i].connect_to(dockers[(i+1) % nodes])

for i in range(nodes):
    print('node ' + str(i)+ ' ' + str(dockers[i].get_ip()))

defaults.network.start(interactive=True)

