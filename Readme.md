Need to add aws access key and access secret key in 

minio/minio-configmap.yaml
mlflow/mlflow-configmap.yaml
myapp/download.py


 

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

#### STEP 3: Run ansible before reboot
GO inside ansible folder 

````
ansible-playbook playbook-config.yml --ask-become-pass
````

reboot

#### STEP 4: Run ansible after reboot

````
ansible-playbook playbook-install.yml --ask-become-pass
````

#### STEP 5: Register runner 


add in /etc/hosts
<containme ip> gitlab-service.default 

than 

````
gitlab-runner register
````
if runner not live 

````
gitlab-runner verify
````
#### STEP 6: upload model in gitlab project 
upload  files in gitlab project
train.py (in mlflow folder)
kc_house_data.cvs(in mlflow floder)
all file in my app folder in root directory on gitlab project

Commit the files

#### STEP 10 : Run pipeline
upload .gitlab-ci.yaml in gitlab project

commit the file pipeline should run automitaclly after commit  
 
#### STEP 11: ADD HTTPS IN GITLAB 
go to gitlab folder amd run 
````
kubectl create -f ingress.yaml
````
for browse withh https need to add host in /etc/hosts
````
127.0.0.1 nndata.mlopps.com
````

