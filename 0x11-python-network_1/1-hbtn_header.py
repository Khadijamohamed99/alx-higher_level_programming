#!/usr/bin/python3
""" sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    import urllib.request as r
    import sys

    url = sys.argv[1]
    with r.urlopen(url) as res:
        data = res.info()
        print(data.get('X-Request-Id'))
