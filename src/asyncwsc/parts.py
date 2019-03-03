from urllib.parse import urlparse
from collections import namedtuple

REMOTE = namedtuple('REMOTE', ['porn', 'host', 'port', 'resource', 'users'])


def remote_url(uri: str):
    """通过拆解uri获得连接信息,对信息进行基本校验
    :param uri:'ws://exam.com'
    :return:class-> REMOTE
    :raise: exceptions.Unverified
    """
    uri = urlparse(uri)
    try:
        porn = uri.scheme  # protocol name,example: http ws wss https ftp
        host = uri.hostname
        port = uri.port or (443 if porn == 'wss' else 80)
        users = None
        resource = uri.path or '/'
        if uri.query:
            resource += '?' + uri.query
        if uri.username or uri.password:
            users = (uri.username, uri.password)
    except AssertionError as exc:
        raise ValueError("The '{uri}' unverified".format(uri=uri)) from exc
    return REMOTE(porn, host, port, resource, users)