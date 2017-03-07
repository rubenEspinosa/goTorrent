from pyactor.context import set_context, create_host, sleep, shutdown
from Peer import *
from Tracker import *


if __name__ == "__main__":
    set_context()
    h = create_host()
    tracker = h.spawn('tracker1', Tracker)
    peer = h.spawn('peer', Peer)
    peer.attach_tracker(tracker)
    peer.add_chunk(1,"B")
    peer.init_gossip_cycle()

#Comprovar lordre descriptura
    peer.add_chunk(6, "F")
    peer.add_chunk(1, "A")
    peer.add_chunk(2, "B")
    peer.add_chunk(3, "C")
    peer.add_chunk(4, "D")
    peer.add_chunk(5, "E")
    peer.add_chunk(7, "G")

    print peer.get_chunks()
    print peer.get_values()

    shutdown()
