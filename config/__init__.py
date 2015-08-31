import os
import sys

def aggregate_server_config(d):
	for root, dirs, files in os.walk('.', topdown=True):
		for name in files:
			trail= len('-server-config.py')
			if len(name) > trail and name[-trail:] == '-server-config.py':
				# print 'file: '+str(name)+' in '+str(root)
				sys.path.append(root)
				# print 'appended root. importing name: '+str(name[:-trail])
				d[name[:-trail]] = __import__(name[:-3]).exports
	return d

def flatten(d):
	# flatten everything one level
	for key, value in d.items():
		if isinstance(value, dict):
			for k, v in value.items():
				d[k] = v

	return d

from config import server as s

exports = dict()
exports['server'] = s.exports

exports = aggregate_server_config(exports)
# exports = flatten(exports)
# print 'completed imports'
print exports