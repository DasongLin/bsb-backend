"""
应用基本信息 & CORS 配置
"""

APP_TITLE       = "BSB Transport API"
APP_DESCRIPTION = "后端 API 为 BSB Transport 网站提供数据接口"
APP_VERSION     = "1.0.0"

# 允许前端访问的域（⚠ 不要带 / 结尾）
CORS_ORIGINS = [
    "https://bsb-frontend.vercel.app",     # 生产域名
    "https://*.bsb-frontend.vercel.app",   # Vercel Preview Deploy（带随机前缀）
    "http://localhost:5173",               # 本地 Vue3 dev server
    "http://127.0.0.1:5173",
]
