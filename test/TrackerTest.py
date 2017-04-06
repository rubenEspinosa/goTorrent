from pyactor.context import set_context, create_host, shutdown , sleep
from Tracker import *


if __name__ == "__main__":
    set_context()
    h = create_host()

    tracker=h.spawn('tracker1',Tracker)

    tracker.announce('peli1','peer1')
    tracker.announce('peli1', 'peer2')
    tracker.announce('peli1', 'peer5')
    tracker.announce('peli1', 'peer6')
    tracker.announce('peli1','peer3')
    tracker.announce('peli1', 'peer4')
    tracker.announce('peli1', 'peer7')
    tracker.announce('peli1', 'peer8')
    tracker.announce('peli1','peer9')
    tracker.announce('peli1', 'peer10')
    tracker.announce('peli1', 'peer11')
    tracker.announce('peli1', 'peer12')
    tracker.announce('peli1','peer13')
    tracker.announce('peli1', 'peer14')
    tracker.announce('peli1', 'peer15')
    tracker.announce('peli1', 'peer16')
    tracker.announce('peli1','peer17')
    tracker.announce('peli1', 'peer18')
    tracker.announce('peli1', 'peer19')
    tracker.announce('peli1', 'peer20')
    tracker.announce('peli2', 'peer3')

    tracker.init_start()

    sleep(11)

    print tracker.get_peers('peli1')

    shutdown()




