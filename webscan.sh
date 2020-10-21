#!/bin/bash
#Colors
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
Purple="\033[0;35m"
Cyan="\033[0;36m"
Cafe="\033[0;33m"
Fiuscha="\033[0;35m"
blue="\033[1;34m"
nc="\e[0m"
clear
echo ""
banner () {
echo -e $'\033[0;35m  _      __ ____ ___    ____ _____ ___    _  __   \e[0m'
echo -e $'\033[0;35m | | /| / // __// _ )  / __// ___// _ |  / |/ /   \e[0m'
echo -e $'\033[0;35m | |/ |/ // _/ / _  | _\ \ / /__ / __ | /    /    \e[0m'
echo -e $'\033[0;35m |__/|__//___//____/ /___/ \___//_/ |_|/_/|_/     \e[0m'

}
banner
echo ""
printf "\033[0;35m Coded by Farhan | Nethunter    \033[1;37m [V 1.0]\e[0m\n"
printf "\033[1;37m ----------------------------------------------------\e[0m\n"
echo -e $'\e[1;37m\e[0m\e[1;33m AUTHOR  : DARKNET HAXOR \e[0m'
echo -e $'\e[1;37m\e[0m\e[1;33m YOUTUBE : YOUTUBE.COM/DARKNETHAXOR \e[0m'
echo -e $'\e[1;37m\e[0m\e[1;33m PAGE    : FACEBOOK.COM/DARKNETHAXOR \e[0m'
echo -e $'\e[1;37m\e[0m\e[1;33m GITHUB  : GITHUB.COM/DARKNETHAXOR \e[0m'
echo -e $'\e[1;32m ----------------------------------------------------\e[0m'
echo""
echo -e $'\e[1;32m\e[0m\e[1;32m SELECT YOUR ATTACK \e[0m'
echo -e $'\e[1;37m\e[0m\e[1;37m <≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠>\e[0m'
echo ""

                 echo -e $'\e[1;34m [\e[0m\e[1;31m1\e[0m\e[1;34m]\e[0m\e[1;32m Admin Finder \e[0m' 
                 echo -e $'\e[1;34m [\e[0m\e[1;31m2\e[0m\e[1;34m]\e[0m\e[1;32m Admin Scanner \e[0m'
                 echo -e $'\e[1;34m [\e[0m\e[1;31m3\e[0m\e[1;34m]\e[0m\e[1;32m No-Redirect \e[0m'
                 echo -e $'\e[1;34m [\e[0m\e[1;31m4\e[0m\e[1;34m]\e[0m\e[1;32m Update Tool \e[0m'
                 echo -e $'\e[1;34m [\e[0m\e[1;31m5\e[0m\e[1;34m]\e[0m\e[1;32m Help \e[0m'
                 echo -e $'\e[1;34m [\e[0m\e[1;31m0\e[0m\e[1;34m]\e[0m\e[1;32m Exit \e[0m'
                 echo ""

                 read -p $'\e[1;31m >>\e[0m\e[1;32m Enter Your Choice : \e[0m' option
		 case $option in

1)
  python admin
   ;;
2)
  python scan
   ;;
3)
  php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                  sleep 2
  xdg-open http://127.0.0.1:4444
  echo ""
  tail -f tamp.txt 
   ;;
4)
  cd $HOME
  rm -rf webscan
  git clone https://github.com/darknethaxor/webscan.git
  cd webscan
  chmod +x setup.sh
  bash setup.sh
  ;;
5)
  xdg-open https://www.facebook.com/groups/1546183828897889
  sleep 2
  bash webscan.sh
  ;;
0)
  xdg-open https://www.facebook.com/groups/1546183828897889
  exit
  ;;
  esac
echo ""
echo ""
echo -e "\e[33m              << Thanks For Stay Us >> \e[m "
exit
