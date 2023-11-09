import subprocess
from datetime import datetime
import time

ipaddr      = '8.8.8.8'                # enter IP address of device to monitor        
endTime     = '2023-05-27 23:00'            # enter time here to stop program 
deviceName  = "DNS"                   # enter site name here

fileName    = f"D:\{deviceName}_Ping_test.txt"   
pcommand    = 'ping -n 1 '+ ipaddr  
startevent  = int()

with open (fileName,"w") as tlog:
    tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Ping Test for {deviceName} : IP {ipaddr} Started" + '\n\n') 
    tlog.flush()
    while(True):
        if (datetime.now().strftime('%Y-%m-%d %H:%M')== endTime):
            tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Ping Test for {deviceName} Ended" + '\n\n')
            tlog.flush()
            exit()
        else:    
            result = subprocess.run(pcommand, capture_output=True, text=True)
            print(result.returncode)
            if result.returncode == 1 and startevent == 0:
                tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S' + f": {deviceName} Disconnected") + '\n')
                tlog.flush() 
                start_time = time.time()
                startevent = 1
            elif result.returncode == 1 and startevent == 1:
                pass
            elif result.returncode == 0 and startevent == 1:  
                end_time = time.time() -start_time
                tlog.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f": Connected back after {int(end_time)} seconds" + '\n\n') 
                tlog.flush()
                startevent = 0
            elif result.returncode == 0 and startevent == 0:  
                time.sleep(1)
                pass
