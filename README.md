
# Django Expense Tracker API

A RESTful backend API for tracking personal income and expenses, with JWT authentication and full CRUD support.

---

## 🔧 Setup Instructions

### Backend (Django)

```bash
git clone <repo-url>
cd expense_tracker
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

#### 🔑 Superuser (optional)
```bash
python manage.py createsuperuser
```

---

### Frontend (React + Vite)

```bash
cd vite-expense-frontend
npm install
npm run dev
```

Make sure backend runs on `http://localhost:8000`.

---

## 🔐 Authentication

- JWT Token required for all API requests.
- Get token via `/api/auth/login/`
- Use in headers:
```
Authorization: Bearer <your_token>
```

---

## 🔗 API Endpoint Documentation

| Method | Endpoint                  | Description                 |
|--------|---------------------------|-----------------------------|
| POST   | `/api/auth/register/`     | Register a new user         |
| POST   | `/api/auth/login/`        | Get JWT tokens              |
| POST   | `/api/auth/refresh/`      | Refresh JWT token           |
| GET    | `/api/expenses/`          | List user's expenses (paginated) |
| POST   | `/api/expenses/`          | Add new expense             |
| GET    | `/api/expenses/{id}/`     | Get a specific record       |
| PUT    | `/api/expenses/{id}/`     | Update a record             |
| DELETE | `/api/expenses/{id}/`     | Delete a record             |

---

## 📄 Sample API Requests/Responses

### 📝 Register

**POST** `/api/auth/register/`

```json
{
  "username": "khabindra",
  "email": "khabindra@gmail.com",
  "password": "test123"
}
```

**Response:**
```json
{
  "message": "User registered successfully"
}
```

---

### 🔐 Login

**POST** `/api/auth/login/`

```json
{
  "username": "khabindra",
  "password": "test123"
}
```

**Response:**
```json
{
  "refresh": "...",
  "access": "..."
}
```

---

### ➕ Add Expense

**POST** `/api/expenses/`

Headers: `Authorization: Bearer <token>`

```json
{
  "title": "Groceries",
  "amount": 100.00,
  "transaction_type": "debit",
  "tax": 10.00,
  "tax_type": "flat"
}
```

**Response:**
```json
{
  "id": 1,
  "title": "Groceries",
  "amount": 100.00,
  "transaction_type": "debit",
  "tax": 10.00,
  "tax_type": "flat",
  "total": 110.00,
  "created_at": "2025-01-01T10:00:00Z",
  "updated_at": "2025-01-01T10:00:00Z"
}
```

---

### 📃 List Expenses (Paginated)

**GET** `/api/expenses/`

**Response:**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/expenses/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Grocery Shopping",
      "amount": 100.00,
      "transaction_type": "debit",
      "total": 110.00,
      "created_at": "2025-01-01T10:00:00Z"
    }
  ]
}
```

---

### 🔁 Refresh JWT

**POST** `/api/auth/refresh/`

```json
{
  "refresh": "<your_refresh_token>"
}
```

**Response:**
```json
{
  "access": "<new_access_token>"
}
```

---

## ✅ Success Criteria

- JWT authentication and permission control
- Users can only manage their own data
- Superusers can access all records
- Flat and percentage tax calculation works
- Paginated response and CRUD working
