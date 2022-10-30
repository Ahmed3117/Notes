## terminal settings:

* to change font color and background of the terminal:
  color 1c   ==>1 to change font color , c to change background color
* to get info about available colors for font and background:
  color -help
* to reset color changes:
  color
* to change current terminal title:
  title ahmed
* you can operate two commands in the same time using:
  &&

## alias:

* to make a shortcut (alias) for a command :
  alias open='xdg-open .'  ===> next time use command open instead of xdg-open . 
* to show all exist command shortcuts:
  alias

## file&folders : (current pathes, movement ,.....)

* ls:
  show all folders and files in this path
* ls -a :
  show all folders and files in this path and also the hidden ones
* ls -l:
  show all folders and files in this path but with details like date added and other
* cd Foldername :
  enter to this folder
* cd "path"
  go to this path
* cd .. :
  go a step back from your current path
* cd ../.. :
  go two steps back from your current path
* pwd :
  get current path

## getting information about a command :

* --help:
  used to get information about a command =====> Ex => cd --help
* man:
  used to get the manual(explanation of how to use) of a command =====> Ex=> man cd
* /?:
  used to get the manual(explanation of how to use) of a command ====> Ex=> cd /?

## getting system information:

* uname:
  used to get system information ====> Ex => uname , uname --all

## files: (create , update , copy , cut , .....)

### get the file type:

* file:
  Ex=> file index.docx    ===> result--> microsoft word file
    (if the file was empty the result will be empty) 

### modify an existing file:

* cat:

  Ex=> cat >> test.txt    then click enter to write on it :
       I am 22 years old

### reading a file:

* cat:
  1) to read a file:
     Ex=> cat test.txt
  2) to read more than a file in the same time: (after each other)
     Ex=> cat test1.txt test2.txt
  3) to read all files exist in current path:
     cat *
* nano:
         nano is a terminal text editor 
         Ex=> nano ( it will open the nano editor to read on it then save it.)
         Ex=> nano test.txt (to modify an exist file .)
* head:
             1) to read first 10 lines from the file
              Ex=> head test.txt
             2) to read any number of lines from a file
              Ex=> head -14 test.txt
* tail:
             1) to read last 10 lines from the file
                Ex=> tail test.txt
             2) to read any number of lines from a file from the tail
                Ex=> tail -14 test.txt
* nl:
         to read a file and numberize its lines
* grep :
         to get lines that have a word from a file (filtering)
         Ex=> cat test.txt | grep lotfy (get the lines that have the word lotfy from the file test.txt .)

### open a file as gui:

* mimeopen file_path :

  to open any file as a gui with the suit editor

### create a file:

* touch:
  to create a file
  EX=> touch test

* echo:

  1) to create a file and write on it 
     Ex=> echo "i am ahmed issa" > test.txt   ===> create a file test and write i am ahmed issa on it
     (if this file is already exist , it will remove its content and write the new content )
  2) the same of number 2 but not removing the last content but continue after it
     Ex=> echo "i am ahmed issa" >> test.txt

* cat:

  to make a file and write on it:
  Ex=> cat > test.txt     then click enter to write on it :
       hi , i am ahmed issa

  

### remove a file:

* rm:
             1) to remove a file
              Ex=>rm test
             2) to remove all files in a place (that won't remove folders )
              Ex=> rm *

### copy a file:

* cp: 

  1) copy a file ( cp file_path paste_path )
     Ex=>cp test.txt Ahmed (where Ahmed is a folder in the same place where test.txt is .)

           2) copy a file with a new name ( cp file_path paste_path/file_new_name )
              Ex=> cp test.txt Ahmed/test2.txt 

### cut afile:

* cat:

  Ex=> cat test1.txt > test2.txt

* mv:

     1) move a file to another place ( mv file_path paste_path )
        Ex=>mv test.txt Ahmed (where Ahmed is a folder in the same place where test.txt is .)
        Ex=>mv test.txt ../  ===> move the file test a step back
     2) move a file with a new name ( mv file_path paste_path/file_new_name )
        Ex=> mv test.txt Ahmed/test2.txt

### rename a file :

​		(move the file to the same place in a new name .)
​		Ex=> mv test.txt test2.txt

### store a command result in a file:

​		Ex: pip freeze > requirements.txt

### copy the result of any command to the clip board 

​		Ex: ping elzero.org | clip

​			===> now if you want make a file and click paste to paste the result of this command

## folders:

### to open home page in details as gui:

​	dolphin : it meats explorer in windows

### to open the current folder as a gui:

​	xdg-open . :  it meats explorer . in windows


