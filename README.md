# 🚀 Django Full Stack & REST API: Módulos 59-68

Este repositório é uma compilação técnica do meu progresso na trilha de **Back-End com Python**. O projeto evoluiu de uma estrutura básica de modelos Django até a implementação de uma API REST robusta, protegida e com suporte a operações assíncronas.

## 📌 Visão Geral do Projeto
O sistema simula o núcleo de um **E-commerce/Blog**, integrando a gestão de produtos, categorias, pedidos de usuários e postagens informativas. O foco principal foi a transição do Django tradicional (Templates/Views) para o **Django REST Framework (DRF)**.

---

## 🛠️ Tecnologias e Conceitos Dominados

### **Core Backend**
* **Django 5.x:** Modelagem complexa de dados e Admin Customizado.
* **Django REST Framework (DRF):** Criação de endpoints escaláveis.
* **Poetry:** Gerenciamento moderno de dependências e ambientes virtuais.
* **Async Python:** Implementação de Views Assíncronas (`async/await`) para tarefas não bloqueantes.

### **Arquitetura de API**
* **Serialização Avançada:** Uso de `ModelSerializer` e `SlugRelatedField` para otimização de JSON.
* **Autenticação & Permissões:** Proteção de rotas via `TokenAuthentication` e controle de acesso com `IsAuthenticated`.
* **Roteamento Dinâmico:** Implementação de `DefaultRouter` para padronização de URLs REST.
* **Paginação:** Configuração global de resultados para otimização de performance.

---

## 📂 Estrutura do Repositório

```text
├── setup_django/          # Configurações globais, ASGI/WSGI e Security
├── loja/                  # Aplicação principal
│   ├── models.py          # Category, Product, Post e Order
│   ├── serializers.py     # Lógica de transformação de dados (JSON)
│   ├── views.py           # ViewSets REST e Views Assíncronas
│   └── urls.py            # Endpoints da aplicação
└── manage.py              # Utilitário de linha de comando
```

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências (Poetry):**
   ```bash
   poetry install
   poetry shell
   ```

3. **Execute as migrações do Banco de Dados:**
   ```bash
   python manage.py migrate
   ```

4. **Crie um superusuário para acessar o `/admin`:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

Se você já rodou o `docker-compose up`, as migrações passaram e você conseguiu criar o superusuário, o "motor" está pronto. Agora, para fechar a entrega com chave de ouro e garantir que o professor Bruno não tenha dúvidas, faltam apenas estes **detalhes de organização no GitHub**:

---

## 🐳 Como rodar com Docker

Para subir o ambiente completo (Aplicação + Banco de Dados Postgres):

1. **Subir os containers:**
   ```bash
   docker-compose up --build
   ```

2. **Criar o Superusuário (necessário na primeira execução):**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

3. **Acessar o sistema:**
   - API: `http://localhost:8000/api/products/`
   - Admin: `http://localhost:8000/admin/`
```

### 2. Verificar o arquivo `.dockerignore`
Certifique-se de que ele existe na raiz. Isso evita que sua imagem Docker fique com 1GB de tamanho desnecessariamente. Ele deve conter:
* `__pycache__`
* `.git`
* `db.sqlite3` (já que agora usamos Postgres)
* `.venv`
* `poetry.lock` (o Docker vai usar o que está na pasta)

---

### 3. O "Grand Finale": O Pull Request (PR)
Este é o ponto mais importante, pois o professor pediu explicitamente o **link do PR**.

1.  **Faça o Push Final:**
    ```bash
    git add .
    git commit -m "docs: atualiza instruções de execução no README e finaliza docker-compose"
    git push origin feature/dockerizacao-projeto
    ```
2.  **Abra o PR no GitHub:**
    - Vá na aba **"Pull Requests"** do seu repositório.
    - Clique em **"New pull request"**.
    - Compare a sua branch (`feature/dockerizacao-projeto`) com a `main`.
    - Clique em **"Create pull request"**.
3.  **A descrição do PR:**
    No campo de texto, escreva algo direto:
    > "Entrega do desafio de Dockerização. Implementado Dockerfile multi-estágio e Docker Compose com serviços 'web' (Django/DRF) e 'db' (PostgreSQL). Projeto testado e funcional."

---

### 4. Checklist de Conferência (Auto-correção)
Antes de colar o link na plataforma da EBAC, responda a si mesmo:
* [ ] O `docker-compose.yml` tem os serviços **web** e **db**?
* [ ] O `settings.py` está pegando as credenciais do banco via `os.environ`?
* [ ] O arquivo `pyproject.toml` tem o `psycopg2-binary` nas dependências?
* [ ] O link que você vai enviar termina em `/pull/X` (onde X é um número)?

Se a resposta for **SIM** para tudo, você terminou! Pode enviar o link do PR e descansar. **Missão cumprida!** 🚀
---

## 👨‍💻 Autor
**Kaio**
*Estudante de Desenvolvimento de Software focado em Python e Backend.*
*Objetivo: Construção de arquiteturas sólidas e integração com ferramentas de IA (Cursor/FastAPI)*

---
