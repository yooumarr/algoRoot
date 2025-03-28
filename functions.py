import os
import webbrowser
import psutil
import subprocess

def get_system_info():
    info = {
        "os": os.name,
        "platform": os.sys.platform,
        "cpu_count": os.cpu_count(),
    }
    return info

def open_url(url: str):
    webbrowser.open(url)
    return f"Opened URL: {url}"

def create_file(filename: str, content: str = ""):
    with open(filename, "w") as f:
        f.write(content)
    return f"File '{filename}' created."

def get_process_list():
    processes = [{"pid": p.pid, "name": p.name()} for p in psutil.process_iter()]
    return processes

def shutdown_system():
    try:
        if os.name == 'nt':
            subprocess.run(["shutdown", "/s", "/t", "1"], check=True)
            return "System shutdown initiated."
        else:
            subprocess.run(["shutdown", "-h", "now"], check=True)
            return "System shutdown initiated."
    except Exception as e:
        return f"Error shutting down: {e}"

def get_current_directory():
    return os.getcwd()

functions = {
    "get_system_info": get_system_info,
    "open_url": open_url,
    "create_file": create_file,
    "get_process_list": get_process_list,
    "shutdown_system": shutdown_system,
    "get_current_directory": get_current_directory,
}