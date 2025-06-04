# 🦇 Sistema de Gerenciamento Wayne Industries

Sistema full-stack para gerenciamento de segurança e recursos das Indústrias Wayne, desenvolvido como projeto final para portfólio.

---

## 📌 Visão Geral

Aplicação completa utilizando **Python + Django** no backend e **React + Vite + Material-UI** no frontend. Permite gerenciamento de usuários, autenticação via JWT e controle de recursos de forma segura e moderna.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** React + Vite + Material-UI  
- **Backend:** Django REST Framework  
- **Banco de Dados:** SQLite (compatível com PostgreSQL)  
- **Autenticação:** JWT (JSON Web Tokens)  

---

## 🚀 Configuração do Projeto

### ✅ Pré-requisitos

- Python 3.10+
- Node.js 16+
- Git

### 📦 Instalação

#### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/wayne-industries.git
cd wayne-industries


cd backend
python -m venv venv
venv\Scripts\activate  # Para Windows
# source venv/bin/activate  # Para Linux/Mac

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


cd ../frontend
npm install
npm run dev



wayne-industries/
├── backend/
│   ├── app/
│   │   ├── models.py         # Modelos: User e Resource
│   │   ├── serializers.py    # Serializers DRF
│   │   └── views.py          # API Views
│   └── core/                 # Configurações do Django
├── frontend/
│   ├── src/
│   │   ├── pages/            # Páginas React
│   │   └── App.jsx           # Roteamento principal
└── README.md


🔐 Rotas da API (Backend)
| Endpoint          | Método | Descrição                    |
| ----------------- | ------ | ---------------------------- |
| `/api/login/`     | POST   | Autenticação de usuários     |
| `/api/users/`     | GET    | Listagem de usuários (admin) |
| `/api/resources/` | GET    | Listar todos os recursos     |


