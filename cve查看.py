import requests
import responses
import json


# def get_cve(cve_year, cve_code):
    # url = f'https://cveawg.mitre.org/api/cve/CVE-20{cve_year}-{cve_code}'
    # get = responses.get(url)


year = input('请输入日期: 20')
code = input('请输入后缀: ')
# get_cve(year, code)
url = f'https://cveawg.mitre.org/api/cve/CVE-20{year}-{code}'
response = requests.get(url)
data = json.loads(response.content)
data = json.dumps(data, indent=4, ensure_ascii=False)
print(data)
