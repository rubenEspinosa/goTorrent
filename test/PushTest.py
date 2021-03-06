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

    peer.set_mode("push")
    peer2.set_mode("push")
    peer3.set_mode("push")

    peer.attach_tracker(tracker)
    peer2.attach_tracker(tracker)
    peer3.attach_tracker(tracker)

    peer.set_file("1a")
    peer2.set_file("1a")
    peer3.set_file("1a")

    peer.set_size(7)
    peer2.set_size(7)
    peer3.set_size(7)

    peer.init_gossip_cycle()
    peer2.init_gossip_cycle()
    peer3.init_gossip_cycle()

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

    #peer2.push(3, "C")
    #peer3.push(6, "F")
    #peer3.push(1, "A")

    sleep(10)


    print peer3.get_chunks()
    print peer2.get_chunks()
    print peer.get_chunks()



shutdown()