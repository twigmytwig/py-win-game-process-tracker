#import wmi
import os
import time
import sys
import psutil
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
import tkinter as tk

class ProcessMonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Process Monitor")

        self.label = QLabel("Latest Process Name: None", self)
        self.label.setFont(self.font())
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_process_name(self, process_name):
        self.label.setText(f"Latest Process Name: {process_name}")


process_name = "Fallout76.exe"

def filter_by_name(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                yield process
        except psutil.NoSuchProcess:
            pass


def is_running(process_name):
    return any(p for p in filter_by_name(process_name))

'''
def initProcessWatch(app):
    seen_process_ids = set()

    while True:
        # Get the list of current running processes
        current_processes = psutil.process_iter(['pid', 'name'])

        for process in current_processes:
            pid = process.info['pid']
            name = process.info['name']

            # Check if this process is new (i.e., not seen before)
            if pid not in seen_process_ids:
                # Print information about the new process
                print(f"New process started - PID: {pid}, Name: {name}")
                if(name == process_name):
                    app.update_process_name(name)
                    for p in filter_by_name(process_name):
                        print("Timing " + name)
                        p.wait()
                        print(time.time() - p.create_time())
                # Add this process ID to the set of seen process IDs
                seen_process_ids.add(pid)

        # Wait for a short interval before checking again (e.g., 1 second)
        time.sleep(1)
'''
def monitor_processes(app):
    existing_processes = set(p.name() for p in psutil.process_iter())

    timer = QTimer()
    

    def check_processes():
        print("-------")
        nonlocal existing_processes
        new_processes = set(p.name() for p in psutil.process_iter()) - existing_processes
        print(new_processes)
        if new_processes:
            latest_process_name = new_processes.pop()  # Get the name of the latest new process
            app.update_process_name(latest_process_name)
            existing_processes.update(new_processes)
    print("Henlo")
    timer.timeout.connect(check_processes)
    timer.start(2000)  # Check for new processes every 1 second
    print(timer)


if __name__ == "__main__":
    #os.system("taskkill /f /im Fallout76.exe")
    app = QApplication(sys.argv)
    window = ProcessMonitorApp()
    window.show()
    
    # Start monitoring processes
    monitor_processes(window)
    
    sys.exit(app.exec())



'''
# Initializing the wmi constructor
f = wmi.WMI()
 
# Printing the header for the later columns
print("pid   Process name")
 
# Iterating through all the running processes 
for process in f.Win32_Process():
     
    # Displaying the P_ID and P_Name of the process

    print(f"{process.ProcessId:<10} {process.Name}") 

print("-------")
'''




'''
if is_running(u"{0}".format(process_name)):
    print(u"{0} is running.".format(process_name))
else:
    print(u"Bad news, {0}'s dead!".format(process_name))

for p in filter_by_name(process_name):
    p.wait()
    print(time.time() - p.create_time())

'''

#/f specifies that processes be forecefully terminated and /im (ImageName) specifies the image name of the process to be terminated
#os.system("taskkill /f /im Fallout76.exe")
