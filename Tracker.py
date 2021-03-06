import random
from pyactor.context import interval


class Tracker(object):
    _tell = ['announce','init_start','update']
    _ask = ['get_peers']
    _ref = ['announce']

    def __init__(self):
        self.torrent = {}

    def announce(self,torrent_hash,peer_ref):
        if not self.torrent.has_key(torrent_hash):
            self.torrent[torrent_hash] = {}
        self.torrent[torrent_hash][peer_ref]=10

    def init_start(self):
        self.time = interval(self.host, 1, self.proxy, "update")

    def get_peers(self,torrent_hash):
        keys= self.torrent[torrent_hash].keys()
        if keys.__len__() > 10:
            return random.sample(keys, 10)
        else:
            return keys

    def update(self):
        for i in self.torrent.keys():
            for j in self.torrent[i].keys():
                self.torrent[i][j] -= 1
                if self.torrent[i][j] <= 0:
                    self.torrent[i].pop(j)
