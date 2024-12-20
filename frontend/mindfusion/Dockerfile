# Use uma imagem base do Node.js
FROM node:20-alpine

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de pacotes e instale as dependências
COPY package.json .
COPY package-lock.json .
RUN npm install

# Copie o restante do código da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["npm", "run", "dev"]