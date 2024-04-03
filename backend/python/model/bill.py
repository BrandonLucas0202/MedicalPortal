"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database Bill object and Payment object.
"""
from model.model import Model, PermanentModel, QueryModel

class Bill(PermanentModel):
    def __init__(self, billID) -> None:
        Model.__init__(self, "Bill", [
           "billID", "description", "amount", "dateIssued", "dueDate", "patientAccountID"
        ], {"billID": billID})
        self.__billID = billID

    def getBillID(self):
        return self.__billID
        
class BillWithPayments(QueryModel):
    def __init__(self, billID) -> None:
        Model.__init__(self, "Bill INNER JOIN (SELECT billID, IFNULL(SUM(amount), 0.0) AS totalPaid FROM Payment GROUP BY billID) Totals ON Bill.billID = Totals.billID", [
           "billID", "description", "amount", "dateIssued", "dueDate", "patientAccountID", "totalPaid"
        ], {"billID": billID})
        self.__billID = billID

    def getBillID(self):
        return self.__billID
    
class Payment(PermanentModel):
    def __init__(self, paymentID) -> None:
        Model.__init__(self, "Payment", [
           "paymentID", "billID", "amount", "date"
        ], {"paymentID": paymentID})
        self.__paymentID = paymentID

    def getPaymentID(self):
        return self.__paymentID
        