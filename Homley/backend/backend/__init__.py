import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb
# Spoof mysqlclient version to satisfy Django checks
MySQLdb.__version__ = "2.2.7"
MySQLdb.version_info = (2, 2, 7, "final", 0)
