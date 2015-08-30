# non-sensitive configuration for server

import os

basedir = os.path.abspath(os.path.dirname(__file__))

from config import secret

exports = dict()
exports['DEBUG'] = True
exports['PORT'] = 5000
exports['HOST'] = '0.0.0.0'

exports['WTF_CSRF_ENABLED'] = True
exports['SECRET_KEY'] = secret.exports['SECRET_KEY']
exports['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
exports['SQLALCHEMY_MIGRATE_REPO'] = os.path.join(basedir, 'db_repository')
