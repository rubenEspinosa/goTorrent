from pyactor.context import set_context, create_host, sleep, shutdown
from Tracker import *


if __name__ == "__main__":
    set_context()
    h = create_host()
    tracker=h.spawn('tracker1',Tracker)
    tracker.announce('peli1','peer1')
    tracker.announce('peli1', 'peer2')
    tracker.announce('peli2', 'peer3')
    tracker.init_start()
    sleep(11)
    tracker.get_peers('peli1')
    shutdown()




