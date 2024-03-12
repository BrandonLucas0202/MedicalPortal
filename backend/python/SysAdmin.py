import mysql.connector

class PatientAccountDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

# CRUD operations for SysAdmin
    def add_sys_admin(self, sys_admin):
        query = "INSERT INTO SysAdmin (sysAdminID, staffAccountID) VALUES (%s, %s)"
        values = (sys_admin.sysAdminID, sys_admin.staffAccountID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_sys_admin_by_id(self, sysAdminID):
        query = "SELECT * FROM SysAdmin WHERE sysAdminID = %s"
        self.cursor.execute(query, (sysAdminID,))
        result = self.cursor.fetchone()
        if result:
            sysAdminID, staffAccountID = result
            return SysAdmin(sysAdminID, staffAccountID)
        else:
            return None

    def update_sys_admin(self, sys_admin):
        query = "UPDATE SysAdmin SET staffAccountID = %s WHERE sysAdminID = %s"
        values = (sys_admin.staffAccountID, sys_admin.sysAdminID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_sys_admin(self, sysAdminID):
        query = "DELETE FROM SysAdmin WHERE sysAdminID = %s"
        self.cursor.execute(query, (sysAdminID,))
        self.connection.commit()
