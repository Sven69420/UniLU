import os

def main():
    x = 1
    pid = os.fork()

    if pid == 0:  # Child process
        print(f"child: x={x+1}")
        print(f"child process ID: {os.getpid()}")
        os._exit(0)
    else:  # Parent process
        print(f"parent: x={x-1}")
        print(f"parent process ID: {os.getpid()}")
        os._exit(0)

if __name__ == "__main__":
    main()
