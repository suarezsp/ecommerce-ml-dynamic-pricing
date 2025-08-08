# E-commerce Product Catalog with Dynamic Pricing (ML)

---

## Machine Learning route

- `/src/redux/ML/server.py` - Flask server with linear regression ML model for dynamic prices based on rating.

---

## How to install

### 1. Clone repository

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repo>
```

### 2. Activate venv

```bash
cd backend

python -m venv venv

#linux, macos
source venv/bin/activate

#windows cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask flask-cors scikit-learn pandas requests
```

### 4. Execute backend

```bash
python server.py
```

### 5. Execute frontend

```bash
cd ..

npm install react-material-ui-carousel --save --legacy-peer-deps

npm start 
```