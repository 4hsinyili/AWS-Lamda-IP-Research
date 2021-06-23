ip_list_1 = [
    '18.180.155.33',
    '54.199.130.150',
    '54.249.201.245',
    '18.183.66.254',
    '18.176.178.8',
    '54.168.103.54',
    '35.74.64.29',
    '18.176.178.8',

    '18.176.178.8',
    '54.168.103.54',
    '18.183.66.254',
    '18.176.178.8',
    '35.74.64.29',
    '54.249.201.245',
    '54.199.130.150',
    '18.180.155.33',
    '54.168.103.54',
    '18.181.109.112',
    '35.73.202.91',
    '18.181.170.187',

    '18.181.170.187',
    '35.73.202.91',
    '18.181.109.112',
    '54.168.103.54',
    '54.199.130.150',
    '18.180.155.33',
    '54.249.201.245',
    '18.176.178.8',
    '35.74.64.29',
    '18.183.66.254',
    '54.168.103.54',
    '18.181.170.187',
    '35.73.202.91',
    '35.74.64.29',
    '54.168.103.54',
    '18.181.170.187',
]

ip_list_2 = [
    '18.181.19.233',
    '3.113.25.180',
    '18.183.230.145',
    '18.183.147.70',
    '13.231.117.47',
    '18.181.237.125',
    '52.195.13.171',
    '13.231.248.73',

    '13.231.248.73',
    '52.195.13.171',
    '18.183.147.70',
    '13.231.117.47',
    '18.181.237.125',
    '18.183.230.145',
    '3.113.25.180',
    '18.181.19.233',
    '18.179.17.138',
    '35.75.4.150',
    '13.115.110.19',
    '54.168.196.5',

    '54.168.196.5',
    '13.115.110.19',
    '18.179.17.138',
    '35.75.4.150',
    '3.113.25.180',
    '18.181.19.233',
    '18.181.237.125',
    '18.183.230.145',
    '13.231.117.47',
    '18.183.147.70',
    '52.195.13.171',
    '13.231.248.73',
    '18.183.230.145',
    '18.183.147.70',
    '52.195.13.171',
    '18.183.230.145',
]
ip_set_1 = set(ip_list_1)

print('There are ', len(ip_list_1), ' ips in list_1.')
print('There are unique', len(ip_set_1), ' ips in list_1.')
print('-----------')

ip_set_2 = set(ip_list_2)
print('There are ', len(ip_list_2), ' ips in list_2.')
print('There are unique', len(ip_set_2), ' ips in list_2.')
print('-----------')

ip_set_1.update(ip_set_2)
ip_set = ip_set_1
print('There are ', len(ip_set), 'unique ips in list_1 and list_2.')
