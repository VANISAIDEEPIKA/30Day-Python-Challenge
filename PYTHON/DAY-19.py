import threading
import time

def download_file(file_name):
    print(f"Starting download: {file_name}")
    time.sleep(2)
    print(f"Finished downloading: {file_name}")

files = ['file1.txt', 'file2.txt', 'file3.txt']
threads = []

for file in files:
    t = threading.Thread(target=download_file, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All downloads complete!")
