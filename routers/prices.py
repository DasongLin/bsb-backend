from fastapi import APIRouter

router = APIRouter()

@router.get("/prices")
def get_prices():
    print("DEBUG: 收到 Transparent prices 页请求")
    return {
        "page": "Transparent prices",
        "content": "在此页面显示我们透明公开的定价信息，让您清楚了解费用构成123啊。"
    }
