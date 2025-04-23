from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 导入全局配置
from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, CORS_ORIGINS

# 导入各个路由模块
from routers import services, prices, about, contact

# 创建 FastAPI 应用实例
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

# 配置 CORS 中间件，允许前端访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,       # 引用你在 config.py 中配置的列表
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册各个子路由模块，统一添加前缀 /api
app.include_router(services.router, prefix="/api", tags=["Services"])
app.include_router(prices.router, prefix="/api", tags=["Prices"])
app.include_router(about.router, prefix="/api", tags=["About"])
app.include_router(contact.router, prefix="/api", tags=["Contact"])
