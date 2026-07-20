from fastapi import HTTPException, status, Header
from book_services.app.services.user_client_service import UserClient

class RoleChecker:
    def __init__(self, allowed_role):
        self.allowed_role = allowed_role
    
    async def __call__(self,authorization:str = Header(..., alias="Authorization")):
        current_user = await UserClient.get_current_user(authorization)
        print("Current User:", current_user)
        print("Allowed Roles:", self.allowed_role)

        user_role = current_user["role"]
        if user_role in self.allowed_role:
            return True
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)