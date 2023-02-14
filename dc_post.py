import requests as req
import random
import time 

url = "https://discord.com/api/v9/channels/1013542170415870012/messages"
url_test = "https://discord.com/api/v9/channels/870267093952643092/messages" # my server


headers = {
    'authorization': 'NDc5MjY5NTUxMjM4ODA3NTcy.GXpl6m.LTo4KRdtZ3lG8akUtIfOrPz3LP1OtFCIWPXeLo',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
headers1 = { #litai3
    'authorization': 'ODA1ODY2ODc4MTMxMzcyMDg0.GDobQO.f0yrCYMO887Ddm79uz1w3V6hIepkwjtZJpHoW8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0'
}
headers2 = { #litai4
    'authorization': 'OTczNTYzODI3MjkzNjU1MDcw.GOhX64.R3lss7xoPnGwKoNCoURyqg2f2gCNGVn10ls5ks',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

data = {"content":"!roll 250","nonce":"1073118219683758080","tts":False,"flags":0}

#test = req.post(url_test ,headers=headers ,data=data1)
#r = req.post(url ,headers=headers ,data=data)
#r1 = req.post(url ,headers=headers1 ,data=data)
#r2 = req.post(url ,headers=headers2 ,data=data)

# Ctrl + C stop 

while True:
    num = random.randint(1,250)
    data["content"] = f"!roll {num}"
    #r2 = req.post(url ,headers=headers2 ,data=data)
    #print (r2)
    #time.sleep(30)
    r = req.post(url ,headers=headers ,data=data)  
    print (r)
    print (time.strftime("%m-%d %H:%M", time.localtime()))
    time.sleep(1810)



'''
while i > 0:
    num = random.randint(1,250)
    print (f"!roll {num}") 
    count += 1 
    time.sleep(5)
'''    


