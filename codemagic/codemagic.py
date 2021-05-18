from .builds import Build
from .utils import send_get_request, send_post_request, get_codemagic_url, prepare_headers, camel_to_snake


class Codemagic:

    def __init__(self, token):
        self.token = token

    def start_build(self, app_id: str, workflow_id: str, branch: str, environment: dict) -> Build:
        data = {
            'appId': app_id,
            'workflowId': workflow_id,
            'branch': branch,
            'environment': environment,
        }
        response = send_post_request(get_codemagic_url('/builds'), data=data, headers=prepare_headers(self.token))
        return self.get_build(response.get("buildId"))

    def list_of_builds(self, app_id=None, workflow_id=None, branch=None, tag=None) -> [Build]:
        data = {
            'appId': app_id,
            'workflowId': workflow_id,
            'branch': branch,
            'tag': tag
        }
        response = send_get_request(get_codemagic_url('/builds'), data=data, headers=prepare_headers(self.token))
        items = []
        for build_dict in response.get('builds', []):
            items.append(self.to_build(build_dict))
        return items

    def get_build(self, pk: str):
        response = send_get_request(get_codemagic_url(f'/builds/{pk}'), headers=prepare_headers(self.token))
        return self.to_build(response.get('build', {}))

    def cancel_build(self, pk: str):
        response = send_post_request(get_codemagic_url(f'/builds/{pk}/cancel'), headers=prepare_headers(self.token))
        return self.to_build(response.get('build', {}))

    @staticmethod
    def to_build(build_dict) -> Build:
        build = Build()
        keys = {}
        for key in build_dict.keys():
            keys[key] = camel_to_snake(key)

        keys['_id'] = 'pk'
        for key in keys:
            if hasattr(build, keys[key]) and build_dict.get(key, None):
                setattr(build, keys[key], build_dict[key])
        return build
