# httpbin-re: HTTP Request & Response Service

Updates and **RE**build based on [Kenneth Reitz](http://kennethreitz.org/bitcoin)'s project

![tw ice cream](/images/tw-ice-cream.jpg)

Run locally:

```sh
docker pull ghcr.io/pichuang/httpbin-re:master
docker run -p 8080:80 ghcr.io/pichuang/httpbin-re:master

# or
docker-compose up -d
```

See http://httpbin.org for more information.

## Major Changelog

- Change
  - Ubuntu 18.04 -> Ubuntu 22.04
  - Travis CI -> GitHub Actions
  - Python 3.6 -> Python 3.10
  - Pipenv -> built-in pip
- Add
  - Provide variables to change TITLE and DESCRIPTION
  - Follow OCI Specification

## References

- [httpbin](http://httpbin.org)

## SEE ALSO

- http://requestb.in
- http://python-requests.org
- https://grpcb.in/
