# Users CRUD API 👥

Proyek ini membangun **REST API** sederhana dengan [FastAPI] API ini mendukung operasi CRUD pada data user, sudah dilengkapi validasi input menggunakan **Pydantic**, serta pengujian otomatis dengan **pytest**.

---

## 📂 Struktur Folder

```
main.py                 # Entry point aplikasi
modules/
 └── items/
     ├── routes/
     │    ├── createUser.py
     │    ├── readUser.py
     │    ├── updateUser.py
     │    └── deleteUser.py
     └── schema/
          └── schemas.py   # Model Pydantic (UserCreate, UserUpdate, RoleEnum, dll.)
tests/
 └── test_Users.py        # Unit test
requirements.txt          # Daftar dependency
```

---

## ⚡ Endpoint CRUD

- **POST /users/** → Tambah user baru  
- **GET /users/{id}?role=admin** → Admin dapat melihat semua user  
- **GET /users/{id}?role=staff** → Staff hanya bisa melihat dirinya sendiri  
- **PUT /users/{id}?role=admin** → Update data user (khusus admin)  
- **DELETE /users/{id}?role=admin** → Hapus user (khusus admin)  

---

## 🛠️ Teknologi yang Dipakai
- **FastAPI** → framework web modern, cepat, dan ringan  
- **Pydantic** → validasi dan parsing data  
- **pytest** → unit testing otomatis  

---

## ▶️ Cara Menjalankan Aplikasi

1. Clone repo:
   ```bash
   git clone 

2. Buat virtual environment:
   ```bash
   python -m venv venv
   ```

3. Aktifkan environment:
   ```bash
   # Linux/MacOS
   source venv/bin/activate
   # Windows PowerShell
   venv\Scripts\activate
   # Git Bash di Windows
   source venv/Scripts/activate
   ```

4. Tambahkan `.gitignore`:
   ```
   venv/
   ```

5. Install dependency:
   ```bash
   pip install "fastapi[standard]"
   ```

6. Jalankan server:
   ```bash
   fastapi dev main.py
   ```

   Server berjalan di:  
   👉 http://127.0.0.1:8000  

7. Dokumentasi API:  
   - Swagger UI: http://127.0.0.1:8000/docs  
   - Redoc: http://127.0.0.1:8000/redoc  

---

## 🧪 Testing

Menjalankan semua unit test:
```bash
pytest -v
```

