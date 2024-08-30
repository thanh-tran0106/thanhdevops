import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()

# remote server credentials
host = "13.60.180.237"
username = "ubuntu"
password = "m4st3r"
port = 22

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

# create an SFTP client object
ftp = ssh_client.open_sftp()

# download a file from the remote server
files = ftp.put("/home/ubuntu/media/cats_photos/laila.jpg","/home/ubuntu/media/cats_photos/laila.jpg")

# close the connection
ftp.close()
ssh_client.close()
