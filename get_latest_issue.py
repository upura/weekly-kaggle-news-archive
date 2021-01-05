import argparse

import requests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--token')
    args = parser.parse_args()

    url = 'https://www.getrevue.co/api/v2/issues/latest'
    headers = {'Authorization': f'Token {args.token}'}

    req = requests.get(url, headers=headers)
    for issue in req.json()['issue']:
        _title = issue['title']
        _html = issue['html']
        _sent_at = issue['sent_at']
        _url = issue['url']
        with open(f'issues/{_sent_at[:10]}_{_title}.md', mode='w') as f:
            f.write(f'# {_title}\n')
            f.write(f'{_url}\n')
            f.write(_html)
