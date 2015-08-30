import os
import sys

def aggregate_server_config(d):
	for root, dirs, files in os.walk('.', topdown=True):
		for name in files:
			if len(name) > len('server-config.py') and name[-len('server-config.py'):] == 'server-config.py':
				print 'file: '+str(name)+' in '+str(root)
				sys.path.append(root)
				print 'appended root. importing name: '+str(name[:-3])
				d[name[:-3]] = __import__(name[:-3]).exports
	return d

def flatten(d):
	# for every dict in d, add k, v to d
	return d

from config import server as s

exports = dict()
exports['server'] = s.exports

exports = aggregate_server_config(exports)
exports = flatten(exports)
print 'completed imports'
print exports