### create a folder :

* mkdir: 

  Ex=> mkdir ahmed 
  Ex=> mkdir ahmed mohamed sara nahla ===> four folders in the same time
  Ex=> mkdir "ahmed issa"  ===> use "" if the name has a space
  Ex=> mkdir ../test   ===> go back a step in the path then make a folder test


### folder tree:

* tree:
  to show folder tree (if i have folders in folders)
  Ex=> tree /a

### remove a folder:

* rmdir:
  to remove an empty folder

* rm -r:
  to remove any folder
  Ex=> rm -r ahmed

### copy a folder:

* cp : 
  to copy an empty folder

* cp -r:
             1) to copy a folder 
              Ex=> cp -r ahmed mohamed (will copy ahmed to mohamed)
             2) to copy a folder with a new name
              Ex=> cp -r ahmed mohamed/yaser (will copy ahmed to mohamed with a new name yaser)

### cut:

         1) move a folder to another place ( mv folder_path paste_path )
            Ex=>mv test Ahmed 
            Ex=>mv test ../  ===> move the folder test a step back
         2) move a folder with a new name ( mv file_path paste_path/file_new_name )
            Ex=> mv test  Ahmed/test2

### rename a folder :

​		(move the folder to the same place in a new name .)
​		Ex=> mv test test2

## search:

* grep :
  Ex=> cat test.txt | grep lotfy (get the lines that have the word lotfy from the file test.txt .)
  Ex=> grep "hi" test.txt  ==> look for hi in the file test
  Ex=> grep "hi" ahmed     ==> look for hi in the folder ahmed
  Ex=> grep "hi" -r        ==> look for hi in the current folder path
  Ex=> grep "hi" -r ahmed  ==> look for hi in the folder ahmed and the files on it 
  Ex=> grep "hi" -r -l     ==> give me a list of files that contains hi in the current path

## search for files and directories:

* to look for files of an installed program :
    whereis vlc
* to look for any file or directory:
    locate test.txt
* to look for a file by its extention:
    locate *.py
    **note** locate searches for a file in all system .
* to look for a file in a specific path :
    find "/home/ahmedissa" -name test.txt
* to look for a file by its extention in aspecific path :
    find "/home/ahmedissa" -name "*.txt"
* to look for a file by its name but I can't remember the extention in aspecific path :
    find "/home/ahmedissa" -name "test.*"

## network:

* ifconfig:
  to know the network cards in your device (like: eth ==> the ethernet port ,, wlan==> the wifi port ,, lo ==> local host )

* iwconfig:
  to get my network cards that work in wireless

* ipconfig: 
  to get my network settings

* ping:
  to ping a website
  1) ping in one time:
     Ex=> ping elzero.org
  2) continue ping untill i break(break by ctrl+c)
     Ex=> ping elzero.org -t

## users & root:

* to deal as a super user (root):
    sudo su
* to exit root mood:
    exit
* to add user:
    sudo adduser ahmed
* to login the terminal with the user name ahmed
    sudo -l ahmed
    OR
    su -l ahmed
    OR
    sudo - ahmed
* to know the current user :
    whoami
* to come out of the user ahmed :
    exit
* to make the user ahmed deal as root:
    sudo usermod -aG sudo ahmed
* to remove a user ( without removing its files ):
    sudo deluser ahmed
* to remove a user ( with removing all its files ):
    sudo deluser --remove-home ahmed 
* to change user password:
    passwd
* to change the root password:
    sudo passwd root
    or enter to root mood then write ==> passwd

## groups:

* to create a new group:
  sudo grouadd developer (developer is the group name)

* to add users to a group:
    sudo usermod -aG developer hassan
* to know groupes that i am added on them:
    groups
    or : groups hassan
* to remove a user from a group:
    sudo gpasswd -d hassan developer
* to remove a group:
    sudo groupdel developer

## permissions:

```
* who   u, g , o    ( user , group , other ) (other means any other user except the current user)

* what  + , - , =   ( add , remove, set exactly)

* which r , w , x   (read , write , execute)

* d ==> this is directory

- ==> this is file
```

* Ex : we went to desktop then command this ==> ls -l
  - the result is :
        drwxrwxr-x  2 ahmedissa ahmedissa      4096 يول 21 11:52  ahmed 
    * explanation of the result:
          d          means directory,
          rwx       means that user can read & write & execute this directory ,
          rwx       means that group can read & write & execute this directory , 
          r-x        means that other can read & execute this directory but can't write on it ,
          2          means the number of files inside this directory ,

