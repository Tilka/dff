#!/usr/bin/env python3

import requests
import os.path

root = 'https://fifo.ci'
dff_list = requests.get(root + '/dff/').json()
print(len(dff_list), 'files')
for dff in dff_list:
    path = 'media/' + dff['filename']
    if not os.path.exists(path):
        print(dff['filename'], dff['shortname'])
        blob = requests.get(root + dff['url'])
        open(path, 'wb+').write(blob.content)
print('done')
