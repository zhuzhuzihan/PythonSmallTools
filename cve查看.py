import requests
import responses
import json


year = input('请输入日期: 20')
code = input('请输入后缀: ')
url = f'https://cveawg.mitre.org/api/cve/CVE-20{year}-{code}'
response = requests.get(url)
data = json.loads(response.content)
data = json.dumps(data, indent=4, ensure_ascii=False)
