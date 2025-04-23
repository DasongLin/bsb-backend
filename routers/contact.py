from fastapi import APIRouter

router = APIRouter()

@router.get("/contact")
def get_contact():
    print("DEBUG: 收到 Contact 页请求")
    return {
        "page": "Contact",
        "content": "您可以通过此页面联系到我们，留下您的咨询和反馈。"
    }
