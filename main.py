from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class Myhandler (FileSystemEventHandler):
    def on_modified(self, event):
        i =1
        if filename != 'kalle':
            new_name = filename
            split_name = filename.split('.')
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                i+=1
                new_name = os.path.splitext(folder_to_track + '/' +new_name)[0] + str(i) + os.path.sp
                new_name = new_name.split("/")[4]
                file_exists = os.path.isfile(folder_destination +"/"+ new_name)
                
            src = folder_to_track + "/" + filename
            new_name = folder_destination + "/" +new_name
            os.rename(src, new_name)
folder_to_track = '/Users/hussah01/Desktop'
folder_destination = '/Users/hussah01/Desktop/kalle'
event_handler = Myhandler()
observer = Observer()
observer.scheduele(event_handler,folder_to_track, recursive = True)
observer.start

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join() 
