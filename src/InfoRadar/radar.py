from rpcserver import InfoRadarService
from rpyc.utils.server import ThreadedServer
import sys
import time

t = ThreadedServer(InfoRadarService,port=9999)
t.start()
print(sys._getframe().f_code.co_name, sys._getframe().f_lineno, time.time())
