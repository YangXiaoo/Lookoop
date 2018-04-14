#date(2018-4-14)

归档
---
[root]# mkdir /archive
[root]# groupadd Archive 
[root]# chgrg Archive /archive #目录归属
[root]# usermod -aG Archive youth #组中添加用户
[root]# chmod 775 /archive #修改权限
[root]# touch /archive/Files_to_Backup #创建需要归档的文件列表
[root]# chmod +x /archive/Files_to_Backup
[root]# vim Daily_Archive #创建脚本
#!/bin/bash
#Daily_Archive

#Gather current date
DATA=$(date +%y%m%d)

#Set archive file name
FILE=/archive$DATA.tar.gz

#Set configuration & destination file
CONFIG_FILE=/archive/daily/Files_to_Backup
DESTINATION=/archive/daily

############   Main Script   #######
#Check backup config file exists
if [ -f $CONFIG_FILE ]
then 
	echo
	echo "Configuration file exists..."
	echo
else
	echo 
	echo "$CONFIG_FILE does not exist! Please chek file..."
	echo "Backup not complete due to missing Configuration file..."
	echo
	exit
fi

#Build the names of all the files to backup

FILE_NO=1 #Record the line of Configuration file
exec < $CONFIG_FILE 
read FILE_NAME #Read form configuration file

while [ $? -eq 0] 
do
	if [ -f $FILE_NAME -o -d $FILE_NAME ] #Test file is exist
	then
		FILE_LIST="$FILE_LIST $FILE_NAME"
	else
		echo
		echo "$FILE_NAME does not exist."
		echo "It is listed on line $FILE_NO of configuration file."
		echo "Continuing to build archive list..."
		echo 
	fi
	FILE_NO=$[ $FILE_NO + 1 ]
	read FILE_NAME
done

########## Backup the files and Compress Archives #######
echo "Starting archive..."
echo

tar -czf $DESTINATION $FILE_LIST 2> /dev/null

echo "Archive completed!"
echo "Resulting archive file is: $DESTINATION"
echo
exit




管理用户账户
------------
需要的步骤：
1.获得正确的待删除用户账户名
2.杀死正在系统上运行的属于该账户的进程
3.确认系统中属于该账户的所有文件
4.删除该用户账户
[root]# vim Delete_User.sh 
#!/bin/bash
#Delete_User

####### define function #######
# get_answer funtion start
function get_answer {

	unset ANSWER 
	ASK_COUNT=0

	while [ -z "$ANSWER" ] # While no answer is given, keep asking.
	do
		ASK_COUNT=$($ASK_COUNT + 1)

		case $ASK_COUNT in # If user gives no answer in time allotted
			2)
				echo 
				echo "Please answer the question..."
				echo
				;;
			3)
				echo
				echo "One last try...Please answer the question."
				echo
				;;
			4)
				echo
				echo "Since you have refuse to answer the question..."
				echo "Now, exiting program..."
				echo
				exit
				;;
		esac

		echo

		if [ -n "$LINE2" ] # Check variable
		then 
			echo $LINE1
			echo -e $LINE2" \C"   
			# -e enable interpretation of backslash escapes 
			# \c produce no further output
		else
			echo -e $LINE1" \C"
		fi
		read -t 60 ANSWER # Allow 60 seconds to answer before time-out
	done

	# Do a little variable clean-up
	unset LINE1
	unset LINE2
}  
# End of get_answer function

# process-answer function start
function process_answer {
	case $ANSWER in
		Y|y|yes|YES|Yes|yES|YEs )
			# If the answer is yes, do nothing.
			;;
		*)
			# If answer anything but yes, exit script
			echo
			echo $EXIT_LINE1
			echo $EXIT_LINE2
			echo 
			exit
			;;
	esac
	# Clean-up variable
	unset EXIT_LINE1
	unset EXIT_LINE2
}
# End of process_answer function
####### End of funtion definitions #######

####### Main Script #######
## 1. Get name of user account to check
echo "Step #1 -Determine User Account name to delete"
echo
LINE1="Please enter the username of user"
LINE2="account you wish to delete form system:"
get_answer
USER_ACCOUNT=$ANSWER

# Double check with script user that this is the correct user account
LINE1="Is $USER_ACCOUNT the user account"
LINE2="you wish to delete from the system?[y/n]"
get_answer
EXIT_LINE1="Because the account, $USER_ACCOUNT,is not"
EXIT_LINE2="the one you wish to delete, we are leaving the script..."
process_answer

##  Check that USER-ACCOUNT is really an account on the system.
USER_ACCOUNT_RECORD=$(cat /etc/passwd | grep -w $USER_ACCOUNT) #-w, --word-regexp 
if [ $? -eq 1 ] # If the account is not on the system, exit script.
then 
	echo 
	echo "Account, $USER_ACCOUNT, not found. "
	echo "Leaving the script..."
	echo 
	exit
