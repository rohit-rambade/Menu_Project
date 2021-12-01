import os
os.system("tput setaf 7")
os.system("tput bold")
j=0
while j!=1:

    print("#############################################################################################")
    print("""

█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀█ █▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█   █▀▀ █▀▄ █▄█ █▄█ █▀▄ █▀█ █░▀░█ \n""")

    print("#############################################################################################")
    os.system("tput setaf 1")
    
    print("Choose Where You Want To RUN \n")
    os.system("espeak-ng -v en+f2 'Where you want to run ' -s150")
    os.system("espeak-ng -v en+f2 'Local or Remote ' -s150")
    r= input("Local | Remote | Exit): ")
    
    os.system("tput setaf 1")

    if r=='local':
        i=0
        os.system('clear')
        while i!=1:
            print("""
            [1] Linux Commands
            [2] To Docker
            [3] Web Server
            [4] Exit\n\n""")
           
            mch = int(input("Enter your choice : "))
          
            if mch==1:
                m=0
                os.system('clear')
                while m!=1:
                    os.system("tput setaf 3")
                    
                    print("""
                    [1] Check date
                    [2] Check calender
                    [3] Check Ip Address
                    [4] Create partition
                    [5] Create directory
                    [6] Delete directory
               
                    [7] Make users
                    [8] open Firefox
                    [9]Exit
                    """)
                    
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
              
                    if ch==1: os.system("date")
                    elif ch==2: os.system("cal")
                    elif ch==3: os.system("ifconfig enp0s3")
                    elif ch==4:
                        fpath  = input("Enter the file path as (/dev/sda ): ")        
                        os.system(("fdisk {}").format(fpath))
                        input()
                    elif ch==5:
                        di = input("Enter the directory name : ")            
                        os.system(("mkdir /{}").format(di))
                    elif ch==6:
                        di = input("Enter the directory name : ")
                        os.system(("rm -rf /{}").format(di))
                    elif ch==8:
                        user = input("Enter the user name : ")
                        os.system(("useradd {}").format(user))
                    elif ch==9: os.system("firefox")
                        
                       
                        


    
                    elif ch==9: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
                   

            



            
                  

            elif mch==2:
                m=0
                os.system('clear')
                while m!=1:
                    print("""\t\t\t
█▀▄ █▀█ █▀▀ █▄▀ █▀▀ █▀█
█▄▀ █▄█ █▄▄ █░█ ██▄ █▀▄""")
                    os.system("tput setaf 3")
                    print("""
                    [1] Install Docker
                    [2] Check version of Docker
                    [3]  Start the docker service
                    [4]   Download the docker image
                    [5]   To Launch the docker container \n

                    [6] Check docker image
                    [7] Check all stopd container
                    [8] Check status of docker
                    [9] check the logs of particular os
                    [10] Check running Container 
                    [11] To start stop docker container
                    [12]To delete docker image
                    [13]To delete docker container
                    [14]To delete all docker contaier
                    [15] To Exit
                    """)
                   
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
                 
                    if ch==1: os.system("yum install docker-ce --nobest")
                    elif ch==2: os.system("docker --version")
                    elif ch==3:  os.system("systemctl start docker")
                    elif ch==4: 
                        dimage = input("Enter the image name : ")                
                        os.system(("docker pull {}").format(dimage))
                    
                    elif ch==5: 
                        osname = input("Enter the docker os name for good ex : ")
                        dimage = input("Enter the image name : ")
                        os.system(("docker run -it --name {} {}").format(osname,dimage))
                    elif ch==6: os.system("docker images")            
                    elif ch==7:
                        os.system("docker ps -a")
                    elif ch==8:os.system("systemctl status docker")
                        

                    elif ch==9:
                        osname = input("Enter the os name : ")
                        os.system(("docker logs {}").format(osname))
                    elif ch==10:
                        os.system("docker ps ") 
                    elif ch==11:
                        osname = input("Enter the os name : ")
                        os.system(("docker start {}").format(osname))
                        os.system(("docker attach {}").format(osname))
                    elif ch==12:
                        osname = input("Enter the os name : ")
                        os.system(("docker rmi {}").format(osname))
                    elif ch==13:
                        osname = input("Enter the os name : ")
                        os.system(("docker rm {}").format(osname))
                    elif ch==14: os.system("docker rm `docker ps -a -q`")
                    
                    elif ch==15: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
                   
            elif mch==3:
                m=0
                while m!=1:
                    os.system("tput setaf 3")
                    print("""
                    press 1 : To install web server service
                    press 2 : To start web server service
                    press 3 : To write html code
                    press 4 : To stop web service
                    press 5 : To Exit
                    """)
                    
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
                 
                    if ch==1: os.system(" yum install httpd")
                    elif ch==2: os.system("systemctl start httpd")
                    elif ch==3: os.system("vim /etc/var/www/new.html")


                    
                    elif ch==4: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
                   



            
            elif mch==4:    i=1
            else:    print("Wrong Input.......")
            os.system("clear")
            os.system("tput setaf 7")
            
   
    elif r=='remote':
        ip  = input("Enter IP : ")
        i=0
        while i!=1:
            print("""
            press 1 : To General Command
            press 5 : To Docker
            press 6 : To Web Server
            press 7 : To exit
            """)
         
            mch = int(input("Enter your choice : "))
         
            if mch==1:
                m=0
                while m!=1:
                    os.system("tput setaf 3")
                    print("""
                    press  1 : To check date
                    press  2 : To check calender
                    press  3 : To Check Ip Address
                    press  4 : To go in any folder
                    press  5 : To create directory
                    press  6 : To delete directory
                    press  7 : To check files in current folder
                    press  8 : To make users
                    press  9 : To open firefox
                    press 10 : To Exit
                    """)
         
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
              
                    if ch==1: os.system(("ssh root@{} date").format(ip))
                    elif ch==2: os.system(("ssh root@{} cal").format(ip))
                    elif ch==3: os.system(("ssh root@{} ifconfig enp0s3").format(ip))
                    elif ch==4:
                        fpath  = input("Enter the file path as (/etc/root/ : ")        
                        os.system(("ssh root@{} cd {}").format(ip,fpath))
                        input()
                    elif ch==5:
                        di = input("Enter the directory name : ")            
                        os.system(("ssh root@{} mkdir /{}").format(ip,di))
                    elif ch==6:
                        di = input("Enter the directory name : ")
                        os.system(("ssh root@{} rm -rf /{}").format(ip,di))
                    elif ch==7: os.system("ls")
                    elif ch==8:
                        user = input("Enter the user name : ")
                        os.system(("ssh root@{} useradd {}").format(ip,user))
                    elif ch==9:
                        ffox = input("Enter which you want to search or url " )
                        os.system(("ssh root@{} firefox {}").format(ip,ffox))



                    elif ch==10: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
    

            elif mch==2:
                m=0
                while m!=1:
                    os.system("tput setaf 3")
                    print("""
                    press 1  : To install docker
                    press 2  : To check the version of docker
                    press 3  : To check the running container
                    press 4  : To check all the stop container
                    press 5  : To check status of docker
                    press 6  : To check the docker image
                    press 7  : To download the docker image
                    press 8  : To Launch the docker container
                    press 9  : To check the logs of particular os
                    press 10 : To Start the docker service
                    press 11 : To start stop docker container
                    press 12 : To delete docker image
                    press 13 : To delete docker container
                    press 14 : To delete all docker contaier
                    press 15 : To Exit
                    """)
              
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
                   
                    if ch==1: os.system(("ssh root@{} yum install docker-ce --nobest").format(ip))
                    elif ch==2: os.system(("ssh root@{} docker --version").format(ip))
                    elif ch==3: os.system(("ssh root@{} docker ps ").format(ip))
                    elif ch==4: os.system(("ssh root@{} docker ps -a").format(ip))
                    elif ch==5: os.system(("ssh root@{} systemctl status docker").format(ip))
                    elif ch==6: os.system(("ssh root@{} docker images").format(ip))            
                    elif ch==7:
                        dimage = input("Enter the image name ")                
                        os.system(("ssh root@{} docker pull {}").format(ip,dimage))
                    elif ch==8:
                        osname = input("Enter the docker os name for good ex : ")
                        dimage = input("Enter the image name : ")
                        os.system(("ssh root@{} docker run -it --name {} {}").format(ip,osname,dimage))

                    elif ch==9:
                        osname = input("Enter the os name : ")
                        os.system(("ssh root@{} docker logs {}").format(ip,osname))
                    elif ch==10:
                        os.system(("ssh root@{} systemctl start docker").format(ip))

                    elif ch==11:
                        osname = input("Enter the os name : ")
                        os.system(("docker start {}").format(osname))
                        os.system(("docker attach {}").format(osname))
                    elif ch==12:
                        osname = input("Enter the os name : ")
                        os.system(("docker rmi {}").format(osname))
                    elif ch==13:
                        osname = input("Enter the os name : ")
                        os.system(("docker rm {}").format(osname))
                    elif ch==14: os.system("docker rm `docker ps -a -q`")




                   
                    elif ch==15: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
                  


            elif mch==3:
                m=0
                while m!=1:
                    os.system("tput setaf 3")
                    print("""
                    press 1 : To install web server service
                    press 2 : To start web server service
                    press 3 : To write html code
                    press 4 : To stop web service
                    press 5 : To Exit
                    """)
                
                    ch = int(input("Enter your choice : "))
                    os.system("tput setaf 6")
             
                    if ch==1: os.system(("ssh root@{} yum install httpd").format(ip))
                    elif ch==2: os.system(("ssh root@{} systemctl start httpd").format(ip))
                    elif ch==3: os.system(("ssh root@{} vim /etc/var/www/new.html").format(ip))

                  
                    elif ch==5: m=1
                    else:    print("Wrong Input.......")
                    input("Press Enter to continue....")
                    os.system("clear")
                    os.system("tput setaf 7")
                





         
            elif mch==4:    i=1
            else:    print("Wrong Input.......")
            os.system("clear")
            os.system("tput setaf 7")









    elif r=='exit': j=1
    else: print("Wrong Input...")
    os.system("tput setaf 7")

