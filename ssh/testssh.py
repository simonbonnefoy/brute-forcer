import multiprocessing as mp
import paramiko
import time

def ssh(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try :
        print('Testing password: ', password)
        ssh.connect('127.0.0.1', username='user', password=password)
        return True
    except paramiko.ssh_exception.AuthenticationException:
        print("authentication failed")
        return False


if __name__ == '__main__':
    pass_list = ['test1','test2','test3', 'test3', 'test3', 'test3', 'test3']
    pool = mp.Pool(processes=2)
    t1 = time.time()
    '''for synchronous'''
    [pool.apply(ssh, args=(x,)) for x in pass_list]
    '''For Asynchronous'''
    results = [pool.apply_async(ssh, args=(x,)) for x in pass_list]
    pool = mp.Pool(processes=4)
    output = [p.get() for p in results]
    print(output)
    print('Code executed in: ', time.time() - t1)