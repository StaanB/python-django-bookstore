# Usando a imagem python:3.11-slim como base
FROM python:3.11-slim

# Definindo variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Instalando dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev \
        gcc

# Criando e movendo para o diretório de trabalho
WORKDIR /app

# Copiando os arquivos de dependências do Python
COPY requirements.txt .

# Instalando as dependências do Python
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copiando o código fonte da aplicação
COPY . .

# Expondo a porta 8000
EXPOSE 8000

# Comando padrão para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
