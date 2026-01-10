import sys

sites_count, query_count = map(int, sys.stdin.readline().split())
password_dict = dict()
for _ in range(sites_count):
    site_domain, password = map(str, sys.stdin.readline().split())
    password_dict[site_domain] = password
for _ in range(query_count):
    query_site = str(sys.stdin.readline().strip())
    print(password_dict[query_site])
