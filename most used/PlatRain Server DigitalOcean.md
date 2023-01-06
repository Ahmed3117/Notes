# SSH : Secure Shell 💎
 - The Secure Shell Protocol (SSH) 
 - is a cryptographic network protocol .
 - for operating network services securely over an unsecured network .
 - to access on other machine using password
     - using the following command 

       
       ssh root_machine_name@machine_ip
       
     - then enter password 

#### ubuntu-platrain-v2 on DigitalOcean 
ssh
ssh root@143.110.168.90

password
with010*#ALLAH
##################
to run the project in browser :
http://143.110.168.90:8000/
##################
in fire wall problem :
* ufw status
if inactive , do these two commands to activate it :
	* deactivate  # to deactivate the environment
	* ufw enable
	* sudo ufw allow 8000   # to allow port 8000 on digital ocean machine



i have a jango model with imagefield , i need to create instance of it 
------------------------------------------

ssh root@143.110.168.90
systemctl restart gunicorn

systemctl status gunicorn