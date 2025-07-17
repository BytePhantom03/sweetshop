# 🍬 Sweet Shop Management System

A robust and scalable application designed for managing inventory and operations in a sweet shop. Built using Test-Driven Development (TDD) principles to ensure code quality, maintainability, and reliability.

![CI](https://img.shields.io/badge/build-passing-brightgreen)

---
## 📁 Project Structure

```bash
sweetshop/
│
├── sweetshop/
│   ├── manager/
│   │   └── sweet_manager.py     # Core business logic
│   ├── models/
│   │   └── sweet.py             # Sweet class
│
├── tests/                       # Unit tests
│   ├── test_add.py
│   ├── test_delete.py
│   ├── ...
├── validators/                       # Unit tests
│   ├── sweet_validator.py
│
├── run_tests.py                 # Test runner
├── README.md                    # This file
└── requirements.txt             # Dependencies
```


---

## 🧩 Key Features

- Add, update, delete sweets with validation and error handling.
- Manage inventory: track quantity, restock, and purchase operations.
- Advanced search with partial match, case insensitivity, and filters.
- Comprehensive test suite covering edge cases and negative scenarios.

---

## 📦 How It Works

> Here's how the system flows under the hood:

1. **SweetManager** handles all operations like add, update, delete, search, purchase, and restock.
2. All inputs are validated to prevent inconsistent or invalid data entries.
3. Edge cases (e.g., duplicate IDs, negative quantity) are managed gracefully.
4. Every logic path is tested with `unittest` for accuracy and coverage.

---

## 🚀 Demo Use Case

Let’s say you want to:
- Add a new sweet: `"Kaju Katli"` → It goes through validations, is stored in memory (or DB), and is now trackable.
- Purchase 5 units → The quantity gets reduced, with checks for out-of-stock conditions.
- Search "kaju" → Partial and case-insensitive match returns the sweet.
- Update price or category later? ✅ Easily done with `update_sweet()` logic.

---

## 🧪 Test Coverage

The project uses **unit testing** extensively:
- ✅ Add/Update/Delete tests
- ✅ Invalid ID formats and negative values
- ✅ Purchase beyond stock
- ✅ Restock behavior
- ✅ Search logic (case/partial/full match)

> Run all tests:
```bash
python run_tests.py
      OR
python -m unittest discover
```

---

## 📌 Why This Project?

This project is designed to reflect:
- 📚 Test-Driven Development in action
- 🧼 Clean Code and modular design
- ✅ Real-world edge case handling
- 🔍 Full CRUD + search workflow

---

## 🛠️ Future Improvements

- Add frontend interface using React.js for better user experience
- Database persistence (e.g.,MySql, SQLite, PostgreSQL)
- User authentication (admin/customer roles)
- Export reports or inventory summaries
- Deploy on cloud for demo access

---

## 🙌 Author

**Ravi Zapadiya**  
_“Turning sweetshop into scalable software.”_
