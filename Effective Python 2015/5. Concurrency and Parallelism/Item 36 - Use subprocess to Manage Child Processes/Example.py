"""
Things to Remember
Use the subprocess module to run child processes and manage their input and output streams.
Child processes run in parallel with the Python interpreter, enabling you to maximize your CPU usage.
Use the timeout parameter with communicate to avoid deadlocks and hanging child processes.
"""

import subprocess

p=subprocess.Popen("dir", shell=True)  
p.wait()  

proc = subprocess.Popen( ['echo', 'Hello from the child!'], shell=True, stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out.decode('utf-8'))


proc = subprocess.Popen(['timeout', '1 > nul'])
while proc.poll() is None:
    print('Working...')
    # Some time-consuming work here
    # ...
print('Exit status', proc.poll())