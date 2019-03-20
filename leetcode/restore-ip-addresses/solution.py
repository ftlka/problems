from collections import deque


def create_branch(i, s, size):
	if i + size > len(s):
		return
	cut = s[i:i + size]
	if not (cut.startswith('0') and size > 1) and int(cut) < 256:
		return cut


def restoreIpAddresses(s):
	ips = set()

	stack = deque()
	for i in range(1, 4):
		branch_ip = create_branch(0, s, i)
		if branch_ip:
			stack.append([i, [branch_ip], 1])

	while stack:
		i, branch_ip, iter_num = stack.pop()
		if iter_num == 4:
			if i >= len(s) and len(branch_ip) == 4:
				ips.add('.'.join(branch_ip))
		else:
			for idx in range(1, 4):
				new_ip_part = create_branch(i, s, idx)
				if new_ip_part:
					stack.append([idx + i, branch_ip + [new_ip_part], iter_num + 1])
	return list(ips)
        