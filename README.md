# E-commerce Product Catalog with Dynamic Pricing (ML)

---

## AI Feature -> Linear Regression ML (simple)

- `/src/redux/ML/server.py` - Flask server with linear regression ML model for dynamic prices based on rating.

---

## How to install + tools used

### 1. Clone repository

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repo>
```

### 2. Activate venv

```bash
cd src/redux/ML

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

## Blockchain integration

The use of this ML model can be benefitial with blockchain technology due to its improvement in transparency and user-centric ecommerce experiences. 

- **Token-gated pricing** -> personalized discounts, exclusive offers that improve relations with loyal customers

- **Loyalty smart contracts** -> automatic rewards with tokens based on purchases or engagement. 
