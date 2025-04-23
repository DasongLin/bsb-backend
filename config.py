# config.py

# 应用基本信息
APP_TITLE = "BSB Transport API"
APP_DESCRIPTION = "后端 API 为 BSB Transport 网站提供数据接口"
APP_VERSION = "1.0.0"

# CORS 配置（允许前端访问的来源）
CORS_ORIGINS = [
    "http://localhost:8080",             # Vue2 默认开发端口
    "http://127.0.0.1:8080",
    "http://localhost:5173",             # ✅ Vue3 默认开发端口
    "http://127.0.0.1:5173",
    "http://www.bsbtransport.com.au"     # 正式部署的前端地址
]
