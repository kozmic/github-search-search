# Search in github search results

Typical use case:
Find all projects with specific dependency,
in projects with that dependency, search for a specific code snippet.

Example:
The npm module `koa-body` is vulnerable for local file inclusion (LFI) in certain scenarios when `multipart: true`.
To find all projects that has `koa-body` as a dependency, and the search those projects for `multipart: true` you would run:

```
./search.py koa-body "multipart: true"
```

Setup access token to Github or Github Enterprise:
```
export GH_SERVER="https://github.example.com/"
export GH_TOKEN=<YOUR-PERSONAL-GITHUB-ENTERPRISE-TOKEN>
```




