from model import User
from extensions import db

class DatabaseService:
    
    def GetAllUsers(self) -> list:
        return list()

    def DeleteUser(self) -> int:
        return 0
    
    def UpdateUser(self) -> int:
        return 0
    
    def AddNewUser(self) -> int:
        return 0
    
    def HashPassword(self):
        pass

    def UnhashPassword(self):
        pass

    def CreateNewUser(self):
        hashed_password = self.HashPassword()