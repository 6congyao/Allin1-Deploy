import subprocess
import time
import sys
import logging

logging.basicConfig(level=logging.INFO, format='From Master: %(asctime)s - %(process)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

args = sys.argv

# Print the arguments
print("Command-line arguments:")
for arg in args:
    print(arg)

print(args)

num_of_requests = int(args[1])
interval = int(args[2])

procs = []
normals = []
abnormals = []

i = 0
for i in range(num_of_requests):
    logger.info(f"This is request number: {i}")
    # Start the child process
    proc = subprocess.Popen(['python', 'multi-process-client.py'])
    procs.append(proc)
    # Do other things while the process is running
    logger.info(f"sleeping for {interval} seconds after sending request number: {i}")
    time.sleep(interval)


j = 0
for j in range(num_of_requests):
    return_code = procs[j].wait()
    logger.info(f"Request number {j} finished with return code {return_code}.")
    if return_code == 0:
        normals.append(return_code)
    else:
        abnormals.append(return_code)

print('请求次数：',num_of_requests)
print('不正常响应次数：', len(abnormals))
print('正常响应次数：', len(normals))
