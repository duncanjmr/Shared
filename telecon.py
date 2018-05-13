import requests
import time
import json


class telecon:
    def __init__(self):
        # Specify flask ip adress here (this one works if flask is run on your own computer)
        self.url = 'http://192.168.0.150:5123'

    def set_location(self,lon_lat,units):
        data = {'location': lon_lat,'units':units}
        resp = requests.post(self.url+'/set_location',data=json.dumps(data))
        response = resp.content
        return response
        
    def set_targ(self,az_alt):
        # Set the target position in the arduino (notice dictionary protocol)
        data = {'targ': az_alt}
        resp = requests.post(self.url+'/set_targ',data=json.dumps(data))
        return resp.content
        
    def get_pos(self):
        # Get the current position of the arduino (again, protocols)
        resp = requests.get(self.url+'/get_pos')
        dic = json.loads(resp.content)
        az_alt = dic['pos']
        return az_alt
    
    def setup(self):
        print("Setting up...")
        t = time.localtime()
        string = ''
        for i in t[:6]:
            bit = str(i)
            if len(bit)==1:
                bit = '0'+bit
            string += bit + '-'
        string += '000'
        # Currently nonfuntional
        data = {'time': string}
        
        # Currently nonfuntionalipython
        a = requests.post(self.url+'/setup',data=json.dumps(data))
        
        labels = ["coor1","coor2","coor3"]
        return [json.loads(a.content)[i] for i in labels]
    
    
    def move(self,az_alt):
        # move a small incriment
        print ("Moving: " + str(az_alt))
        data = {'increment': az_alt}
        req = requests.post(self.url+'/move',data=json.dumps(data))
        response = req.content
        return response
        
    def set_calib(self,n=None):
        "Setting calibration point"
        if n==None:
            requests.post(self.url+'/set_calib')
        else:
            data = {"calib_num": n }
            req = requests.post(self.url+'/set_calib',data=json.dumps(data))
            response = req.content
            
    def calibrate(self):
        print ("Calibrating...")
        req = requests.post(self.url+'/calibrate',data=json.dumps({}))
        response = json.loads(req.content)
        if response["response"] == "ok":
            print("Calibration successful!")
        elif response["response"] == "failed":
            print("Calibration failed... :(")
      
    def search(self,string):
        print('Searching for: "' + string + '"')
        data = {'string': string}
        req = requests.post(self.url+'/search',data=json.dumps(data))
        response = json.loads(req.content)
        print(response["String"])
        
    def track(self,string):
        print('Searching for: "' + string + '"')
        data = {'string': string}
        req = requests.post(self.url+'/track',data=json.dumps(data))
        response = json.loads(req.content)
        print(response["String"])




