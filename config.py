# config.py

test_db = {
	'user' : 'root',
	'password' : 'pythonbackend',
	'host' : 'python-backend-test.ceoknp6ykuev.ap-northeast-2.rds.amazonaws.com',
	'port' : 3306,
	'database' : 'python-backend-test'
}

test_config = {
	'DB_URL' : f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8",
	JWT_SECRET_KEY : ' ',
	JWT_EXP_DELTA_SECONDS : 7 * 24 * 60 * 60
}
