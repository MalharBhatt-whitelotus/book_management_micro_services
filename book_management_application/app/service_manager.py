import sys
import time
import threading
import subprocess

class ServiceManager:

    def __init__(self):
        self.processes = {}
        self.running = True
    
    def _launch_service(self, module: str, port: int):
        return subprocess.Popen([sys.executable, "-m", "uvicorn", f"{module}:app", "--port", str(port)])

    def start_service(self, name, module, port):
        process = self._launch_service(module, port)
        self.processes[name] = {"module":module,"port":port,"process":process}

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
    
    