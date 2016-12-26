import MySQLdb

class DB(object):

    def __init__(self):

    	if not hasattr(DB, 'db_user_name'):
    		raise Exception("db_user_name not provided")

    	if not hasattr(DB, 'db_user_pass'):
    		raise Exception("db_user_pass not provided")

    	if not hasattr(DB, 'db_host'):
    		raise Exception("db_host not provided")

    	if not hasattr(DB, 'db_table'):
    		raise Exception("db_table not provided")

        self.db = MySQLdb.connect(DB.db_host, DB.db_user_name, DB.db_user_pass, DB.db_table)

    @staticmethod
    def instance():
        if not hasattr(DB, 'db_instance'):
            DB.db_intance = DB()

        return DB.db_intance.db;

    @staticmethod
    def cursor():
        return DB.instance().cursor();

    @staticmethod
    def cursor_dictonary():
        return DB.instance().cursor(MySQLdb.cursors.DictCursor);

    @staticmethod
    def lastid():
        return DB.instance().lastrowid;

    @staticmethod
    def run(str, use_normal_cursor=False):
        crs = DB.cursor() if use_normal_cursor else DB.cursor_dictonary()
        crs.execute(str)
        return crs

    @staticmethod
    def close():
        DB.instance().close();
        del DB.db_intance


DB.db_host="localhost"
DB.db_user_name="user"
DB.db_user_pass="pass"
DB.db_table="test"


print DB.run("show tables;").fetchall();

DB.close();
