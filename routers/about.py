from fastapi import APIRouter

router = APIRouter()

@router.get("/about")
def get_about():
    print("DEBUG: 收到 About us 页请求")
    return {
        "page": "About us",
        "content": "了解我们的公司背景、使命以及我们如何为您提供专业服务。"
    }
