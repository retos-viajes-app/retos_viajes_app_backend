from pydantic import BaseModel, EmailStr, Field

class ResetPasswordRequest(BaseModel):
    new_password: str = Field(..., min_length=6, max_length=100, description="La contraseña debe tener entre 6 y 100 caracteres")