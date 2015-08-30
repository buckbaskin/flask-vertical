import sys
sys.path[0] = '/home/buck/Github/flask-vertical'

from config.assets import merge
from config.assets import default, production, test, development

print default.exports
print production.exports
print 'dict merge: '
print merge(default.exports, production.exports)