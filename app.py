"""
FastAPI 入口
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --------------------------------------------------
# 基本信息 & CORS 列表
# --------------------------------------------------
from config import (
    APP_TITLE, APP_DESCRIPTION, APP_VERSION,
    CORS_ORIGINS,
)

# --------------------------------------------------
# 创建 FastAPI 实例
# --------------------------------------------------
app = FastAPI(
    title       = APP_TITLE,
    description = APP_DESCRIPTION,
    version     = APP_VERSION,
)

# --------------------------------------------------
# CORS 中间件
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins     = CORS_ORIGINS,
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)

# --------------------------------------------------
# 挂载各子路由
# --------------------------------------------------
from routers import services, prices, about, contact

app.include_router(services.router, prefix="/api", tags=["Services"])
app.include_router(prices.router,   prefix="/api", tags=["Prices"])
app.include_router(about.router,    prefix="/api", tags=["About"])
app.include_router(contact.router,  prefix="/api", tags=["Contact"])

# --------------------------------------------------
# 本地 / Fly.io 容器启动入口
# --------------------------------------------------
if __name__ == "__main__":
    # Fly.io 会注入 PORT 环境变量（例如 8080）
    import os, uvicorn

    uvicorn.run(
        "app:app",                # 模块名:实例名
        host="0.0.0.0",           # 必须 0.0.0.0 才能被容器外访问
        port=int(os.getenv("PORT", 8000)),
        reload=False,             # 生产环境关闭热重载
    )
