from fastapi import APIRouter

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"]
)

@router.get("/")
def get_complaints():
    return {
        "message": "Complaint API is working"
    }