fi
echo 
echo "I found this record:"
echo  $USER_ACCOUNT_RECORD

# Check the user account
LINE1="Is this the correct user account? [y/n]"
get_answer

EXIT_LINE1="Because the account, $USER_ACCOUNT,is not"
EXIT_LINE2="the one you wish to delete, we are leaving the script..."
process_answer

## 2. Serch for any running process that belong to the user account.
echo
echo "Step #2 - Find process on system belong to user account."
echo

ps -u $USER_ACCOUNT >/dev/null 

case $? in
	1 )
		echo "There are no process for this account currently running."
		echo
		;;
	0 )
		echo "$USER_ACCOUNT has the following process running:"
		ps -u $USER_ACCOUNT
		LINE1="Would you like me to kill the process(es)? [y/n]"
		get_answer

		case $ANSWER in
			Y|y|yes|YES|Yes|yES|YEs )
				COMMAND_1="ps -u $USER_ACCOUNT --no-heading"
				COMMAND_3="xargs -d \\n /user/bin/sudo /bin/kill -9"
				$COMMAND_1 | gawk '{print $1}' | COMMAND_3
				echo 
				echo "Process(es) Killed."
				;;
			* ) 
				echo
				echo "Will not kill the process(es)."
		esac
esac

## Create a report of all files owned by user account 
echo 
echo "Step #3 - Find files on system belonging to user account"
echo
echo "Creating a report of all files owned by $USER_ACCOUNT"
echo
echo "It is recommended that you backup/archive these files,"
echo "and then do one of two things:"
echo "1) Delete the files"
echo "2) Change the files' ownership to a current user account."
echo
echo "Please wait. This could take a while..."

REPORT_DATE=$(date +%y%m%d)
REPORT_FILE=$USER_ACCOUNT"_FILES_"$REPORT_DATE".rpt"

find / -user $USER_ACCOUNT > $REPORT_FILE 2>/dev/null

echo "Report is  completed."
echo "Name of report: 	$REPORT_FILE"
echo "Location of report: 	$(pwd)"
echo 

## Remove user account
echo
echo "Step #4 -Remove user account"
echo
LINE1="Remove $USER_ACCOUNT's account from system? [y/n]"
get_answer

EXIT_LINE1="Since you do not wish to remove the user account,"
EXIT_LINE2="$USER_ACCOUNT at this time, exiting the script..."
process_answer

userdel $USER_ACCOUNT
echo
echo "User account, $USER_ACCOUNT, has been removed!"
echo "Goodbye! My dear programer!"
exit


检查指定目录空间使用状况
------------------------
[root]# vim space_use.sh
#!/bin/bash

CHECK_DIRECTIONS="/var/log"

DATE=$(date '+%m%d')

exec > space_use_$DATE.rpt 

echo "Top ten Disk space usage"
echo "for $CHECK_DIRECTIONS directories"

for DIR in $CHECK_DIRECTIONS 
do
	echo 
	echo "The $DIR directory:"
	du -S $DIR 2>/dev/null
	sort -rn | sed '{11,$D; =}' | sed 'N; s/\n/ /' | gawk '{printf $1 ":" "\t" $2 "\t" $3 "\n"}'
done
exit




获取网络格言
------------
#!/bin/bash
url=http://www.lz13.cn/lizhiyingyu/8740.html
check_url=$(wget -nv --spider $url 2>&1)
if [[ $check_url == *error404* ]]
then 
        echo
        echo "Bad website!"
        echo "$url invalid..."
        echo "Exiting script..."
        echo
        exit
fi
wget -o /tmp/test/quote.log -O /tmp/test/quote.html --restrict-file-names=nocontrol $url #-o 日志 -O 下载
chmod +x /tmp/test/quote.html
qt_url=/tmp/test/qt.txt
sed 's/<[^>]*>//g' /tmp/test/quote.html > $qt_url
chmod +x $qt_url
cat $qt_url | while read line
do 
        gawk '{/^1..[A-Z][a-zA-Z]*\.$/} {print $0}' $line
done
exit

---------------------------
#!/bin/bash
url=www.quotationspage.com/qotd.html
check_url=$(wget -nv --spider $url 2>&1)
if [[ $check_url == *error404* ]]
then 
        echo
        echo "Bad website!"
        echo "$url invalid..."
        echo "Exiting script..."
        echo
        exit
fi
wget -o /tmp/test/quote.log -O /tmp/test/quote.html --restrict-file-names=nocontrol $url #-o 日志 -O 下载
chmod +x /tmp/test/quote.html
qt_url=/tmp/test/quote.txt
chmod +x $qt_url
sed 's/<[^>]*//g' /tmp/test/quote.html |
grep "$(date '+%Y)" -A2 |
sed 's/>//g' |
sed '/&nbsp;/{n ; d}' |  #匹配空格符并删除下一行的数据
gawk 'BEGIN{FS="&nbsp;"} {print $1}' |
tee $qt_url > /dev/null
exit

