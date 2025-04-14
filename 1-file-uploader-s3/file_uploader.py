import boto3
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



bucket_name = "derking-bucket-0414"
watch_path = "to_upload"
uploaded_path = "uploaded"

s3 = boto3.client("s3")

class UploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            try:
                s3.upload_file(event.src_path, bucket_name, file_name)
                print(f"Downloaded: {file_name}")
                shutil.move(event.src_path, os.path.join(uploaded_path, file_name))
            except Exception as e:
                print(f"Error: {e}")

observer = Observer()
observer.schedule(UploadHandler(), watch_path, recursive=False)
observer.start()

print("Please upload a file, AWS will work")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
