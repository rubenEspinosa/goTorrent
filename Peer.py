from random import randint

class Peer(object):
    _tell = ['init_gossip_cycle','push','add_chunk','attach_tracker']
    _ask = ['pull','get_chunks','get_values']
    _ref = ['attach_tracker']


    def __init__(self):
        self.operation = "push"
        self.chunks = {}    #conte la llista de chunks que te el peer

    def init_gossip_cycle(self):
        self.time = self.host.interval(1, self.proxy, "propagate_chunk")

    def propagate_chunk(self):
        array = self.chunks.keys()
        var = randint(0, array.__len__()-1)
        if self.operation=="push":
            self.push(var, self.chunks[var])
        else:
            pass

    def push(self,chunk_id,chunk_data):
        peers= self.tracker.get_peers()
        for peer in peers:
            peer.add_chunk(chunk_id,chunk_data)
            #self.tracker[peer].add_chunk(chunk_id,chunk_data)

    def pull(self,chunk_id):
        print "hola"

    def add_chunk(self,chunk_id,chunk_data):
        if not self.chunks.has_key(chunk_id):
            self.chunks[chunk_id] = chunk_data

    def attach_tracker(self, tracker):
        self.tracker = tracker

    def get_chunks(self):
        return self.chunks

    def get_values(self):
        string = ""
        for i in self.chunks.values():
            string = string + i
        return string





