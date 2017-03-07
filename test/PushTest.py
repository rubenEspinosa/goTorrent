from pyactor.context import set_context, create_host, sleep, shutdown
from Peer import *
from Tracker import *

if __name__ == "__main__":
    set_context()
    h = create_host()
    tracker = h.spawn('tracker1', Tracker)
    peer = h.spawn('peer', Peer)
    peer2 = h.spawn('peer2', Peer)
    peer3 = h.spawn('peer3', Peer)
    peer.attach_tracker(tracker)
    peer2.attach_tracker(tracker)
    peer3.attach_tracker(tracker)


    tracker.announce('1a','peer')
    tracker.announce('1a','peer2')
    tracker.announce('1a','peer3')



#peer es la seed
    peer.add_chunk(6, "F")
    peer.add_chunk(1, "A")
    peer.add_chunk(2, "B")
    peer.add_chunk(3, "C")
    peer.add_chunk(4, "D")
    peer.add_chunk(5, "E")
    peer.add_chunk(7, "G")

    peer2.add_chunk(3, "C")
    peer2.add_chunk(4, "D")
    peer2.add_chunk(5, "E")
    peer2.add_chunk(7, "G")

    peer3.add_chunk(6, "F")
    peer3.add_chunk(1, "A")
    peer3.add_chunk(7, "G")

    peer2.push(3, "C")

    print "chunks que tiene peer3"
    print peer3.get_values()                    #se han anadido los chunks de hacer push el peer2


    peer3.push(6, "F")
    peer3.push(1, "A")

    print "chunks que tiene peer2"
    print peer2.get_values()


    peer.init_gossip_cycle()



shutdown()