"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

Database data objects.
An object is a data object if its only purpose is to store immutable data with no functionality.
"""
from model.model import Model, PermanentModel, Searchable, QueryModel

class InsurancePolicy(PermanentModel, Searchable):
    def __init__(self, insurancePolicyID) -> None:
        Model.__init__(self, "InsurancePolicy", [
           "insurancePolicyID", "insuranceName", "insurancePolicyNumber", "copayAmount"
        ], {"insurancePolicyID": insurancePolicyID})
        self.__insurancePolicyID = insurancePolicyID

    def getInsurancePolicyID(self):
        return self.__insurancePolicyID
    
class Chart(PermanentModel):
    def __init__(self, chartID) -> None:
        Model.__init__(self, "Chart", [
           "chartID", "weight", "height", "bloodPressure", "temperature", "diagnoses", "allergies", "date", "patientAccountID"
        ], {"chartID": chartID})
        self.__chartID = chartID

    def getChartID(self):
        return self.__chartID
    
class Pharmacy(PermanentModel, Searchable):
    def __init__(self, pharmacyID) -> None:
        Model.__init__(self, "Pharmacy", [
           "pharmacyID", "name", "address", "phoneNumber"
        ], {"pharmacyID": pharmacyID})
        self.__pharmacyID = pharmacyID

    def getPharmacyID(self):
        return self.__pharmacyID
    
class Prescription(PermanentModel):
    def __init__(self, prescriptionID) -> None:
        Model.__init__(self, "Prescription", [
           "prescriptionID", "drug", "dosage", "frequency", "date", "pharmacyID", "patientAccountID"
        ], {"prescriptionID": prescriptionID})
        self.__prescriptionID = prescriptionID

    def getPrescriptionID(self):
        return self.__prescriptionID
    
class Laboratory(PermanentModel, Searchable):
    def __init__(self, labID) -> None:
        Model.__init__(self, "Laboratory", [
           "labID", "name", "address", "phoneNumber"
        ], {"labID": labID})
        self.__labID = labID

    def getLabID(self):
        return self.__labID
