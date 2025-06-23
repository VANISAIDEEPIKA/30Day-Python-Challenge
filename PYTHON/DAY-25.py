from pydantic import BaseModel, EmailStr, Field, ValidationError


class UserProfile(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Full name of the user")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(..., ge=18, le=100, description="User's age (18-100 only)")

    def display(self):
        return f"👤 Name: {self.name}\n📧 Email: {self.email}\n🎂 Age: {self.age}"


# ✅ Test a valid user
try:
    user = UserProfile(name="Vani Sai Deepika", email="saideepikavani@gmail.com", age=20)
    print("✅ Valid user created!\n")
    print(user.display())

except ValidationError as e:
    print("❌ Validation Error:", e)

# ❌ Test invalid data (uncomment to see the validation in action)
# try:
#     invalid_user = UserProfile(name="A", email="not-an-email", age=120)
# except ValidationError as e:
#     print("❌ Error while creating invalid user:\n", e)
