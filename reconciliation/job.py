from dataclasses import dataclass, field
from enum import Enum
from typing import Dict


class JobType(Enum):
    SYSTEM_STATS = "SYSTEM_STATS"
    REMOTE_STATE = "REMOTE_STATE"
    REGISTER_CONTROLLER = "REGISTER_CONTROLLER"
    HANDLE_UPDATE = "HANDLE_UPDATE"


JOB_PRIORITIES: Dict[str, int] = {
    JobType.SYSTEM_STATS.value: 1,
    JobType.HANDLE_REQUEST.value: 10,
    JobType.SYNCHRONISE: 15,
    JobType.REGISTER_CONTROLLER.value: 20,
}


@dataclass(order=True)
class ReconciliationJob:
    priority: int
    job: Any=field(compare=False)
