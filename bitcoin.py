import requests as req
import json

### API Docs:  https://www.coindesk.com/api/


class Bitcoin:
    
    def __init__(self):
        self.url= 'https://api.coindesk.com/v1/bpi/currentprice.json'

    def get(self):
        res= req.get(self.url)
        if(res.ok):
            data= json.loads(res.content)
            
            self.updated= data['time']['updated']
            self.disclaimer= data['disclaimer']
            
            self.usd_text= data['bpi']['USD']['rate']
            self.usd_value= data['bpi']['USD']['rate_float']
            self.usd_value= float(self.usd_value)
            
            return True
        else:
            return False

if __name__=='__main__':
    print('Welcome to Digital corrency world')
    bc= Bitcoin()
    bc.get()
    print(bc.updated)
    print(bc.usd_value)
    