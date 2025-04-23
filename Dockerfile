################ 基础镜像（已带 Python 3.12）##############
FROM python:3.12-slim

################ 工作目录 ################
WORKDIR /app

################ 复制依赖文件并安装 ################
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

################ 复制项目源码 ################
COPY . .

################ 暴露端口（给人看用，不写也行） ################
EXPOSE 8000

################ 启动 FastAPI ################
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
