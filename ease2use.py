import socket,getmac,requests,speedtest,psutil,sys,os
from tabulate import tabulate


class easy_to_use(object):
    def system_ip(self):
        self.hostname=socket.gethostname()
        self.ip=socket.gethostbyname(self.hostname)
        self.data={"System IP":[self.ip]}
        self.table=tabulate(self.data,headers="keys",tablefmt="grid")
        return self.table

    def mac_address(self):
        self.mac=getmac.get_mac_address()
        self.data={"Mac Address":[self.mac]}
        self.table=tabulate(self.data,headers="keys",tablefmt="grid")
        return self.table

    def host(self):
        self.hostname=socket.gethostname()
        self.data={"Host Name":[self.hostname]}
        self.table=tabulate(self.data,headers="keys",tablefmt="grid")
        return self.table
    
    def global_ip(self):
        self.g_ip=requests.get('http://ip.42.pl/short').text
        self.data={"Global IP":[self.g_ip]}
        self.table=tabulate(self.data,headers="keys",tablefmt="grid")
        return self.table

    def ping_test(self,host):
        self.response=os.system("ping -n 5 " + host)
        
        if self.response == 0:
            return True
        else:
            return False

class Speed_test(object):
    def __init__(self):
        self.scanner = psutil.net_if_addrs()
        self.speed = speedtest.Speedtest()
        self.interfaces = self.interface()[0]
        

    def interface(self):
        interfaces = []
        for interface_name, _ in self.scanner.items():
            interfaces.append(str(interface_name))
        return interfaces


    def test(self):
        down = str(f"{round(self.speed.download() / 1_000_000, 2)} Mbps")
        up = str(f"{round(self.speed.upload() / 1_000_000, 2)} Mbps")
        interface = self.interfaces
        data = {" Interface " : [interface],
                "Download:" : [down],
                "Upload:" : [up]
                }
        table = tabulate(data, headers="keys", tablefmt="grid")
        return table


    def __str__(self):
        return str(self.test())

if __name__=='__main__':
    object=easy_to_use()
    while(True):
        thisdict=[
            ["1", "System IP"],
            ["2", "Global IP"],
            ["3", "Mac Address"],
            ["4", "Host Name"],
            ["5", "Network Speed"],
            ["6", "Check Ping"],
            ["90", "Quit"]
        ]
        table=tabulate(thisdict,headers=['___ Menu ___'],tablefmt='fancy_grid')
        print(table)
        ask=int(input('Press numeric according to your requirement: '))
        if ask==1:
            try:
                print(object.system_ip())
            except Exception as e:
                print(f'Some problem arise {e}')
        elif ask==2:
            try:
                print(object.global_ip())
            except Exception as e:
                print(f'Some problem arise {e}')
        elif ask==3:
            try:
                print(object.mac_address())
            except Exception as e:
                print(f'Some problem arise {e}')
        elif ask==4:
            try:
                print(object.host())
            except Exception as e:
                print(f'Some problem arise {e}')
        elif ask==5:
            try:
                print('Wait for Couple of Seconds !!')
                print(Speed_test())
            except Exception as e:
                print(f'Some problem arise {e}')
        elif ask==6:
                try:
                    ask=input('Enter URL: ')
                    print(object.ping_test(ask))
                except Exception as e:
                    print(f'Some problem arise {e}')
        elif ask==90:
            print('      Quit !!        ')
            sys.exit()
        else:
            print('Wrong Choice !!')
