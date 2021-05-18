from datetime import datetime

from codemagic.apps import Application
from codemagic.enums import Choices


class BuildStatus(Choices):
    FINISHED = 'finished'
    BUILDING = 'building'
    FAILED = 'failed'
    CANCELED = 'canceled'
    QUEUED = 'queued'


class Build:
    pk: str = None
    app: Application = None
    status: BuildStatus = None
    workflow_id: str = None
    started_at: datetime = None

    def __init__(self):
        pass
