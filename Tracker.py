import random
from pyactor.context import interval



class Tracker(object):
    _tell = ['announce','update','init_start']
    _ask = ['get_peers']
    _ref = ['announce']


    def __init__(self):
        self.torrent = {}

    def init_start(self):
        self.time = interval(self.host, 1, self.proxy, "update")

    def announce(self,torrent_hash,peer_ref):
        if not self.torrent.has_key(torrent_hash):
            self.torrent[torrent_hash] = {}
        self.torrent[torrent_hash][peer_ref]=10

    def get_peers(self,torrent_hash):
        #keys = self.torrent[torrent_hash].keys()
        #return keys
        try:
            return random.sample(self.torrent[torrent_hash].keys(), 10)
        except:
            return self.torrent[torrent_hash].keys()



    def update(self):
        print self.torrent
        for i in self.torrent.keys():
            for j in self.torrent[i].keys():
                self.torrent[i][j] -= 1
                if self.torrent[i][j] <= 0:
                    self.torrent[i].pop(j)