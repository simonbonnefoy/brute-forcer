Suite of script for brute force attack.
So far the program is compatible with python2/3
The following librairies are needed

!!!Note, the GUI is made to work on python3, not maintenance for python2!!!


###############################################  
To install all the dependencies on Kali linux:  
###############################################  
  
`apt-get install build-essential libssl-dev libffi-dev python-dev gcc  `
`apt-get install libffi-dev `
´apt-get install python3-pyqt5   `  

For GUI devel  
apt-get install pyqt5-dev-tools  
apt-get install qttools5-dev-tools  
apt-get install qttools5-dev  

pip install paramiko  
pip install python-nmap  
pip install mysql-connector-python  
pip install pytest  

http://docs.paramiko.org/en/2.4/api/client.html  
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html  
https://pypi.org/project/python-nmap/  
https://pytest.org/en/latest/  

######################  
Running the test unit  
######################  
To run the test unit, and check that all the   
librairies are correctly loaded, just type `pytest` in the main  
folder, where the test_sample.py is located.  
pytest will go through the test in the test_sample.py, and report any  
problem during the unit test.
  
####################  
Setting the system  
####################  
On kali linux the ssh server is not running by default,   
you need to start it.  
Run the following command to start the ssh server:  
`systemctl start ssh`  
This is not required for the test unit, but to test the ssh bruteforce  
on your local computer.  

