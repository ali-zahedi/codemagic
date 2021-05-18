from datetime import datetime

from codemagic.enums import Choices


class ProjectType(Choices):
    FLUTTER_APP = 'flutter-app'


class Application:
    pk: str
    app_name: str
    archived: bool
    branches: str
    created_at: datetime
    file_workflow_ids: list = []
    last_build_id: str
    project_type: ProjectType
