import os
import shlex
from multiprocessing import Process
from bokeh.command.bootstrap import main

exampleFolder = '.'  # Replace with the actual path to your Examples folder

# Get a list of all files in the Examples folder
exampleFiles = [file for file in os.listdir(exampleFolder) if os.path.isfile(os.path.join(exampleFolder, file))]

# Define a starting port number
startPort = 57878

# Create a list of arguments for each Bokeh server with unique port numbers
argss = [f'--port {startPort + i} --allow-websocket-origin localhost:{startPort + i} {os.path.join(exampleFolder, file)}' for i, file in enumerate(exampleFiles)]

if __name__ == '__main__':
    # Start a separate process for each Bokeh server
    processes = [Process(target=main, args=(['python', 'serve'] + shlex.split(args),)) for args in argss]
    for p in processes:
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()