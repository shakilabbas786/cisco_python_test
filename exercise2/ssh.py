import paramiko, getpass

ip=raw_input("Enter server ip:")
port=22
username=raw_input("Enter username:")
password=getpass.getpass("Enter password:")

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

def check_command(option):
    if option == "1":
        execute_command("df -hT")
    elif option == "2":
        execute_command("df -i")
    elif option == "3":
        execute_command("ls -ltrh")
    elif option == "exit":
        print "Good Bye!! :)"
    else:
        print "Invalid option entered!"

def execute_command(cmd):
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print resp

option = ""
while (option != "exit"):
    print "Enter your choice:"
    print "1. Check disk usage"
    print "2. Inode usage"
    print "3. Get list of files from current path"
    print "Enter exit to finish"
    option = raw_input()
    check_command(option)
