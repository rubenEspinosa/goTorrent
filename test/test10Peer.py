from pyactor.context import set_context, create_host, sleep, shutdown
from Peer import *
from Tracker import *

if __name__ == "__main__":
   set_context()
   h = create_host()

   tracker = h.spawn("tracker1", Tracker)
   peer0 = h.spawn("peer0", Peer)
   peer1 = h.spawn("peer1", Peer)
   peer2 = h.spawn("peer2", Peer)
   peer3 = h.spawn("peer3", Peer)
   peer4 = h.spawn("peer4", Peer)
   peer5 = h.spawn("peer5", Peer)
   peer6 = h.spawn("peer6", Peer)
   peer7 = h.spawn("peer7", Peer)
   peer8 = h.spawn("peer8", Peer)
   peer9 = h.spawn("peer9", Peer)

   modo = str(raw_input("por favor indique si desea usar push, pull o push-pull: "))
   peer0.set_mode(modo)
   peer1.set_mode(modo)
   peer2.set_mode(modo)
   peer3.set_mode(modo)
   peer4.set_mode(modo)
   peer5.set_mode(modo)
   peer6.set_mode(modo)
   peer7.set_mode(modo)
   peer8.set_mode(modo)
   peer9.set_mode(modo)

   peer0.attach_tracker(tracker)
   peer1.attach_tracker(tracker)
   peer2.attach_tracker(tracker)
   peer3.attach_tracker(tracker)
   peer4.attach_tracker(tracker)
   peer5.attach_tracker(tracker)
   peer6.attach_tracker(tracker)
   peer7.attach_tracker(tracker)
   peer8.attach_tracker(tracker)
   peer9.attach_tracker(tracker)

   peer0.set_file("1a")
   peer1.set_file("1a")
   peer2.set_file("1a")
   peer3.set_file("1a")
   peer4.set_file("1a")
   peer5.set_file("1a")
   peer6.set_file("1a")
   peer7.set_file("1a")
   peer8.set_file("1a")
   peer9.set_file("1a")

   f = open("chunksFile", "r").read()

   for i in range (0,f.__len__()):
      peer0.add_chunk(i, f[i])

   peer0.set_size(f.__len__())
   peer1.set_size(f.__len__())
   peer2.set_size(f.__len__())
   peer3.set_size(f.__len__())
   peer4.set_size(f.__len__())
   peer5.set_size(f.__len__())
   peer6.set_size(f.__len__())
   peer7.set_size(f.__len__())
   peer8.set_size(f.__len__())
   peer9.set_size(f.__len__())

   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")
   tracker.announce("1a","peer$i")

   peer0.init_gossip_cycle()
   peer1.init_gossip_cycle()
   peer2.init_gossip_cycle()
   peer3.init_gossip_cycle()
   peer4.init_gossip_cycle()
   peer5.init_gossip_cycle()
   peer6.init_gossip_cycle()
   peer7.init_gossip_cycle()
   peer8.init_gossip_cycle()
   peer9.init_gossip_cycle()

   sleep(33)

   print peer0.get_chunks()
   print peer1.get_chunks()
   print peer2.get_chunks()
   print peer3.get_chunks()
   print peer4.get_chunks()
   print peer5.get_chunks()
   print peer6.get_chunks()
   print peer7.get_chunks()
   print peer8.get_chunks()
   print peer9.get_chunks()

   print peer0.get_values()
   print peer1.get_values()
   print peer2.get_values()
   print peer3.get_values()
   print peer4.get_values()
   print peer5.get_values()
   print peer6.get_values()
   print peer7.get_values()
   print peer8.get_values()
   print peer9.get_values()

   shutdown()