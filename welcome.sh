#!/bin/bash

C_BD="\033[1m"
C_R="\033[31m"
C_Y="\033[33m"
C_G="\033[32m"
C_B="\033[34m"
C_P="\033[35m"
C_RS="\033[0m"


dot ()
{
	for NUM in {1..50}; do
		echo -en '-'
		sleep 0.01
	done
	echo -e "\n"
}

#dot
#echo -e "$C_BD		WELCOME$C_RS"
#echo -e "$C_Y\n Name:$C_RS$C_BD Sangeun Lee $C_RS$C_Y Email:$C_RS$C_BD leesese3320@gmail.com $C_RS"
#sleep 0.3
#echo -en "$C_Y\n Is everything correct? $C_RS"
#read YN
#sleep 0.3
#echo -en "$C_Y Is your email is leesese3320@gmail.com? $C_RS"
#read YN

dot
echo -e "$C_P$C_BD\n	  [ RIGGING DEMO REEL ]$C_RS"
sleep 0.3
echo -e "$C_G\n Name:$C_RS$C_BD Sangeun Lee$C_RS$C_G  Email:$C_RS$C_BD leesese3320@gmail.com$C_RS"
sleep 0.5
echo -e "$C_B$C_BD\n 3$C_RS"
sleep 0.3
echo -e "$C_Y$C_BD\n 2$C_RS"
sleep 0.3
echo -e "$C_R$C_BD\n 1$C_RS"
sleep 0.3
echo -e "$C_G$C_BD\n START!$C_RS"