* to change permissions : (suppose I have a file with the name test )
  Ex1 :  chmod u-w test 

  - explanation of this command :
     chmod       means change mode 
     u                means user (the change will be for me )

    " - "              means remove (I want to remove a permission)
     w                means write (this is the permission I want to remove)
     test             is the file path

  Ex2==> chmod u-rw test 

  - explanation of this command :
     u                 means user (the change will be for me )

    " - "              means remove (I want to remove a permission)
     rw               means read & write (this is the permission I want to remove)

  Ex3==> chmod o=x test

  * explanation of this command:
      o               means other
      =               means set (remove all permissions of other to set the next permission only)
      x               means execte (execute will be the only permission for other )

  Ex4==> chmod +x test

  * explanation of this command:
    +x           you let the first digit empty without identifing a user or group or other and this means that the                                              permission x will be added to them all

    

* another way to identify the permissions:
        
        0   ---
        1   --x
        2   -w-
        3   -wx
        4   r--
        5   r-x
        6   rw-
        7   rwx
    Ex==> chmod 403 test

    * explanation of this command:
      4   means that permissions for user is r-- (can only read)
      0   means that permissions for group is --- (can't read,write or execute)
      3   means that permissions for other is -wx (can write & execute but can't read )

## install , uninstall , upgrade , remove , update , search in repos:

* to search for a program on my reposetory:
    apt-cache search firefox
    
* to install a program from my reposetory:
    sudo apt-get install vlc
    
    **note** in arch : sudo pamac install vlc     or     sudo pacman -S vlc
    
* to remove(uninstall) a program:
    sudo apt-get remove vlc
    
* looking for updates (system updates or your installed programs updates)
    sudo apt-get update  (just search for updates)
    
* to upgrade your system (to command needed updates):
    sudo apt-get upgrade

## process management:

(somthing like task manager to know programs that is running now and show their PID and how mutch every one takes from memory and cpu and so on.... )

* to get current processes in this terminal (just in this terminal):
    ps

    **note** ( ps will get process information just in this moment but if we need a command to get process information and get updated it self in the terminal until I stop it myself, I will use top command )

* to get process information and get updated it self in the terminal until I stop it myself:
    top
    
* to get process information for a specific user:
    top -u ahmed

* to get all processes running in the system:
    ps aux
    
* to get process information for a running program (just for this program):
    ps aux | grep voko
    
* to lock a running program :(you will use the PID for this program )
    kill 2907 (where 2907 is the PID for the program)
    **note** ( ps will get process information just in this moment but if we need a command to get process information and get updated it self in the terminal until I stop it myself, I will use top command )

    

## file system:

* to go to file system path :
    cd /
    then    ls    to show them
* bin         ==> contains files for all programs or terminal commands in the system.
* sbin       ==> contains files for  programs or terminal commands that needs root permissions in the system.
* home     ==> has users directories(when i create a new user it creates a directory with its name in home )but the main user(root) has his own folder outside home .
* boot       ==> contains boot files like grub and others that are responsible for running the system.
* sys         ==> (فيه تعريفات النظام , أو ملفات تعريف الهاردوير بتاع النظام)
* media     ==> (ملفات تعريف الهاردوير الخارجى زى الفلاشة والماوس وكده)

## Bash :

* Bash is the linux language (linux commands)
* we can make a file and put some commands in it then let terminal operate them respectively .
* to make a bash file:
    1) make a file with extention sh (for example test.sh)
    2) write this ==> #!/bin/bash   as the first line in the file then save the file
    3) write commands you want to operate like :
        pwd
        ls
        cat > test
        I am Ahmed Issa
        ^c  (this means ctrl+c to exit cat command)
    4) to be able to run this file in the terminal you need to give user a permission to execute it :
        chmod u+x test.sh
    5) stop in terminal in the path where the bash file is then write this ==> ./test.sh    then enter.
    you also can run the bash file by double click on it or by pulling it to the terminal. 
* some BAsh programming commands :
    1) printing:
        echo "I am Ahmed Issa"
        echo 2422
        
    2) variables:
        x="ahmed"
        echo $x 
        
    3) receiving input :
         read -p ==> used to receive visual input 
         read -sp ==> used to receive non visual input (like password)
         Ex==> read -p "Enter your name : " name (when user enter his name it will be stored in a variable name)
               echo "hello $name" 
         
    4) making an empty line:
         echo

         - Ex:
    
           Program to look for a word in a file 
           the user will enter the file path and the word he needs to look for then the program will return the result:
         
           read -p "Enter file path : " f
           read -p "Enter the word you want to look for : " word
           echo
           cat $f | grep $word