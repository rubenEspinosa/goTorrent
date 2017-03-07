from random import randint



class Tracker(object):
    _tell = ['announce','update','init_start']
    _ask = ['get_peers']
    _ref = ['announce']


    def __init__(self):
        self.peers = {}

    def init_start(self):
        self.time = self.host.interval(1, self.proxy, "update")

    def announce(self,torrent_hash,peer_ref):
        if not self.peers.has_key(torrent_hash):
            self.peers[torrent_hash] = {}
        self.peers[torrent_hash][peer_ref]=10
        print self.peers

    def get_peers(self,torrent_hash):
        array=[]
        keys = self.peers.get(torrent_hash).keys()
        #if keys.__len__() < 10 : lenght= keys.__len__()
        #else: lenght=10
        #for i in range(1,lenght):
        #    array.append(randint(0,keys.__len__()))
       # array
        print keys
        return keys

    def update(self):
        for i in self.peers.keys():
            for j in self.peers[i].keys():
                self.peers[i][j] -= 1
                if self.peers[i][j] <= 0:
                    self.peers[i].pop(j)