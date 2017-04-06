import random
from pyactor.context import interval

class Peer(object):
    _tell = ['set_file','set_mode','set_size','attach_tracker','add_chunk','announce','init_gossip_cycle','propagate_chunk','push','pull']
    _ask = ['get_chunks','get_chunk','get_values']
    _ref = ['attach_tracker']

    def __init__(self):
        self.chunks = {}    #conte la llista de chunks que te el peer

    def set_file(self,file):
        self.file = file

    def set_mode(self,operation):
        self.operation = operation

    def set_size(self,torrent_size):
        self.size = torrent_size

    def attach_tracker(self,tracker):
        self.tracker = tracker

    def add_chunk(self,chunk_id,chunk_data):
        if not self.chunks.has_key(chunk_id):
            self.chunks[chunk_id] = chunk_data

    def get_chunks(self):
        return self.chunks

    def get_chunk(self,chunk_id):
        return (chunk_id, self.chunks[chunk_id])

    def get_values(self):
        string = ""
        for i in self.chunks.values():
            string = string + i
        return string

    def announce(self):
        self.tracker.announce(self.file, self.id)

    def init_gossip_cycle(self):
        self.time = interval(self.host, 2, self.proxy, "propagate_chunk")
        self.time2 = interval(self.host, 5, self.proxy, "announce")

    def propagate_chunk(self):
        if self.operation=="push" or self.operation=="push-pull":
            try:
                var = random.choice(self.chunks.keys())
                self.push(var, self.chunks[var])
            except:
                pass
            finally:
                pass

        if self.operation=="pull" or self.operation=="push-pull":
            chunk=random.randint(0,self.size-1)
            self.pull(chunk)

    def push(self,chunk_id,chunk_data):
        peers = self.tracker.get_peers(self.file)
        try:
            peers.remove(self.id)
        except:
            pass
        finally:
            for peerStr in peers:
                try:
                    peerRef = self.host.lookup(peerStr)
                    peerRef.add_chunk(chunk_id,chunk_data)
                except:
                    pass
                finally:
                    pass

    def pull(self,chunk_id):
        peers=self.tracker.get_peers(self.file)
        try:
            peers.remove(self.id)
        except:
            pass
        finally:
            for i in peers:
                try:
                    peerRef = self.host.lookup(i)
                    future = peerRef.get_chunk(chunk_id, future=True)
                    future.add_callback('pong')
                except:
                    pass
                finally:
                    pass

    def pong(self,future):
        try:
            msg = future.result()
            self.add_chunk(msg.__getitem__(0), msg.__getitem__(1))
        except:
            pass
        finally:
            pass
