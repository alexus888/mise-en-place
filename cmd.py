import subprocess
import signal
import sys
import shutil
import threading
from pathlib import Path
from typing import Union
from tempfile import TemporaryDirectory


def watch(file: Union[Path, str], dest: Union[Path, str] = Path.home() / "Desktop"):
    procs = []

    temp_dir = TemporaryDirectory()
    temp_file = str(Path(temp_dir.name) / "output.svg")

    NODEMON_CMD = [
        "npx",
        "nodemon",
        "--watch",
        file,
        "--exec",
        f"mmdc -i {file} -o {temp_file}",
    ]

    LIVE_SERVER_CMD = [
        "npx",
        "live-server",
        temp_dir.name,
        "--open=./output.svg",
    ]

    def _listen():
        print("Press 's' + Enter to save the current SVG.")
        while True:
            if input().strip().lower() == "s":
                out = dest / Path(file).with_suffix(".svg").name
                shutil.copy(temp_file, out)
                print(f"Saved to {out}")

    try:
        subprocess.run(["mmdc", "-i", str(file), "-o", temp_file], check=True)

        procs.append(subprocess.Popen(NODEMON_CMD))
        procs.append(subprocess.Popen(LIVE_SERVER_CMD))

        threading.Thread(target=_listen, daemon=True).start()

        def _shutdown(sig, frame):
            _ = sig, frame
            for p in procs:
                p.terminate()
            temp_dir.cleanup()
            sys.exit(0)

        signal.signal(signal.SIGINT, _shutdown)
        signal.signal(signal.SIGTERM, _shutdown)

        for p in procs:
            p.wait()

    except Exception as e:
        for p in procs:
            p.terminate()
        raise e
