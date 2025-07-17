# Sweet Shop Management System

A simple web application to manage a sweet shop’s inventory and sales.
You can add, view, search, sort, purchase, and restock sweets using a user-friendly web interface.

---

## Description

This project is designed to help sweet shop owners easily manage their inventory and sales.
It allows you to keep track of all sweets in the shop, update their details, search and sort through the list, handle purchases (with stock checks), and restock items as needed.
The system is easy to use, works in your browser, and is backed by a robust Python backend.

---

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript (vanilla)
* **Backend:** Python, Flask
* **Testing:** pytest (for backend logic)
* **Other:** CORS enabled for frontend-backend communication

---

## Features

* **Add Sweets:** Add new sweets with a unique ID, name, category, price, and quantity.
* **Delete Sweets:** Remove sweets from the shop.
* **View Sweets:** See all available sweets in a table.
* **Search Sweets:** Find sweets by name, category, or price range.
* **Sort Sweets:** Sort sweets by name, category, price, or quantity.
* **Purchase Sweets:** Buy sweets (stock decreases, error if not enough in stock).
* **Restock Sweets:** Increase the quantity of any sweet.
* **Modern Web Interface:** Clean, responsive, and easy to use.
* **Tested Backend:** All backend logic is covered by automated tests.

---

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/mahivram/Sweet-Shop-Management-System
cd Sweet-Shop-Management-System
```

### 2. Set up your Python environment

It’s recommended to use a virtual environment:

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the backend server

```sh
python -m sweetshop.api
```

The backend will start at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 5. Open the frontend

Open `frontend/index.html` in your browser.

---

## How to Use

* **Add a sweet:** Fill in the form and click "Add Sweet".
* **View sweets:** All sweets are listed in the table.
* **Search:** Use the search fields to filter by name, category, or price.
* **Sort:** Use the dropdown to sort by name, category, price, or quantity.
* **Purchase:** Click "Purchase" next to a sweet and enter the quantity.
* **Restock:** Click "Restock" and enter the quantity to add.
* **Delete:** Click "Delete" to remove a sweet from the shop.

---

## Running Tests

To run all backend tests:

```sh
python -m pytest
```

All core features are covered by tests in `tests/test_shop.py`.

---

## API Endpoints (for reference)

* `GET /sweets` — List all sweets
* `POST /sweets` — Add a new sweet
* `DELETE /sweets/<id>` — Delete a sweet
* `GET /sweets/search` — Search sweets
* `GET /sweets/sort` — Sort sweets
* `POST /sweets/<id>/purchase` — Purchase a sweet
* `POST /sweets/<id>/restock` — Restock a sweet

All endpoints return JSON.

---

## Notes

* Make sure the backend is running before using the frontend.
* If you see CORS errors, check that the backend is running and CORS headers are set (see `api.py`).
* All data is stored in memory (no database), so data will reset when the server restarts.

---

## License

This project is open source and free to use.

---

## Author

- Mahiv Ram
