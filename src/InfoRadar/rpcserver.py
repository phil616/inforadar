import rpyc
import requests



class InfoRadarService(rpyc.Service):
    def exposed_get_info(self):
        return "InfoRadarServer Connect Success"
    
    def on_connect(self, conn):
        return super().on_connect(conn)
    def on_disconnect(self, conn):
        return super().on_disconnect(conn)
    def on_session_end(self):
        return super().on_session_end()
    
    def exposed_network_get(self,params:dict):

        return requests.get(
            url=params['url']
            )

    exposed_constant_value = False

