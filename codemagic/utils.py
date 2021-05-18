import requests
import logging
import re


def get_codemagic_url(relative_url=None):
    url = 'https://api.codemagic.io'
    if relative_url:
        url = '{}/{}'.format(url, relative_url.lstrip('/'))
    return url


def prepare_headers(token) -> dict:
    return {
        'x-auth-token': token,
        'Content-Type': 'application/json',
    }


def send_get_request(url, data={}, headers={}) -> dict:
    r = requests.get(
        url,
        params=data,
        headers=headers,
    )
    return _handle_response(r)


def send_post_request(url, data={}, headers={}) -> dict:
    r = requests.post(
        url,
        headers=headers,
        json=data,
    )
    return _handle_response(r)


def _handle_response(response):
    if not (200 <= response.status_code < 300):
        logging.exception("Request failed", stack_info=True, )
    data = response.json()
    return data


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
