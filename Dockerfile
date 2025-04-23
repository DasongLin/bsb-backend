# ----- 1. 选择基础镜像（已带 Python 3.12） -----
    FROM python:3.12-slim

    # ----- 2. 工作目录 -----
    WORKDIR /app
    
    # ----- 3. 安装依赖 -----
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # ----- 4. 复制项目源码 -----
    COPY . .
    
    # ----- 5. 启动 FastAPI -----
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
    