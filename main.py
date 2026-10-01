from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Inisialisasi aplikasi FastAPI
app = FastAPI(title="Tugas 1 Integrasi Sistem - API Mahasiswa")

# 1. Model Data (Sesuai instruksi: Nama, Alamat, IPK, Semester, Hobi)
class Mahasiswa(BaseModel):
    nama: str
    alamat: str
    ipk: float
    semester: int
    hobi: str

# 2. Simulasi Database (Menggunakan dictionary seperti contoh main.py)
# Key = ID Mahasiswa (misal NPM), Value = Data Mahasiswa
mahasiswa_db = {}

# 3. ROOT Endpoint
@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Tugas 1 Integrasi Sistem"}

# 4. CREATE (POST) - Menambahkan data mahasiswa baru
@app.post("/mahasiswa/{mahasiswa_id}")
async def create_mahasiswa(mahasiswa_id: int, data: Mahasiswa):
    if mahasiswa_id in mahasiswa_db:
        raise HTTPException(status_code=400, detail="Mahasiswa dengan ID tersebut sudah ada")
    
    mahasiswa_db[mahasiswa_id] = data.dict()
    return {
        "message": "Data mahasiswa berhasil ditambahkan",
        "data": mahasiswa_db[mahasiswa_id]
    }

# 5. READ (GET) - Mendapatkan data mahasiswa berdasarkan ID
@app.get("/mahasiswa/{mahasiswa_id}")
async def read_mahasiswa(mahasiswa_id: int):
    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    
    return {
        "mahasiswa_id": mahasiswa_id,
        "data": mahasiswa_db[mahasiswa_id]
    }

# Opsional: GET semua data (Berguna untuk presentasi)
@app.get("/mahasiswa")
async def read_all_mahasiswa():
    return {"total_data": len(mahasiswa_db), "data": mahasiswa_db}

# 6. UPDATE (PUT) - Mengubah data mahasiswa berdasarkan ID
@app.put("/mahasiswa/{mahasiswa_id}")
async def update_mahasiswa(mahasiswa_id: int, data: Mahasiswa):
    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    
    mahasiswa_db[mahasiswa_id] = data.dict()
    return {
        "message": "Data mahasiswa berhasil diupdate",
        "data": mahasiswa_db[mahasiswa_id]
    }

# 7. DELETE - Menghapus data mahasiswa berdasarkan ID
@app.delete("/mahasiswa/{mahasiswa_id}")
async def delete_mahasiswa(mahasiswa_id: int):
    if mahasiswa_id not in mahasiswa_db:
        raise HTTPException(status_code=404, detail="Data mahasiswa tidak ditemukan")
    
    deleted_data = mahasiswa_db.pop(mahasiswa_id)
    return {
        "message": "Data mahasiswa berhasil dihapus",
        "deleted_data": deleted_data
    }