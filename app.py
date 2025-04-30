from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ————————————————————————————
# ① 全局配置
# ————————————————————————————
APP_TITLE       = "BSB Transport API"
APP_DESCRIPTION = "后端 API 为 BSB Transport 网站提供数据接口"
APP_VERSION     = "1.0.0"

# 把你的正式/测试前端域名写在这里；开发阶段也可以用 ["*"] 全放开
CORS_ORIGINS = [
    "https://bsb-frontend.vercel.app",  # Vercel 生产域名
    "http://localhost:5173",            # 本地前端调试端口（可按需保留）
]

# 如果你已经在 config.py 里维护了同名变量，保留一份即可
# from config import APP_TITLE, APP_DESCRIPTION, APP_VERSION, CORS_ORIGINS
# ---------------------------------------------------------------


# ————————————————————————————
# ② 导入各个子路由
# ————————————————————————————
from routers import services, prices, about, contact


# ————————————————————————————
# ③ 创建 FastAPI 应用实例
# ————————————————————————————
app = FastAPI(
    title       = APP_TITLE,
    description = APP_DESCRIPTION,
    version     = APP_VERSION,
)


# ————————————————————————————
# ④ 配置 CORS 中间件
# ————————————————————————————
app.add_middleware(
    CORSMiddleware,
    allow_origins     = CORS_ORIGINS,   # ← 关键：允许来自这些域的跨域请求
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],
)


# ————————————————————————————
# ⑤ 注册子路由（统一前缀 /api）
# ————————————————————————————
app.include_router(services.router, prefix="/api", tags=["Services"])
app.include_router(prices.router,   prefix="/api", tags=["Prices"])
app.include_router(about.router,    prefix="/api", tags=["About"])
app.include_router(contact.router,  prefix="/api", tags=["Contact"])
