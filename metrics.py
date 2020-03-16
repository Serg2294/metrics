import psutil
import sys

# psutil.PROCFS_PATH = '/proc'

def get_cpu():
    print('system.cpu.idle', psutil.cpu_times().idle)
    print('system.cpu.user', psutil.cpu_times().user)
    print('system.cpu.guest', psutil.cpu_times().guest)
    print('system.cpu.iowait', psutil.cpu_times().iowait)
    print('system.cpu.stolen', psutil.cpu_times().steal)
    print('system.cpu.system ', psutil.cpu_times().system)

def get_memory():
    print('virtual total ', psutil.virtual_memory().total)
    print('virtual used ', psutil.virtual_memory().used)
    print('virtual free ', psutil.virtual_memory().free)
    print('virtual shared ', psutil.virtual_memory().shared)
    print('swap total ', psutil.swap_memory().total)
    print('swap used ', psutil.swap_memory().used)
    print('swap free ', psutil.swap_memory().free)


if len(sys.argv) - 1 > 1:
    print("Please type only 'cpu' or 'mem'")
elif len(sys.argv) - 1 == 0:
    print("Please type 'cpu' or 'mem'")
else:
    if sys.argv[1] == "cpu":
        get_cpu()
    elif sys.argv[1] == "mem":
        get_memory()
    else:
        print("Incorrect argument. Please type only 'cpu' or 'mem'")