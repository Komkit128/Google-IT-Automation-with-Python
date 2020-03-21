#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)



#!/usr/bin/env python
import subprocess
src = "/home/student-00-1b4b0180a349/data/prod/" # replace <source-path> with the source directory
dest = "/home/student-00-1b4b0180a349/data/prod_backup/" # replace <destination-path> with the destination directory
subprocess.call(["rsync", "-arq", src, dest])


#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
src = "/home/student-00-1b4b0180a349/data/prod/" # replace <source-path> with the source directory
dest = "/home/student-00-1b4b0180a349/data/prod_backup/" # replace <destination-path> with the destination directory
def run(task):
  # Do something with task here
    subprocess.call(["rsync", "-arq", src, dest])
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
