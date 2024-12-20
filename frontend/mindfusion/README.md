1. Arquitetura do Frontend

1.1 Estrutura de Pastas

A estrutura do frontend, utilizando Next.js com TypeScript, pode seguir o modelo abaixo:

```bash
/pages
    /index.tsx         # Página inicial (landing page)
    /login.tsx         # Página de login
    /signup.tsx        # Página de cadastro
    /dashboard.tsx     # Página de dashboard do aluno ou tutor
    /tutors.tsx        # Página de listagem de tutores
    /sessions.tsx      # Página de agendamento de sessões
    /profile.tsx       # Página de perfil do aluno ou tutor
    /payment.tsx       # Página de pagamento de sessão

/components
    /Header.tsx        # Cabeçalho com links de navegação
    /TutorCard.tsx     # Componente para exibir um tutor na lista
    /SessionCard.tsx   # Componente para exibir uma sessão de tutoria
    /Rating.tsx        # Componente para mostrar avaliações e estrelas

/services
    /api.ts            # Funções de chamadas à API (usando Axios ou Fetch)
    /auth.ts           # Funções de login, logout, etc.

/contexts
    /AuthContext.tsx   # Contexto global para armazenar o usuário autenticado

/styles
    /global.css        # Estilos globais
    /tailwind.config.js # Configuração do TailwindCSS (caso utilize)
```

1.2 Telas e Funcionalidades

**Página Inicial (index.tsx):**

- Apresentação da plataforma com botões de Login e Cadastro.
- Breve descrição dos serviços oferecidos.

**Página de Login (login.tsx):**

- Formulário de login com email e senha.
- Redirecionamento para a página de dashboard após login bem-sucedido.
- Integração com a API para autenticar o usuário e gerar o JWT.

**Página de Cadastro (signup.tsx):**

- Formulário para criar uma nova conta (campo de email, senha, e tipo de usuário: aluno ou tutor).
- Validação do formulário (ex: checar se o email já está registrado).
- Envio de dados via API para criar o novo usuário.

**Página de Dashboard (dashboard.tsx):**

- Tela principal após login com links rápidos para agendamento de tutoria, perfil e sessões agendadas.
- Exibição de avaliações e sessões passadas.
- Links para visualização de tutores ou agendar nova tutoria.

**Página de Tutores (tutors.tsx):**

- Lista de tutores com filtros de pesquisa: preço, especialização, avaliação.
- Cada tutor deve ter um card exibindo sua foto, especialização e avaliações.

**Página de Sessões (sessions.tsx):**

- Interface para agendar novas sessões, selecionando o tutor, data e hora.
- Integração com a API para listar os tutores disponíveis.

**Página de Perfil (profile.tsx):**

- Perfil do aluno ou tutor com informações pessoais, área de especialização (para tutores) e lista de sessões.

**Página de Pagamento (payment.tsx):**

- Página para processamento de pagamento com Stripe ou PayPal.
- Exibição de detalhes do pagamento antes da confirmação.

1.3 Gestão de Estado Global

**AuthContext:**

- Um contexto global para gerenciar o estado de autenticação. Após login, o token JWT é armazenado no contexto e utilizado para autenticar as requisições subsequentes.

1.4 Interação com a API

**API Service:**

- Utilize Axios ou Fetch para fazer requisições à API, como login, agendamento de sessões, visualização de tutores, etc.
- Autenticação: As requisições autenticadas devem incluir o token JWT nos headers.