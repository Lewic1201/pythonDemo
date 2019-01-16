import re

test2 = "['GET', '/ikepolicies/{id}', '获取IKE策略详情']"
print(re.sub('[{}]', '', re.sub('[-/]', '_', test2)))
