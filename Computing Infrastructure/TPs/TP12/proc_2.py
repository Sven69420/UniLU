import os
import psutil

def main():
    x = 1
    pid = os.fork()

    if pid == 0:  # Child process
        print(f"child: x={x+1}")
        print(f"child process ID: {os.getpid()}")
        
        # Use psutil to get the process status
        proc = psutil.Process(os.getpid())
        print(f"child process state: {proc.status()}")
        print(f"child process ID from psutil: {proc.pid}")
        
        os._exit(0)
    else:  # Parent process
        print(f"parent: x={x-1}")
        print(f"parent process ID: {os.getpid()}")
        os._exit(0)

if __name__ == "__main__":
    main()
