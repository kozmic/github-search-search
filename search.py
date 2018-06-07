#!/usr/bin/env python
import os
import sys
import urllib.request
from urllib.parse import urlencode, quote_plus
import json

def main():
    try:
        ghtoken = os.environ["GH_TOKEN"]
    except KeyError:
        print("Please set the environment variable GH_TOKEN")
        sys.exit(1)

    try:
        ghserver = os.environ["GH_SERVER"]
    except KeyError:
        print("Please set the environment variable GH_SERVER")
        sys.exit(1)

    if len(sys.argv) != 3:
        print("No search argument passed to script. Two search arguments required.")
        sys.exit(1)

    repo_search_term = sys.argv[1]
    code_search_term = sys.argv[2]
    print("Searching in repositiries for: '" + repo_search_term + "'")
    repo_search_params = urlencode({'q': repo_search_term}, quote_via=quote_plus)
    repo_url = ghserver + '/api/v3/search/code?%s' % repo_search_params
    req = urllib.request.Request(repo_url)
    req.add_header('Authorization', 'token ' + ghtoken)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    response = urllib.request.urlopen(req)
    json_response = json.load(response)
    repos = []
    for item in json_response['items']:
            repos.append(item['repository']['full_name'])

    print("Searching for '" + code_search_term + "' in the following repos: " + ','.join(repos))
    code_search_params = urllib.parse.urlencode({'q': code_search_term + " repo:" + ' repo:'.join(repos)}, quote_via=quote_plus)
    code_url = ghserver + '/api/v3/search/code?%s' % code_search_params
    req = urllib.request.Request(code_url)
    req.add_header('Authorization', 'token ' + ghtoken)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    response = urllib.request.urlopen(req)
    json_response = json.load(response)
    
    print("Results: ")
    for item in json_response['items']:
        print(item['html_url'])
    if json_response['total_count'] == 0:
        print("No results found.")


if __name__ == '__main__':
    main()
