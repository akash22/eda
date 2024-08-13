import time
import psutil
from ansible.events import EventSource

class CpuMonitor(EventSource):
    def __init__(self, threshold):
        self.threshold = threshold

    def listen(self):
        while True:
            utilization = psutil.cpu_percent(interval=1)
            if utilization > self.threshold:
                yield {
                    'utilization': utilization
                }
            time.sleep(1)
