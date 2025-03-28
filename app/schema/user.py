from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import Optional
from datetime import datetime

#Para manejar el inicio propi

class UserEmail(BaseModel):
    email: EmailStr 
class UserLogin(BaseModel): 
    # userid can be either email or username
    userid:  str = Field(..., min_length=3, max_length=50, description="Puede ser un email o nombre de usuario")
    password: str = Field(..., min_length=6, max_length=100, description="La contraseña debe tener al menos 6 caracteres")

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100, description="La contraseña debe tener entre 6 y 100 caracteres")

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="El nombre de usuario debe tener entre 3 y 20 caracteres")
    email: EmailStr
    profile_photo_url: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=150, description="La biografía debe tener menos de 150 caracteres")
    total_points: Optional[int] = None
    name: Optional[str] = Field(None, max_length=50, description="El nombre debe tener menos de 50 caracteres")

# UserUpdate la uso para register_screen que sirve para google login y normal login
#userUpdate no tiene email ya que esto no se actualiza
class UserUpdate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="El nombre de usuario debe tener entre 3 y 20 caracteres")
    profile_photo_url: Optional[str] = None
    bio: Optional[str] = Field(None, max_length=150, description="La biografía debe tener menos de 150 caracteres")
    total_points: Optional[int] = None
    name: str = Field(None, max_length=50, description="El nombre debe tener menos de 50 caracteres")

# Definición del esquema para la respuesta al obtener un usuario
from pydantic import BaseModel, EmailStr, Field


class UserResponse(UserBase):
    id: int
    sub: Optional[str] = None
    username: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
