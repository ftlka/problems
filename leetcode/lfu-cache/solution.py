class LFUCache(object):

	def __init__(self, capacity):
		self.limit = self.capacity = capacity

		self.storage = {}
		self.key_used = {}
		self.used_counts_to_keys = {0: []}

	def _update_key_info(self, key):
		# add new vals
		self.key_used[key] += 1
		times_used = self.key_used[key]
		if times_used in self.used_counts_to_keys:
			self.used_counts_to_keys[times_used].append(key)
		else:
			self.used_counts_to_keys[times_used] = [key]

		# delete outdated info
		keys = self.used_counts_to_keys[times_used - 1]
		keys.remove(key)

	def get(self, key):
		if key in self.storage:
			self._update_key_info(key)
			return self.storage[key]
		return -1
		
	def put(self, key, value):
		if self.capacity == 0:
			return
		if self.limit > 0 and key not in self.storage:
			self.limit -= 1
		elif key not in self.storage:
			# discard key
			for amount_used, keys in self.used_counts_to_keys.items():
				if keys:
					discarded_key = keys.pop(0)
					break

			del self.storage[discarded_key]
			del self.key_used[discarded_key]

		if key not in self.storage:
			self.key_used[key] = 0
			self.used_counts_to_keys[0].append(key)
		else:
			self._update_key_info(key)

		self.storage[key] = value
