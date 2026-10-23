
import os
from datetime import datetime, timedelta


def scan_files(folder):
    results = []

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        if os.path.isfile(path):
            info = os.stat(path)

            size = info.st_size
            file_type = os.path.splitext(filename)[1]

            modified = datetime.fromtimestamp(info.st_mtime)

            age = datetime.now() - modified

            old = age > timedelta(days=30)

            fine = max(0, age.days - 30) * 10

            results.append({
                "name": filename,
                "size": size,
                "type": file_type,
                "modified": modified.strftime("%Y-%m-%d"),
                "status": "OLD" if old else "OK",
                "fine": fine
            })

    return results
