from queue import PriorityQueue
from threading import Lock, Thread, Event, Timer

from .job import ReconciliationJob, JobType
from .controller import ControllerRegistry

class Controller:
    def update():
        pass

class Reconciler:
    def __init__(self, state: State, timeout, max_queue_length, sync_interval):
        self.queue = PriorityQueue()
        self.controllers = ControllerRegistry()
        self.reconciliation_thread = Thread(target=self._reconcile)

    def _reconcile(self):
        while True:
            try:
                j = self.queue.get()
                with self.state:
                    match j.job.get("operation"):
                        case JobType.SYSTEM_STATS:
                            pass
                        case JobType.REMOTE_STATE:
                            pass
                        case JobType.REGISTER_CONTROLLER:
                            self.controllers.register(j.job)
                        case JobType.HANDLE_UPDATE:
                            self.controllers(j.job)
            except Exception as e:
                print(e)

    def enqueue(self, job: ReconciliationJob):
        self.queue.put(job)

    def stop(self):
        pass