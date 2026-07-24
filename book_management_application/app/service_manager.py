import sys
import time
import threading
import subprocess

class ServiceManager:

    def __init__(self):
        self.processes = {}
        self.running = True
    
    def _launch_service(self, module: str, port: int, working_dir : str):
        return subprocess.Popen([sys.executable, "-m", "uvicorn", f"{module}:app", "--port", str(port)], cwd=working_dir)

    def start_service(self, name: str, module: str, port: int, working_dir: str = "/Users/maulik/malhar /day-16 task2"):
        process = self._launch_service(module, port, working_dir)
        self.processes[name] = {"module":module,"port":port,"process":process,"cwd":working_dir}

    def stop_all(self):
        self.running = False
        self.monitor_thread.join(timeout=2)

        for service in self.processes.values():
            service["process"].terminate()
        
        for service in self.processes.values():
            service["process"].wait()
    
    def start_monitor(self):
        self.monitor_thread = threading.Thread(target=self.monitor, daemon=True)
        self.monitor_thread.start()

    def monitor(self):
        while self.running:
            for name, services in self.processes.items():
                if services["process"].poll() is not None:
                    if not self.running: break
                    print(f"The {name} service has stopped. Trying to restart the {name} service ...")
                    print(f"Restarting {name} service ....")
                    try:
                        process = self._launch_service(services["module"], services["port"])
                        services["process"] = process
                    except Exception as e:
                        print(f"Failed to restart the {name} services: {e}")
                else: print(f"The {name} service is running ...")
            time.sleep(5)
    
    