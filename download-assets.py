from pathlib import Path
import json, urllib.request
root = Path(__file__).resolve().parent
assets = root / 'assets'
assets.mkdir(exist_ok=True)
for name, url in json.loads((root / 'assets.json').read_text()).items():
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
        if not response.headers.get('Content-Type','').startswith('image/'):
            raise ValueError('Not an image: ' + url)
    (assets / name).write_bytes(data)
    print(name, len(data), 'bytes')
