# Products API

![CI Status](https://github.com/dzackyahmad/homework-prakt-ppl1/actions/workflows/ci.yml/badge.svg?branch=develop)

## 1. Deskripsi Project

Products API adalah RESTful API sederhana yang digunakan untuk melakukan manajemen data produk. API ini menyediakan operasi CRUD (Create, Read, Update, Delete) dan mengembalikan response dalam format JSON standar.

---

## 2. Dokumentasi API

### Endpoint List

* GET /products → mengambil semua data produk
* GET /products/{id} → mengambil produk berdasarkan id
* POST /products → menambahkan produk baru
* PUT /products/{id} → mengupdate produk
* DELETE /products/{id} → menghapus produk

---

### Contoh CRUD 🔧

#### Create (POST /products)

```bash
curl -X POST http://127.0.0.1:5000/products \
-H "Content-Type: application/json" \
-d '{"name": "Laptop", "price": 1000}'
```

#### Read All (GET /products)

```bash
curl http://127.0.0.1:5000/products
```

#### Read by ID (GET /products/{id})

```bash
curl http://127.0.0.1:5000/products/1
```

#### Update (PUT /products/{id})

```bash
curl -X PUT http://127.0.0.1:5000/products/1 \
-H "Content-Type: application/json" \
-d '{"name": "Laptop Gaming", "price": 1500}'
```

#### Delete (DELETE /products/{id})

```bash
curl -X DELETE http://127.0.0.1:5000/products/1
```

---

### Mapping CRUD → Endpoint 📊

| Operasi    | Method | Endpoint       |
| ---------- | ------ | -------------- |
| Create     | POST   | /products      |
| Read All   | GET    | /products      |
| Read by ID | GET    | /products/{id} |
| Update     | PUT    | /products/{id} |
| Delete     | DELETE | /products/{id} |

---

### Flow Request → Response 🔄

1. Client mengirim HTTP request (GET/POST/PUT/DELETE)
2. Request diterima oleh endpoint `/products`
3. Server memproses data (create/read/update/delete)
4. Server mengembalikan response JSON
5. Client menerima hasil (success/error)

Contoh alur:

```
Client → Request → API → Process → JSON Response → Client
```

---

### Format Response

#### Success Response ✅

```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Laptop",
    "price": 1000
  }
}
```

#### Error Response ❌

```json
{
  "status": "error",
  "message": "Product not found"
}
```

---

### Format Response

#### Success Response

```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Laptop",
    "price": 1000
  }
}
```

#### Error Response

```json
{
  "status": "error",
  "message": "Product not found"
}
```

---

## 3. Panduan Instalasi (Docker)

### Menjalankan aplikasi

```bash
docker-compose up --build
```

### Informasi Port

* Host Port: 5000
* Container Port: 5000

Akses API di:
[http://127.0.0.1:5000/products](http://127.0.0.1:5000/products)

---

## 4. Alur Kerja Git

### Branch yang digunakan

* main → production
* develop → integration
* feature/* → pengembangan fitur

### Workflow

1. Membuat branch dari develop
2. Mengembangkan fitur
3. Commit menggunakan Conventional Commits
4. Merge ke develop
5. Jika stabil → merge ke main

### Contoh Conventional Commit

* feat: implement CRUD products API
* fix: correct API response format
* docs: update README

---

## 5. Status Automasi (GitHub Actions)

### Workflow

Pipeline berjalan otomatis saat:

* push
* pull request

### CI (Continuous Integration)

Menjalankan testing sederhana untuk memastikan pipeline berjalan.

### CS (Code Security)

Menggunakan Gitleaks untuk mendeteksi potensi kebocoran secret.

### Status

Workflow berhasil dijalankan dan berada dalam status SUCCESS di tab GitHub Actions.

---

## Checklist Pemenuhan Tugas

| Kriteria                 | Status |
| ------------------------ | ------ |
| CRUD API                 | ✔      |
| RESTful Endpoint         | ✔      |
| JSON Response            | ✔      |
| Feature Branch Flow      | ✔      |
| Conventional Commits     | ✔      |
| Dockerfile               | ✔      |
| docker-compose           | ✔      |
| CI Pipeline              | ✔      |
| Security Scan (Gitleaks) | ✔      |
| Dokumentasi Lengkap      | ✔      |

---

## Kesimpulan

Project ini telah memenuhi seluruh checklist minimal pada tugas Praktikum Perangkat Lunak I, termasuk implementasi API, containerization dengan Docker, workflow Git yang benar, serta automasi menggunakan GitHub Actions.
