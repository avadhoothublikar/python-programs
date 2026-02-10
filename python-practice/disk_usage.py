import shutil

total, used, free = shutil.disk_usage("/")

usage = used / total * 100

if usage > 80:
    print("disk usage has crossed threshold", usage)