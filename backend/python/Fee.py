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

  # CRUD operations for Fee
    def add_fee(self, fee):
        query = "INSERT INTO Fee (feeID, reason, amount) VALUES (%s, %s, %s)"
        values = (fee.feeID, fee.reason, fee.amount)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_fee_by_id(self, feeID):
        query = "SELECT * FROM Fee WHERE feeID = %s"
        self.cursor.execute(query, (feeID,))
        result = self.cursor.fetchone()
        if result:
            feeID, reason, amount = result
            return Fee(feeID, reason, amount)
        else:
            return None

    def update_fee(self, fee):
        query = "UPDATE Fee SET reason=%s, amount=%s WHERE feeID=%s"
        values = (fee.reason, fee.amount, fee.feeID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_fee(self, feeID):
        query = "DELETE FROM Fee WHERE feeID = %s"
        self.cursor.execute(query, (feeID,))
        self.connection.commit()

    # CRUD operations for BillFee
    def add_bill_fee(self, bill_fee):
        query = "INSERT INTO BillFee (billID, feeID, insuranceID) VALUES (%s, %s, %s)"
        values = (bill_fee.billID, bill_fee.feeID, bill_fee.insuranceID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_bill_fee_by_ids(self, billID, feeID):
        query = "SELECT * FROM BillFee WHERE billID = %s AND feeID = %s"
        self.cursor.execute(query, (billID, feeID))
        result = self.cursor.fetchone()
        if result:
            billID, feeID, insuranceID = result
            return BillFee(billID, feeID, insuranceID)
        else:
            return None

    def update_bill_fee(self, bill_fee):
        query = "UPDATE BillFee SET insuranceID=%s WHERE billID=%s AND feeID=%s"
        values = (bill_fee.insuranceID, bill_fee.billID, bill_fee.feeID)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_bill_fee(self, billID, feeID):
        query = "DELETE FROM BillFee WHERE billID = %s AND feeID = %s"
        self.cursor.execute(query, (billID, feeID))
        self.connection.commit()
