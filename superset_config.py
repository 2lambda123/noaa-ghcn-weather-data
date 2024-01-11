import os

from superset_config import *

# Database configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:////path/to/database.db')

# Authentication configuration
AUTH_TYPE = os.environ.get('AUTH_TYPE', 'ldap')
AUTH_LDAP_SERVER = os.environ.get('LDAP_SERVER', 'ldap://localhost:389')
AUTH_LDAP_BIND_USER = os.environ.get('LDAP_BIND_USER', 'cn=admin,dc=example,dc=com')
AUTH_LDAP_BIND_PASSWORD = os.environ.get('LDAP_BIND_PASSWORD', 'password')
AUTH_LDAP_SEARCH_BASE = os.environ.get('LDAP_SEARCH_BASE', 'ou=users,dc=example,dc=com')

# Feature flags
ENABLE_FEATURE_A = os.environ.get('ENABLE_FEATURE_A', 'False') == 'True'
ENABLE_FEATURE_B = os.environ.get('ENABLE_FEATURE_B', 'False') == 'True'
ENABLE_FEATURE_C = os.environ.get('ENABLE_FEATURE_C', 'False') == 'True'
