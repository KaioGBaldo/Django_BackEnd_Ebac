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

---

## 👨‍💻 Autor
**Kaio**
*Estudante de Desenvolvimento de Software focado em Python e Backend.*
*Objetivo: Construção de arquiteturas sólidas e integração com ferramentas de IA (Cursor/FastAPI).*

---
