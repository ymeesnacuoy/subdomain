Red="\e[0;31m"
Blue="\e[0;94m"
Green="\e[0;32m"
Off="\e[0m"

function indexS(){
    echo -e "===== SUBDOMAIN TOOLS INSTALL ====="
}

function termuxOS() {
	echo -e "$Red [$Green+$Red]$Off Checking directories... "
	if [ -e "/data/data/com.termux/files/usr/share/sub" ]; then
		echo -e "$Red [$Green+$Red]$Off A previous installation was found Do you want to replace it? [Y/n]: "
		read replace
		if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
	    		rm -r "/data/data/com.termux/files/usr/share/sub"
	    		rm "/data/data/com.termux/files/usr/bin/sub"
		else
	    		echo -e "$Red [$Green✘$Red]$Off If You Want To Install You Must Remove Previous Installations";
	    		echo -e "$Red [$Green✘$Red]$Off Installation Failed";
	    		exit
		fi
	fi
	echo -e "$Red [$Green+$Red]$Off Installing ...";
	mkdir "/data/data/com.termux/files/usr/share/sub" 
	cp "sub.py" "/data/data/com.termux/files/usr/share/sub"
	cp "install.sh" "/data/data/com.termux/files/usr/share/sub"
	echo -e "$Red [$Green+$Red]$Off Creating Symbolic Link ...";
	echo "#!/data/data/com.termux/files/usr/bin/bash
	python3 /data/data/com.termux/files/usr/share/sub/sub.py" '${1+"$@"}' > "sub";
	cp "sub" "/data/data/com.termux/files/usr/bin"
	chmod +x "/data/data/com.termux/files/usr/bin/sub"
	rm -r "sub";
	if [ -d "/data/data/com.termux/files/usr/share/sub" ] ;then
        	echo -e "$Red [$Green✘$Red]$Off Tool successfully installed and will start in 5s!";
        	echo -e "$Red [$Green✘$Red]$Off You can execute tool by typing sub"
        	sleep 5;
	       
	else
        	echo -e "$Red [$Green✘$Red]$Off Tool Cannot Be Installed On Your System! Use It As Portable !";
        	exit
    	fi
}
	

function linuxOS(){
	echo -e "$Red [$Green+$Red]$Off Checking directories... "
	if [ -d "/usr/share/sub" ]; then
        	echo -e "$Red [$Green✘$Red]$Off A Directory subdomain Was Found! Do You Want To Replace It? [Y/n]:" ;
        	read replace
        	if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
            		sudo rm -r "/usr/share/sub"
            		sudo rm "/usr/local/bin/sub"
        	else
            		echo -e "$Red [$Green✘$Red]$Off If You Want To Install You Must Remove Previous Installations";
            		echo -e "$Red [$Green✘$Red]$Off Installation Failed";
            		exit
        	fi
   	fi 
	echo -e "$Red [$Green+$Red]$Off Installing ...";
  	echo -e "$Red [$Green+$Red]$Off Creating Symbolic Link ...";
	echo -e "#!/bin/bash
   		python3 /usr/share/sub/sub.py" '${1+"$@"}' > "sub";
	chmod +x "sub";
	sudo mkdir "/usr/share/sub"
	sudo cp "sub.py" "/usr/share/sub"
	sudo cp "install.sh" "/usr/share/sub"
	sudo cp "sub" "/usr/local/bin"
   	rm -r "sub";
	if [ -d "/usr/share/sub" ] ;
	then
		echo -e "$Red [$Green✘$Red]$Off Tool Successfully Installed And Will Start In 5s!";
		sleep 5;
		echo -e "$Red [$Green✘$Red]$Off You can execute tool by typing sub";

	else
		echo -e "$Red [$Green✘$Red]$Off Tool Cannot Be Installed On Your System! Use It As Portable !";
		exit
	fi 
}


if [ -d "/data/data/com.termux/files/usr/" ]; then
	indexS
   	echo -e "$Red [$Green+$Red]$Off Sub Will Be Installed In Your System";
	termuxOS
elif [ -d "/usr/bin/" ];then
	indexS
	echo -e "$Red [$Green+$Red]$Off Sub Will Be Installed In Your System";
	linuxOS
else
	echo -e "$Red [$Green+$Red]$Off Tool Cannot Be Installed On Your System! Use It As Portable !";
	exit
fi
