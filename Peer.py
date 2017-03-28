import random
from pyactor.context import interval

class Peer(object):
    _tell = ['init_gossip_cycle','attach_tracker','propagate_chunk','add_chunk','push','pull','set_mode']
    _ask = ['get_chunks','get_values','get_chunk']
    _ref = ['attach_tracker']


    def __init__(self):
        self.file = "1a"
        self.size = 7
        self.chunks = {}    #conte la llista de chunks que te el peer

    def set_mode(self,operation):
        self.operation = operation

    def init_gossip_cycle(self):
        self.time = interval(self.host, 1, self.proxy, "propagate_chunk")

    def propagate_chunk(self):
        if self.operation=="push":
            var = random.choice(self.chunks.keys())
            self.push(var, self.chunks[var])
        elif self.operation=="pull":
            chunk=random.randint(1,self.size-1)
            self.pull(chunk)
        else:
            pass

    def push(self,chunk_id,chunk_data):
        peers = self.tracker.get_peers(self.file)
        try:
            peers.remove(self.id)
        except:
            pass
        finally:
            for peerStr in peers:
                peerRef = self.host.lookup(peerStr)
                peerRef.add_chunk(chunk_id,chunk_data)

    def pull(self,chunk_id):
        peers=self.tracker.get_peers(self.file)
        try:
            peers.remove(self.id)
        except:
            pass
        finally:
            for i in peers:
                peerRef = self.host.lookup(i)
                future = peerRef.get_chunk(chunk_id, future=True)
                future.add_callback('pong')

    def add_chunk(self,chunk_id,chunk_data):
        if not self.chunks.has_key(chunk_id):
            self.chunks[chunk_id] = chunk_data

    def attach_tracker(self, tracker):
        self.tracker = tracker

    def get_chunks(self):
        return self.chunks

    def get_chunk(self,chunk_id):
        return (chunk_id, self.chunks[chunk_id])

    def get_values(self):
        string = ""
        for i in self.chunks.values():
            string = string + i
        return string

    def pong(self,future):
        msg = future.result()
        self.add_chunk(msg.__getitem__(0), msg.__getitem__(1))






