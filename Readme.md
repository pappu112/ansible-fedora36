### STEP 1: install as root

````
dnf update

dnf -y install iptables-legacy

alternatives --config iptables
````

There are 2 programs which provide 'iptables'.

  Selection    Command
-----------------------------------------------
*+ 1           /usr/sbin/iptables-nft
   2           /usr/sbin/iptables-legacy

# switch to [iptables-legacy]
Enter to keep the current selection[+], or type selection number: 2

#### STEP 2: install ansible

````
dnf -y install ansible
````

#### STEP 3: 
GO inside ansible folder 

````
ansible-playbook playbook-config.yml --ask-become-pass
````

reboot

#### STEP 4:

````
ansible-playbook playbook-install.yml --ask-become-pass
````

