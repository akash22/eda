import time
import psutil
from ansible_rulebook.engine import EventSource

class CpuMonitor(EventSource):
    def __init__(self, threshold=60):
        self.threshold = threshold

    def listen(self):
        while True:
            utilization = psutil.cpu_percent(interval=1)
            if utilization > self.threshold:
                yield {
                    'utilization': utilization,
                    'message': f'CPU usage exceeded {self.threshold}%. Current usage: {utilization}%.'
                }
            time.sleep(1)
