from design_pattern.proxy.implementation import CachedTelevision


_cached_television = CachedTelevision()

# demonstrate that the television proxy caches the list of channels
for _index in range(10):
	_channel_list = _cached_television.get_list()

	# periodically clear the cache
	if (_index + 1) % 4 == 0:
		_cached_television.clear_cache()
