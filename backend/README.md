# Arquitetura do Backend

## 1. Estrutura de Pastas

A estrutura de pastas no backend pode seguir o modelo típico de FastAPI ou Flask. A seguir está uma sugestão para a estrutura de pastas:

```bash
/app
    /models          # Modelos do banco de dados (ORM)
    /routes          # Roteadores de API
    /schemas         # Schemas para validação e serialização de dados
    /services        # Lógica de negócios (ex: tutoria, agendamento)
    /utils           # Funções auxiliares (ex: autenticação, geração de token)
    /database        # Configuração do banco de dados
    /auth            # Funções e endpoints relacionados à autenticação
    /...             # Demais arquivos e pastas
/config.py         # Configurações do projeto
main.py            # Arquivo principal para rodar o servidor
/...             # Demais arquivos e pastas
```

## 2. Banco de Dados e Modelos

O banco de dados será relacional (PostgreSQL) para permitir fácil relação entre usuários, tutores, sessões e avaliações. A seguir, uma descrição dos modelos que você deve implementar:

### Usuário (User)

- `id`: ID único do usuário (Primary Key).
- `email`: E-mail único do usuário.
- `password_hash`: Hash da senha.
- `role`: Tipo de usuário (student ou tutor).
- `created_at`: Data de criação da conta.

### Tutor (Tutor)

- `id`: ID do tutor (Primary Key, chave estrangeira de User).
- `specialization`: Especializações do tutor (por exemplo, “Matemática”, “Programação”).
- `price_per_hour`: Preço por hora da tutoria.
- `bio`: Descrição ou breve biografia do tutor.
- `availability`: Horários disponíveis para tutoria.

### Sessão de Tutoria (Session)

- `id`: ID da sessão (Primary Key).
- `tutor_id`: Relacionado ao tutor (Foreign Key).
- `student_id`: Relacionado ao aluno (Foreign Key).
- `scheduled_at`: Data e hora agendada para a sessão.
- `status`: Status da sessão (agendada, realizada, cancelada).
- `price`: Preço total da sessão.

### Avaliação (Review)

- `id`: ID da avaliação (Primary Key).
- `session_id`: Relacionado à sessão de tutoria (Foreign Key).
- `student_id`: Relacionado ao aluno (Foreign Key).
- `rating`: Avaliação (1-5 estrelas).
- `comment`: Comentário da avaliação.
- `created_at`: Data de criação da avaliação.

## 3. Rotas e Endpoints da API

A API será desenvolvida com base em rotas RESTful, utilizando FastAPI ou Flask. Aqui estão as principais rotas que você precisa:

### Autenticação

- `POST /auth/register`: Cadastro de usuário (aluno ou tutor).
- `POST /auth/login`: Login de usuário e geração de token JWT.
- `POST /auth/logout`: Logout do usuário.

### Usuário (Aluno/Tutor)

- `GET /user/{id}`: Recuperar informações do perfil de um usuário (aluno ou tutor).
- `PUT /user/{id}`: Atualizar informações do perfil.

### Tutoria

- `GET /tutors`: Listar todos os tutores disponíveis.
- `GET /tutors/{id}`: Detalhes de um tutor específico.
- `POST /sessions`: Agendar uma nova sessão de tutoria.
- `GET /sessions/{id}`: Detalhes de uma sessão agendada.
- `GET /sessions/user/{id}`: Listar sessões agendadas por um aluno ou tutor.

### Avaliação

- `POST /reviews`: Criar uma avaliação após a sessão.
- `GET /reviews/session/{session_id}`: Listar avaliações de uma sessão específica.
- `GET /reviews/tutor/{tutor_id}`: Listar avaliações de um tutor específico.

### Pagamento

- `POST /payment/charge`: Processar pagamento de uma sessão de tutoria via Stripe ou PayPal.

## 4. Autenticação e Autorização

- Implementação do JWT (JSON Web Token) para autenticação.
- O token deve ser gerado no login e armazenado no lado do cliente (localStorage ou cookies).
- O token será usado para autorizar rotas privadas (agendamento de tutoria, avaliação, etc.).

## 5. Lógica de Negócio

- **Cadastro e Login**: Quando o aluno ou tutor se cadastrar, o sistema deve criptografar a senha (com bcrypt ou argon2).
- **Agendamento de Sessão**: Quando o aluno agenda uma sessão, o sistema deve verificar a disponibilidade do tutor e definir um preço com base no tempo agendado.
- **Pagamento**: Após a confirmação da sessão, o pagamento será processado via integração com Stripe ou PayPal. O pagamento será confirmado antes de confirmar a sessão como "realizada".

## 6. Banco de Dados

### 6.1 Tabelas

As tabelas devem ser definidas conforme os modelos descritos no backend.

### 6.2 Relacionamentos

- **Usuário ↔ Tutor**: Um usuário pode ser um tutor. A tabela de tutores tem uma chave estrangeira para a tabela usuários.
- **Aluno ↔ Sessão**: Um aluno pode ter várias sessões de tutoria, e cada sessão tem uma chave estrangeira para o aluno e tutor.
- **Sessão ↔ Avaliação**: Uma avaliação pertence a uma sessão de tutoria, e é criada após a sessão ser realizada.


    ```bash
docker-compose --env-file ../.env up
```


```bash
$path = "./docker-compose/postgres/docker-entrypoint.sh" # enter docker path then execute in powershell
icacls $path /grant Everyone:F
```