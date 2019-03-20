from solution import restoreIpAddresses


assert set(restoreIpAddresses('25525511135')) == {'255.255.11.135', '255.255.111.35'}

assert set(restoreIpAddresses('351936026')) == {'35.193.60.26'}

assert restoreIpAddresses('8888') == ['8.8.8.8']

assert restoreIpAddresses('0000') == ['0.0.0.0']
