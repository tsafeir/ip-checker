# from os import system, name
import os

print("\n***     Hi This Is a IP Brute Force Scanner     ***\n")

start_net_ip=input("please enter start network ip (Example: 192.168.1.1) : ")
end_net_ip=input("please enter end network ip (Example: 192.168.1.200) : ")
start_net_ip_list=start_net_ip.split(".")
end_net_ip_list=end_net_ip.split(".")

net_ip_start=(int(start_net_ip_list[3]))
start_net_ip_list.pop()
end_net_ip_4=int(end_net_ip_list[3])
host_ip=list(range(net_ip_start,(end_net_ip_4)+1))
ip= start_net_ip_list[0] + "." + start_net_ip_list[1] + "."+ start_net_ip_list[2]
print("\nyour IP range : "+ str(host_ip))
print("\n----------------------------------------------\n")
host_ip=list(reversed(host_ip))

def ping_ip(ip,host_ip):

    while len(host_ip) > 0:

        x=str(host_ip.pop())
        response = os.popen(f"ping {ip}"+"."+ x).read()
        
        if "Reply from "+ip+"."+x+": bytes=" in response:
            print(response+"\n")
            print(f"{ip}"+"."+ x+" is Up . Ping Successful")
            print("\n----------------------------------------------\n")

ping_ip(ip,host_ip)