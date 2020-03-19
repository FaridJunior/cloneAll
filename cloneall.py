#!/usr/bin/env python3
from __future__ import unicode_literals
import sys 
import os
import requests

user_name= sys.argv[1]
r =requests.get(f"https://api.github.com/users/{user_name}/repos")

json_responce = r.json()

for i , repo in enumerate(json_responce):
    os.system(f"git clone {repo['clone_url']}")
    