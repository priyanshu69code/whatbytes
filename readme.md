# Django Healthcare Backend

A robust backend system for a healthcare application built with Django, Django REST Framework (DRF), PostgreSQL, and JWT authentication. This system allows secure management of users, patients, doctors, and their associations.

---

## **Table of Contents**

- Project Overview
- Features
- Tech Stack
- Getting Started
    - Prerequisites
    - Clone the Repository
    - Running with Docker Compose
- API Endpoints
    - Authentication
    - Patient Management
    - Doctor Management
    - Patient-Doctor Mapping
- Environment Variables
- Testing the APIs
- License

---

## **Project Overview**

This backend provides RESTful APIs for:

- User registration and login with JWT authentication.
- Managing patient and doctor records.
- Assigning doctors to patients.
- Secure access and validation.

---

## **Features**

- **JWT Authentication** for secure user access.
- **CRUD operations** for patients and doctors.
- **Patient-Doctor mapping** APIs.
- **PostgreSQL** for data storage.
- **Dockerized** for easy setup and deployment.
- **Environment variable** support for sensitive configs.

---

## **Tech Stack**

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL(Docker Image)
- djangorestframework-simplejwt
- Docker \& Docker Compose

---

## **Getting Started**

### **Prerequisites**

- Docker \& Docker Compose installed on your system.


### **Clone the Repository**

```bash
git clone &lt;your-repo-url&gt;
cd whatbytes;
```


### **Running with Docker Compose**

Build and start the project using Docker Compose:

```bash
docker compose -f docker-compose.yml build
docker compose -f docker-compose.yml up
```

The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **API Endpoints**

All endpoints are prefixed with `/api/`.

---

### **1. Authentication APIs**

| Endpoint | Method | Description | Body Params | Auth Required |
| :-- | :-- | :-- | :-- | :-- |
| `/api/auth/register/` | POST | Register a new user | `name`, `email`, `password` | No |
| `/api/auth/login/` | POST | Login and get JWT token | `email`, `password` | No |

**Example Request (Register):**

```json
POST /api/auth/register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "yourpassword"
}
```

**Example Request (Login):**

```json
POST /api/auth/login/
{
  "email": "john@example.com",
  "password": "yourpassword"
}
```


---

### **2. Patient Management APIs**

| Endpoint | Method | Description | Body Params | Auth Required |
| :-- | :-- | :-- | :-- | :-- |
| `/api/patients/` | POST | Add a new patient | `name`, `age`, `gender`, `address`, `phone` | Yes |
| `/api/patients/` | GET | List all patients (of user) | - | Yes |
| `/api/patients/&lt;id&gt;/` | GET | Get details of a specific patient | - | Yes |
| `/api/patients/&lt;id&gt;/` | PUT | Update patient details | Any patient fields | Yes |
| `/api/patients/&lt;id&gt;/` | DELETE | Delete a patient | - | Yes |

**Example Request (Add Patient):**

```json
POST /api/patients/
{
  "name": "Nikhil Raj",
  "age": 21,
  "gender": "M",
  "address": "Vaishali, Bihar",
  "phone": "5479766951"
}
```


---

### **3. Doctor Management APIs**

| Endpoint | Method | Description | Body Params | Auth Required |
| :-- | :-- | :-- | :-- | :-- |
| `/api/doctors/` | POST | Add a new doctor | `name`, `specialization`, `email`, `phone_number` | Yes |
| `/api/doctors/` | GET | List all doctors | - | Yes |
| `/api/doctors/&lt;id&gt;/` | GET | Get details of a specific doctor | - | Yes |
| `/api/doctors/&lt;id&gt;/` | PUT | Update doctor details | Any doctor fields | Yes |
| `/api/doctors/&lt;id&gt;/` | DELETE | Delete a doctor | - | Yes |

**Example Request (Add Doctor):**

```json
POST /api/doctors/
{
  "name": "Dr. Smith",
  "specialization": "Cardiology",
  "email": "drsmith@example.com",
  "phone_number": "1234567890"
}
```


---

### **4. Patient-Doctor Mapping APIs**

| Endpoint | Method | Description | Body Params | Auth Required |
| :-- | :-- | :-- | :-- | :-- |
| `/api/mappings/` | POST | Assign a doctor to a patient | `patient`, `doctor` | Yes |
| `/api/mappings/` | GET | List all patient-doctor mappings | - | Yes |
| `/api/mappings/&lt;patient_id&gt;/` | GET | List all doctors assigned to a patient | - | Yes |
| `/api/mappings/&lt;id&gt;/` | DELETE | Remove a doctor from a patient | - | Yes |

**Example Request (Assign Doctor):**

```json
POST /api/mappings/
{
  "patient": 6,
  "doctor": 7
}
```


---

## **Environment Variables**

Sensitive settings (e.g., database credentials, secret keys) should be managed via environment variables. See `.env.example` for reference.

---

## **Testing the APIs**

You can test all endpoints using [Postman](https://www.postman.com/) or any API client. Sample Postman collections for User, Patient, Doctor, and Mapping APIs are available in the `postman_collections/` directory.

---

## **License**

This project is licensed under the MIT License.

---

**Happy coding! 🚀**

<div style="text-align: center">Priyanshu Kumar</div>
