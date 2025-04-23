# main.py

import uvicorn
from app import app     # 从 app.py 导入 FastAPI 实例

# 让 main.py 也有一个 `app` 变量
__all__ = ("app",)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
