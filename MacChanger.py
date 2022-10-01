import subprocess
import optparse
import re

def get_user_input(): ## ---> Kullanıcıdan input alma yeri
   
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest = "interface", help = "Interface to help")
    parse_object.add_option("-m","--mac", dest = "mac_adress", help = "New Mac Adress")

    #print(parse_object.parse_args())
    return parse_object.parse_args()

def Mac_changer(user_interface, user_mac_adress): ## ---> Programın çalıştığı yer.
    
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_adress])
    subprocess.call(["ifconfig", user_interface, "up"]) 

def control_new_mac(interface): ## ----> Input kontrolü

    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) ## ---> str -> Python3 uyumluluğu

    if new_mac:
        
        return new_mac.group(0)
    
    else:
        
        return None

print("Mac is Changing")

(user_input,arguments) = get_user_input()

Mac_changer(user_input.interface, user_input.mac_adress)

final_mac = control_new_mac(str(user_input.interface)) ## ---> str -> Python3 uyumluluğu

if final_mac == user_input.mac_adress:
    print("Succsess")

else:
    print("Error")