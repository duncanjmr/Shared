import urllib.request as urllib
import json

class server:
    def __init__(self):
        # Specify flask ip adress here (this one works if flask is run on your own computer)
        self.url = 'http://localhost:5123'
        
    def set_location(self,lon_lat,units):
        data = {'location': lon_lat,'units':units}
        req = urllib.Request(self.url+'/set_location')
        req.add_header('Content-Type', 'application/json')
        response = urllib.urlopen(req, json.dumps(data))
        
    def set_targ(self,az_alt):
        # Set the target position in the arduino (notice dictionary protocol)
        data = {'targ': az_alt}
        req = urllib.Request(self.url+'/set_targ')
        req.add_header('Content-Type', 'application/json')
        response = urllib.urlopen(req, json.dumps(data))
        
    def get_pos(self):
        # Get the current position of the arduino (again, protocols)
        a = urllib.urlopen(self.url+'/get_pos')
        dic = json.loads(a.read())
        az_alt = dic['pos']
        #az_alt_targ = dic['targ']
        return az_alt#,az_alt_targ
    
    def setup(self):
        # Currently nonfuntionalipython
        a = urllib.urlopen(self.url+'/setup')
        return json.loads(a.read())

    def move(self,az_alt):
        # move a small incriment
        data = {'increment': az_alt}
        req = urllib.Request(self.url+'/move')
        req.add_header('Content-Type', 'application/json')
        response = urllib.urlopen(req, json.dumps(data))
        
    def set_calib(self,n=None):
        if n==None:
            urllib.urlopen(self.url+'/set_calib')
        else:
            data = {"calib_num": n }
            req = urllib.Request(self.url+'/set_calib')
            req.add_header('Content-Type', 'application/json')
            response = urllib.urlopen(req, json.dumps(data))
    def calibrate(self):
        urllib.urlopen(self.url+'/calibrate')
        
