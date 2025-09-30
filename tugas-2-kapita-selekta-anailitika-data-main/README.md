# Users CRUD API 🚀

Project ini adalah implementasi sederhana REST API menggunakan **FastAPI** untuk manajemen data User (Create, Read, Update, Delete).  
API ini sudah dilengkapi dengan validasi input menggunakan **Pydantic** dan unit test otomatis menggunakan **pytest**.

---

## 📂 Struktur Project
├── main.py # Entry point FastAPI
├── modules/ <br>
│ └── items/ <br>
│ ├── routes/ <br>
│ │ ├── createUser.py <br>
│ │ ├── readUser.py <br>
│ │ ├── updateUser.py <br>
│ │ └── deleteUser.py <br>
│ └── schema/ <br>
│ └── schemas.py # Pydantic models (UserCreate, UserUpdate, UserResponse, RoleEnum) <br>
├── tests/ <br>
│ └── test_Users.py # Unit tests dengan pytest <br>
└── requirements.txt # (opsional, daftar dependency) <br>

---

## ⚙️ Fitur
- **Create User** → Tambah user baru (`POST /users/`)
- **Read User(s)**  
  - `GET /users/{id}?role=admin` → Admin bisa lihat semua user  
  - `GET /users/{id}?role=staff` → Staff hanya bisa lihat dirinya sendiri
- **Update User** → Hanya admin yang bisa update data user (`PUT /users/{id}?role=admin`)
- **Delete User** → Hanya admin yang bisa hapus user (`DELETE /users/{id}?role=admin`)

---

## 🛠️ Teknologi
- [FastAPI](https://fastapi.tiangolo.com/) (Backend framework)
- [Pydantic](https://docs.pydantic.dev/) (Data validation)
- [pytest](https://docs.pytest.org/) (Testing)

---

## ▶️ Cara Menjalankan

1. Clone repository:
   ```bash
   git clone https://github.com/davonnlemuel/tugas-2-kapita-selekta-anailitika-data.git
   cd tugas-2-kapita-selekta-anailitika-data
    ```
2. Buat virtual environment & install dependency:
    ```bash
    python -m venv venv
    source venv/bin/activate        # di Linux, MacOS
    venv\Scripts\activate           # di Windows Powwershell
    source .venv/Scripts/activate   # di Windows Bash
    ```
3. Cek virtual environment sudah aktif:
    ```bash
    which python        # di Linux, macOS, Windows Bash: 
    Get-Command python  # di Windows PowerShell
    ```
5.  Tambahkan file `.gitignore` di root folder, isi: `.venv/`
6. Install FastAPI: `pip install "fastapi[standard]"`
7.  Cek FastAPI sudah terinstal: `pip show fastapi`
8. Jalankan server FastAPI:
Jalankan server (development mode): `fastapi dev main.py`
• Akses server: http://127.0.0.1:8000
9. Buka dokumentasi interaktif API:
Swagger UI → http://127.0.0.1:8000/docs <br>
Redoc → http://127.0.0.1:8000/redoc

## 🧪 Testing
Untuk menjalankan unit test:
```bash
pytest -v
```
