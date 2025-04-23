# services.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/services")
def get_services():
    print("DEBUG: 收到 Services 请求")
    return {
        "page":    "Services",
        "content": "这里展示我们的服务项目。"
    }

@router.get("/hello")
async def say_hello():
    print("DEBUG: 收到 Hello 请求")
    return {
        "msg": "你好 Vue！我是后端 FastAPI 返回的"
    }
