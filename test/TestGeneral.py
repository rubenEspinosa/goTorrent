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
    peer4 = h.spawn('peer4', Peer)
    peer5 = h.spawn('peer5', Peer)

    modo = str(raw_input("por favor indique si desea usar push, pull o push-pull: "))

    peer.set_mode(modo)
    peer2.set_mode(modo)
    peer3.set_mode(modo)
    peer4.set_mode(modo)
    peer5.set_mode(modo)

    peer.attach_tracker(tracker)
    peer2.attach_tracker(tracker)
    peer3.attach_tracker(tracker)
    peer4.attach_tracker(tracker)
    peer5.attach_tracker(tracker)

    peer.set_file("1a")
    peer2.set_file("1a")
    peer3.set_file("1a")
    peer4.set_file("1a")
    peer5.set_file("1a")

    f = open('chunksFile', 'r').read()

    peer.set_size(f.__len__())
    peer2.set_size(f.__len__())
    peer3.set_size(f.__len__())
    peer4.set_size(f.__len__())
    peer5.set_size(f.__len__())

    for i in range (0,f.__len__()):
        peer.add_chunk(i, f[i])

    tracker.announce('1a','peer')
    tracker.announce('1a','peer2')
    tracker.announce('1a','peer3')
    tracker.announce('1a', 'peer4')
    tracker.announce('1a', 'peer5')

    peer.init_gossip_cycle()
    peer2.init_gossip_cycle()
    peer3.init_gossip_cycle()
    peer4.init_gossip_cycle()
    peer5.init_gossip_cycle()

    sleep(16)

    peer.stop_interval()
    peer2.stop_interval()
    peer3.stop_interval()
    peer4.stop_interval()
    peer5.stop_interval()

    print peer5.get_chunks(timeout=5)
    print peer4.get_chunks(timeout=5)
    print peer3.get_chunks(timeout=5)
    print peer2.get_chunks(timeout=5)
    print peer.get_chunks(timeout=5)

    print peer.get_values(timeout=5)
    print peer2.get_values(timeout=5)
    print peer3.get_values(timeout=5)
    print peer4.get_values(timeout=5)
    print peer5.get_values(timeout=5)

    shutdown()