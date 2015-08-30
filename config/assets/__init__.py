# assets
# to import: from config.assets import patterns

from config.assets import default, production, test, development

def patterns(version):
	if version == 'production':
		return merge(default.exports, production.exports)
	elif version == 'test':
		return merge(default.exports, test.exports)
	else: # default to development
		return merge(default.exports, development.exports)

def merge(dict1, dict2):
	m = dict(**dict1)
	for k, v in dict2.items():
		if k in m:
			if isinstance(v, dict):
				# print 'merge dicts from common key '+str(k)
				m_new = merge(m[k], v)
				# print 'm_new: '+str(m_new)
				m[k] = m_new
				# print 'k: '+str(k)+' m[k]: '+str(m[k])
			elif isinstance(v, list):
				print 'merge lists of common key: '+str(k)+' l1: '+str(m[k])+' l2: '+str(v)
				m[k].extend(v)
			#if isinstance(v, basestring):
			else:
				m[k] = v
		else:
			if isinstance(v, dict):
				m[k] = merge(dict(), v)
			else: # basic element, no need to recursively add dict
				m[k] = v
	# print 'merge dicts => '+str(m)
	return m
