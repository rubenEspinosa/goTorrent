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
   peer10 = h.spawn("peer10", Peer)
   peer11 = h.spawn("peer11", Peer)
   peer12 = h.spawn("peer12", Peer)
   peer13 = h.spawn("peer13", Peer)
   peer14 = h.spawn("peer14", Peer)
   peer15 = h.spawn("peer15", Peer)
   peer16 = h.spawn("peer16", Peer)
   peer17 = h.spawn("peer17", Peer)
   peer18 = h.spawn("peer18", Peer)
   peer19 = h.spawn("peer19", Peer)
   peer20 = h.spawn("peer20", Peer)
   peer21 = h.spawn("peer21", Peer)
   peer22 = h.spawn("peer22", Peer)
   peer23 = h.spawn("peer23", Peer)
   peer24 = h.spawn("peer24", Peer)
   peer25 = h.spawn("peer25", Peer)
   peer26 = h.spawn("peer26", Peer)
   peer27 = h.spawn("peer27", Peer)
   peer28 = h.spawn("peer28", Peer)
   peer29 = h.spawn("peer29", Peer)
   peer30 = h.spawn("peer30", Peer)
   peer31 = h.spawn("peer31", Peer)
   peer32 = h.spawn("peer32", Peer)
   peer33 = h.spawn("peer33", Peer)
   peer34 = h.spawn("peer34", Peer)
   peer35 = h.spawn("peer35", Peer)
   peer36 = h.spawn("peer36", Peer)
   peer37 = h.spawn("peer37", Peer)
   peer38 = h.spawn("peer38", Peer)
   peer39 = h.spawn("peer39", Peer)
   peer40 = h.spawn("peer40", Peer)
   peer41 = h.spawn("peer41", Peer)
   peer42 = h.spawn("peer42", Peer)
   peer43 = h.spawn("peer43", Peer)
   peer44 = h.spawn("peer44", Peer)
   peer45 = h.spawn("peer45", Peer)
   peer46 = h.spawn("peer46", Peer)
   peer47 = h.spawn("peer47", Peer)
   peer48 = h.spawn("peer48", Peer)
   peer49 = h.spawn("peer49", Peer)
   peer50 = h.spawn("peer50", Peer)
   peer51 = h.spawn("peer51", Peer)
   peer52 = h.spawn("peer52", Peer)
   peer53 = h.spawn("peer53", Peer)
   peer54 = h.spawn("peer54", Peer)
   peer55 = h.spawn("peer55", Peer)
   peer56 = h.spawn("peer56", Peer)
   peer57 = h.spawn("peer57", Peer)
   peer58 = h.spawn("peer58", Peer)
   peer59 = h.spawn("peer59", Peer)
   peer60 = h.spawn("peer60", Peer)
   peer61 = h.spawn("peer61", Peer)
   peer62 = h.spawn("peer62", Peer)
   peer63 = h.spawn("peer63", Peer)
   peer64 = h.spawn("peer64", Peer)
   peer65 = h.spawn("peer65", Peer)
   peer66 = h.spawn("peer66", Peer)
   peer67 = h.spawn("peer67", Peer)
   peer68 = h.spawn("peer68", Peer)
   peer69 = h.spawn("peer69", Peer)
   peer70 = h.spawn("peer70", Peer)
   peer71 = h.spawn("peer71", Peer)
   peer72 = h.spawn("peer72", Peer)
   peer73 = h.spawn("peer73", Peer)
   peer74 = h.spawn("peer74", Peer)
   peer75 = h.spawn("peer75", Peer)
   peer76 = h.spawn("peer76", Peer)
   peer77 = h.spawn("peer77", Peer)
   peer78 = h.spawn("peer78", Peer)
   peer79 = h.spawn("peer79", Peer)
   peer80 = h.spawn("peer80", Peer)
   peer81 = h.spawn("peer81", Peer)
   peer82 = h.spawn("peer82", Peer)
   peer83 = h.spawn("peer83", Peer)
   peer84 = h.spawn("peer84", Peer)
   peer85 = h.spawn("peer85", Peer)
   peer86 = h.spawn("peer86", Peer)
   peer87 = h.spawn("peer87", Peer)
   peer88 = h.spawn("peer88", Peer)
   peer89 = h.spawn("peer89", Peer)
   peer90 = h.spawn("peer90", Peer)
   peer91 = h.spawn("peer91", Peer)
   peer92 = h.spawn("peer92", Peer)
   peer93 = h.spawn("peer93", Peer)
   peer94 = h.spawn("peer94", Peer)
   peer95 = h.spawn("peer95", Peer)
   peer96 = h.spawn("peer96", Peer)
   peer97 = h.spawn("peer97", Peer)
   peer98 = h.spawn("peer98", Peer)
   peer99 = h.spawn("peer99", Peer)

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
   peer10.set_mode(modo)
   peer11.set_mode(modo)
   peer12.set_mode(modo)
   peer13.set_mode(modo)
   peer14.set_mode(modo)
   peer15.set_mode(modo)
   peer16.set_mode(modo)
   peer17.set_mode(modo)
   peer18.set_mode(modo)
   peer19.set_mode(modo)
   peer20.set_mode(modo)
   peer21.set_mode(modo)
   peer22.set_mode(modo)
   peer23.set_mode(modo)
   peer24.set_mode(modo)
   peer25.set_mode(modo)
   peer26.set_mode(modo)
   peer27.set_mode(modo)
   peer28.set_mode(modo)
   peer29.set_mode(modo)
   peer30.set_mode(modo)
   peer31.set_mode(modo)
   peer32.set_mode(modo)
   peer33.set_mode(modo)
   peer34.set_mode(modo)
   peer35.set_mode(modo)
   peer36.set_mode(modo)
   peer37.set_mode(modo)
   peer38.set_mode(modo)
   peer39.set_mode(modo)
   peer40.set_mode(modo)
   peer41.set_mode(modo)
   peer42.set_mode(modo)
   peer43.set_mode(modo)
   peer44.set_mode(modo)
   peer45.set_mode(modo)
   peer46.set_mode(modo)
   peer47.set_mode(modo)
   peer48.set_mode(modo)
   peer49.set_mode(modo)
   peer50.set_mode(modo)
   peer51.set_mode(modo)
   peer52.set_mode(modo)
   peer53.set_mode(modo)
   peer54.set_mode(modo)
   peer55.set_mode(modo)
   peer56.set_mode(modo)
   peer57.set_mode(modo)
   peer58.set_mode(modo)
   peer59.set_mode(modo)
   peer60.set_mode(modo)
   peer61.set_mode(modo)
   peer62.set_mode(modo)
   peer63.set_mode(modo)
   peer64.set_mode(modo)
   peer65.set_mode(modo)
   peer66.set_mode(modo)
   peer67.set_mode(modo)
   peer68.set_mode(modo)
   peer69.set_mode(modo)
   peer70.set_mode(modo)
   peer71.set_mode(modo)
   peer72.set_mode(modo)
   peer73.set_mode(modo)
   peer74.set_mode(modo)
   peer75.set_mode(modo)
   peer76.set_mode(modo)
   peer77.set_mode(modo)
   peer78.set_mode(modo)
   peer79.set_mode(modo)
   peer80.set_mode(modo)
   peer81.set_mode(modo)
   peer82.set_mode(modo)
   peer83.set_mode(modo)
   peer84.set_mode(modo)
   peer85.set_mode(modo)
   peer86.set_mode(modo)
   peer87.set_mode(modo)
   peer88.set_mode(modo)
   peer89.set_mode(modo)
   peer90.set_mode(modo)
   peer91.set_mode(modo)
   peer92.set_mode(modo)
   peer93.set_mode(modo)
   peer94.set_mode(modo)
   peer95.set_mode(modo)
   peer96.set_mode(modo)
   peer97.set_mode(modo)
   peer98.set_mode(modo)
   peer99.set_mode(modo)

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
   peer10.attach_tracker(tracker)
   peer11.attach_tracker(tracker)
   peer12.attach_tracker(tracker)
   peer13.attach_tracker(tracker)
   peer14.attach_tracker(tracker)
   peer15.attach_tracker(tracker)
   peer16.attach_tracker(tracker)
   peer17.attach_tracker(tracker)
   peer18.attach_tracker(tracker)
   peer19.attach_tracker(tracker)
   peer20.attach_tracker(tracker)
   peer21.attach_tracker(tracker)
   peer22.attach_tracker(tracker)
   peer23.attach_tracker(tracker)
   peer24.attach_tracker(tracker)
   peer25.attach_tracker(tracker)
   peer26.attach_tracker(tracker)
   peer27.attach_tracker(tracker)
   peer28.attach_tracker(tracker)
   peer29.attach_tracker(tracker)
   peer30.attach_tracker(tracker)
   peer31.attach_tracker(tracker)
   peer32.attach_tracker(tracker)
   peer33.attach_tracker(tracker)
   peer34.attach_tracker(tracker)
   peer35.attach_tracker(tracker)
   peer36.attach_tracker(tracker)
   peer37.attach_tracker(tracker)
   peer38.attach_tracker(tracker)
   peer39.attach_tracker(tracker)
   peer40.attach_tracker(tracker)
   peer41.attach_tracker(tracker)
   peer42.attach_tracker(tracker)
   peer43.attach_tracker(tracker)
   peer44.attach_tracker(tracker)
   peer45.attach_tracker(tracker)
   peer46.attach_tracker(tracker)
   peer47.attach_tracker(tracker)
   peer48.attach_tracker(tracker)
   peer49.attach_tracker(tracker)
   peer50.attach_tracker(tracker)
   peer51.attach_tracker(tracker)
   peer52.attach_tracker(tracker)
   peer53.attach_tracker(tracker)
   peer54.attach_tracker(tracker)
   peer55.attach_tracker(tracker)
   peer56.attach_tracker(tracker)
   peer57.attach_tracker(tracker)
   peer58.attach_tracker(tracker)
   peer59.attach_tracker(tracker)
   peer60.attach_tracker(tracker)
   peer61.attach_tracker(tracker)
   peer62.attach_tracker(tracker)
   peer63.attach_tracker(tracker)
   peer64.attach_tracker(tracker)
   peer65.attach_tracker(tracker)
   peer66.attach_tracker(tracker)
   peer67.attach_tracker(tracker)
   peer68.attach_tracker(tracker)
   peer69.attach_tracker(tracker)
   peer70.attach_tracker(tracker)
   peer71.attach_tracker(tracker)
   peer72.attach_tracker(tracker)
   peer73.attach_tracker(tracker)
   peer74.attach_tracker(tracker)
   peer75.attach_tracker(tracker)
   peer76.attach_tracker(tracker)
   peer77.attach_tracker(tracker)
   peer78.attach_tracker(tracker)
   peer79.attach_tracker(tracker)
   peer80.attach_tracker(tracker)
   peer81.attach_tracker(tracker)
   peer82.attach_tracker(tracker)
   peer83.attach_tracker(tracker)
   peer84.attach_tracker(tracker)
   peer85.attach_tracker(tracker)
   peer86.attach_tracker(tracker)
   peer87.attach_tracker(tracker)
   peer88.attach_tracker(tracker)
   peer89.attach_tracker(tracker)
   peer90.attach_tracker(tracker)
   peer91.attach_tracker(tracker)
   peer92.attach_tracker(tracker)
   peer93.attach_tracker(tracker)
   peer94.attach_tracker(tracker)
   peer95.attach_tracker(tracker)
   peer96.attach_tracker(tracker)
   peer97.attach_tracker(tracker)
   peer98.attach_tracker(tracker)
   peer99.attach_tracker(tracker)

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
   peer10.set_file("1a")
   peer11.set_file("1a")
   peer12.set_file("1a")
   peer13.set_file("1a")
   peer14.set_file("1a")
   peer15.set_file("1a")
   peer16.set_file("1a")
   peer17.set_file("1a")
   peer18.set_file("1a")
   peer19.set_file("1a")
   peer20.set_file("1a")
   peer21.set_file("1a")
   peer22.set_file("1a")
   peer23.set_file("1a")
   peer24.set_file("1a")
   peer25.set_file("1a")
   peer26.set_file("1a")
   peer27.set_file("1a")
   peer28.set_file("1a")
   peer29.set_file("1a")
   peer30.set_file("1a")
   peer31.set_file("1a")
   peer32.set_file("1a")
   peer33.set_file("1a")
   peer34.set_file("1a")
   peer35.set_file("1a")
   peer36.set_file("1a")
   peer37.set_file("1a")
   peer38.set_file("1a")
   peer39.set_file("1a")
   peer40.set_file("1a")
   peer41.set_file("1a")
   peer42.set_file("1a")
   peer43.set_file("1a")
   peer44.set_file("1a")
   peer45.set_file("1a")
   peer46.set_file("1a")
   peer47.set_file("1a")
   peer48.set_file("1a")
   peer49.set_file("1a")
   peer50.set_file("1a")
   peer51.set_file("1a")
   peer52.set_file("1a")
   peer53.set_file("1a")
   peer54.set_file("1a")
   peer55.set_file("1a")
   peer56.set_file("1a")
   peer57.set_file("1a")
   peer58.set_file("1a")
   peer59.set_file("1a")
   peer60.set_file("1a")
   peer61.set_file("1a")
   peer62.set_file("1a")
   peer63.set_file("1a")
   peer64.set_file("1a")
   peer65.set_file("1a")
   peer66.set_file("1a")
   peer67.set_file("1a")
   peer68.set_file("1a")
   peer69.set_file("1a")
   peer70.set_file("1a")
   peer71.set_file("1a")
   peer72.set_file("1a")
   peer73.set_file("1a")
   peer74.set_file("1a")
   peer75.set_file("1a")
   peer76.set_file("1a")
   peer77.set_file("1a")
   peer78.set_file("1a")
   peer79.set_file("1a")
   peer80.set_file("1a")
   peer81.set_file("1a")
   peer82.set_file("1a")
   peer83.set_file("1a")
   peer84.set_file("1a")
   peer85.set_file("1a")
   peer86.set_file("1a")
   peer87.set_file("1a")
   peer88.set_file("1a")
   peer89.set_file("1a")
   peer90.set_file("1a")
   peer91.set_file("1a")
   peer92.set_file("1a")
   peer93.set_file("1a")
   peer94.set_file("1a")
   peer95.set_file("1a")
   peer96.set_file("1a")
   peer97.set_file("1a")
   peer98.set_file("1a")
   peer99.set_file("1a")

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
   peer10.set_size(f.__len__())
   peer11.set_size(f.__len__())
   peer12.set_size(f.__len__())
   peer13.set_size(f.__len__())
   peer14.set_size(f.__len__())
   peer15.set_size(f.__len__())
   peer16.set_size(f.__len__())
   peer17.set_size(f.__len__())
   peer18.set_size(f.__len__())
   peer19.set_size(f.__len__())
   peer20.set_size(f.__len__())
   peer21.set_size(f.__len__())
   peer22.set_size(f.__len__())
   peer23.set_size(f.__len__())
   peer24.set_size(f.__len__())
   peer25.set_size(f.__len__())
   peer26.set_size(f.__len__())
   peer27.set_size(f.__len__())
   peer28.set_size(f.__len__())
   peer29.set_size(f.__len__())
   peer30.set_size(f.__len__())
   peer31.set_size(f.__len__())
   peer32.set_size(f.__len__())
   peer33.set_size(f.__len__())
   peer34.set_size(f.__len__())
   peer35.set_size(f.__len__())
   peer36.set_size(f.__len__())
   peer37.set_size(f.__len__())
   peer38.set_size(f.__len__())
   peer39.set_size(f.__len__())
   peer40.set_size(f.__len__())
   peer41.set_size(f.__len__())
   peer42.set_size(f.__len__())
   peer43.set_size(f.__len__())
   peer44.set_size(f.__len__())
   peer45.set_size(f.__len__())
   peer46.set_size(f.__len__())
   peer47.set_size(f.__len__())
   peer48.set_size(f.__len__())
   peer49.set_size(f.__len__())
   peer50.set_size(f.__len__())
   peer51.set_size(f.__len__())
   peer52.set_size(f.__len__())
   peer53.set_size(f.__len__())
   peer54.set_size(f.__len__())
   peer55.set_size(f.__len__())
   peer56.set_size(f.__len__())
   peer57.set_size(f.__len__())
   peer58.set_size(f.__len__())
   peer59.set_size(f.__len__())
   peer60.set_size(f.__len__())
   peer61.set_size(f.__len__())
   peer62.set_size(f.__len__())
   peer63.set_size(f.__len__())
   peer64.set_size(f.__len__())
   peer65.set_size(f.__len__())
   peer66.set_size(f.__len__())
   peer67.set_size(f.__len__())
   peer68.set_size(f.__len__())
   peer69.set_size(f.__len__())
   peer70.set_size(f.__len__())
   peer71.set_size(f.__len__())
   peer72.set_size(f.__len__())
   peer73.set_size(f.__len__())
   peer74.set_size(f.__len__())
   peer75.set_size(f.__len__())
   peer76.set_size(f.__len__())
   peer77.set_size(f.__len__())
   peer78.set_size(f.__len__())
   peer79.set_size(f.__len__())
   peer80.set_size(f.__len__())
   peer81.set_size(f.__len__())
   peer82.set_size(f.__len__())
   peer83.set_size(f.__len__())
   peer84.set_size(f.__len__())
   peer85.set_size(f.__len__())
   peer86.set_size(f.__len__())
   peer87.set_size(f.__len__())
   peer88.set_size(f.__len__())
   peer89.set_size(f.__len__())
   peer90.set_size(f.__len__())
   peer91.set_size(f.__len__())
   peer92.set_size(f.__len__())
   peer93.set_size(f.__len__())
   peer94.set_size(f.__len__())
   peer95.set_size(f.__len__())
   peer96.set_size(f.__len__())
   peer97.set_size(f.__len__())
   peer98.set_size(f.__len__())
   peer99.set_size(f.__len__())

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
   peer10.init_gossip_cycle()
   peer11.init_gossip_cycle()
   peer12.init_gossip_cycle()
   peer13.init_gossip_cycle()
   peer14.init_gossip_cycle()
   peer15.init_gossip_cycle()
   peer16.init_gossip_cycle()
   peer17.init_gossip_cycle()
   peer18.init_gossip_cycle()
   peer19.init_gossip_cycle()
   peer20.init_gossip_cycle()
   peer21.init_gossip_cycle()
   peer22.init_gossip_cycle()
   peer23.init_gossip_cycle()
   peer24.init_gossip_cycle()
   peer25.init_gossip_cycle()
   peer26.init_gossip_cycle()
   peer27.init_gossip_cycle()
   peer28.init_gossip_cycle()
   peer29.init_gossip_cycle()
   peer30.init_gossip_cycle()
   peer31.init_gossip_cycle()
   peer32.init_gossip_cycle()
   peer33.init_gossip_cycle()
   peer34.init_gossip_cycle()
   peer35.init_gossip_cycle()
   peer36.init_gossip_cycle()
   peer37.init_gossip_cycle()
   peer38.init_gossip_cycle()
   peer39.init_gossip_cycle()
   peer40.init_gossip_cycle()
   peer41.init_gossip_cycle()
   peer42.init_gossip_cycle()
   peer43.init_gossip_cycle()
   peer44.init_gossip_cycle()
   peer45.init_gossip_cycle()
   peer46.init_gossip_cycle()
   peer47.init_gossip_cycle()
   peer48.init_gossip_cycle()
   peer49.init_gossip_cycle()
   peer50.init_gossip_cycle()
   peer51.init_gossip_cycle()
   peer52.init_gossip_cycle()
   peer53.init_gossip_cycle()
   peer54.init_gossip_cycle()
   peer55.init_gossip_cycle()
   peer56.init_gossip_cycle()
   peer57.init_gossip_cycle()
   peer58.init_gossip_cycle()
   peer59.init_gossip_cycle()
   peer60.init_gossip_cycle()
   peer61.init_gossip_cycle()
   peer62.init_gossip_cycle()
   peer63.init_gossip_cycle()
   peer64.init_gossip_cycle()
   peer65.init_gossip_cycle()
   peer66.init_gossip_cycle()
   peer67.init_gossip_cycle()
   peer68.init_gossip_cycle()
   peer69.init_gossip_cycle()
   peer70.init_gossip_cycle()
   peer71.init_gossip_cycle()
   peer72.init_gossip_cycle()
   peer73.init_gossip_cycle()
   peer74.init_gossip_cycle()
   peer75.init_gossip_cycle()
   peer76.init_gossip_cycle()
   peer77.init_gossip_cycle()
   peer78.init_gossip_cycle()
   peer79.init_gossip_cycle()
   peer80.init_gossip_cycle()
   peer81.init_gossip_cycle()
   peer82.init_gossip_cycle()
   peer83.init_gossip_cycle()
   peer84.init_gossip_cycle()
   peer85.init_gossip_cycle()
   peer86.init_gossip_cycle()
   peer87.init_gossip_cycle()
   peer88.init_gossip_cycle()
   peer89.init_gossip_cycle()
   peer90.init_gossip_cycle()
   peer91.init_gossip_cycle()
   peer92.init_gossip_cycle()
   peer93.init_gossip_cycle()
   peer94.init_gossip_cycle()
   peer95.init_gossip_cycle()
   peer96.init_gossip_cycle()
   peer97.init_gossip_cycle()
   peer98.init_gossip_cycle()
   peer99.init_gossip_cycle()

   sleep(10)

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
   print peer10.get_chunks()
   print peer11.get_chunks()
   print peer12.get_chunks()
   print peer13.get_chunks()
   print peer14.get_chunks()
   print peer15.get_chunks()
   print peer16.get_chunks()
   print peer17.get_chunks()
   print peer18.get_chunks()
   print peer19.get_chunks()
   print peer20.get_chunks()
   print peer21.get_chunks()
   print peer22.get_chunks()
   print peer23.get_chunks()
   print peer24.get_chunks()
   print peer25.get_chunks()
   print peer26.get_chunks()
   print peer27.get_chunks()
   print peer28.get_chunks()
   print peer29.get_chunks()
   print peer30.get_chunks()
   print peer31.get_chunks()
   print peer32.get_chunks()
   print peer33.get_chunks()
   print peer34.get_chunks()
   print peer35.get_chunks()
   print peer36.get_chunks()
   print peer37.get_chunks()
   print peer38.get_chunks()
   print peer39.get_chunks()
   print peer40.get_chunks()
   print peer41.get_chunks()
   print peer42.get_chunks()
   print peer43.get_chunks()
   print peer44.get_chunks()
   print peer45.get_chunks()
   print peer46.get_chunks()
   print peer47.get_chunks()
   print peer48.get_chunks()
   print peer49.get_chunks()
   print peer50.get_chunks()
   print peer51.get_chunks()
   print peer52.get_chunks()
   print peer53.get_chunks()
   print peer54.get_chunks()
   print peer55.get_chunks()
   print peer56.get_chunks()
   print peer57.get_chunks()
   print peer58.get_chunks()
   print peer59.get_chunks()
   print peer60.get_chunks()
   print peer61.get_chunks()
   print peer62.get_chunks()
   print peer63.get_chunks()
   print peer64.get_chunks()
   print peer65.get_chunks()
   print peer66.get_chunks()
   print peer67.get_chunks()
   print peer68.get_chunks()
   print peer69.get_chunks()
   print peer70.get_chunks()
   print peer71.get_chunks()
   print peer72.get_chunks()
   print peer73.get_chunks()
   print peer74.get_chunks()
   print peer75.get_chunks()
   print peer76.get_chunks()
   print peer77.get_chunks()
   print peer78.get_chunks()
   print peer79.get_chunks()
   print peer80.get_chunks()
   print peer81.get_chunks()
   print peer82.get_chunks()
   print peer83.get_chunks()
   print peer84.get_chunks()
   print peer85.get_chunks()
   print peer86.get_chunks()
   print peer87.get_chunks()
   print peer88.get_chunks()
   print peer89.get_chunks()
   print peer90.get_chunks()
   print peer91.get_chunks()
   print peer92.get_chunks()
   print peer93.get_chunks()
   print peer94.get_chunks()
   print peer95.get_chunks()
   print peer96.get_chunks()
   print peer97.get_chunks()
   print peer98.get_chunks()
   print peer99.get_chunks()

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
   print peer10.get_values()
   print peer11.get_values()
   print peer12.get_values()
   print peer13.get_values()
   print peer14.get_values()
   print peer15.get_values()
   print peer16.get_values()
   print peer17.get_values()
   print peer18.get_values()
   print peer19.get_values()
   print peer20.get_values()
   print peer21.get_values()
   print peer22.get_values()
   print peer23.get_values()
   print peer24.get_values()
   print peer25.get_values()
   print peer26.get_values()
   print peer27.get_values()
   print peer28.get_values()
   print peer29.get_values()
   print peer30.get_values()
   print peer31.get_values()
   print peer32.get_values()
   print peer33.get_values()
   print peer34.get_values()
   print peer35.get_values()
   print peer36.get_values()
   print peer37.get_values()
   print peer38.get_values()
   print peer39.get_values()
   print peer40.get_values()
   print peer41.get_values()
   print peer42.get_values()
   print peer43.get_values()
   print peer44.get_values()
   print peer45.get_values()
   print peer46.get_values()
   print peer47.get_values()
   print peer48.get_values()
   print peer49.get_values()
   print peer50.get_values()
   print peer51.get_values()
   print peer52.get_values()
   print peer53.get_values()
   print peer54.get_values()
   print peer55.get_values()
   print peer56.get_values()
   print peer57.get_values()
   print peer58.get_values()
   print peer59.get_values()
   print peer60.get_values()
   print peer61.get_values()
   print peer62.get_values()
   print peer63.get_values()
   print peer64.get_values()
   print peer65.get_values()
   print peer66.get_values()
   print peer67.get_values()
   print peer68.get_values()
   print peer69.get_values()
   print peer70.get_values()
   print peer71.get_values()
   print peer72.get_values()
   print peer73.get_values()
   print peer74.get_values()
   print peer75.get_values()
   print peer76.get_values()
   print peer77.get_values()
   print peer78.get_values()
   print peer79.get_values()
   print peer80.get_values()
   print peer81.get_values()
   print peer82.get_values()
   print peer83.get_values()
   print peer84.get_values()
   print peer85.get_values()
   print peer86.get_values()
   print peer87.get_values()
   print peer88.get_values()
   print peer89.get_values()
   print peer90.get_values()
   print peer91.get_values()
   print peer92.get_values()
   print peer93.get_values()
   print peer94.get_values()
   print peer95.get_values()
   print peer96.get_values()
   print peer97.get_values()
   print peer98.get_values()
   print peer99.get_values()

   shutdown()