from pydantic import BaseModel, EmailStr, Field
class VerifyConfirmationCode(BaseModel):
    email: EmailStr
    code: str = Field(..., min_length=6, max_length=6, description="El código debe tener 6 caracteres")
    is_registration: bool = False
