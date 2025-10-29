# EM MAH TEE - Self-Checkout Web App

A fully interactive **self-checkout system** built using **Python** and **Streamlit**, simulating a sandwich shop ordering experience.  
Users can browse a menu, customize their sandwiches, add items to a cart, and proceed through checkout with payment validation.

---

## Features

- **Menu Display** – Browse sandwiches with names, prices, calories, and descriptions  
- **Customization** – Choose bread type, size, vegetables, condiments, and special instructions  
- **Cart Management** – Add, remove, and review items dynamically  
- **Checkout Process** – Enter customer details, choose payment method, and validate inputs  
- **Streamlit UI** – Clean, responsive interface with multi-page navigation using `st.session_state`  

---

## Technologies Used

- **Python 3.9+**
- **Streamlit** – for the interactive web interface  
- **Regular Expressions (re)** – for form validation  

---

## Project Structure

selfcheckout-app/
├── app.py # Main app – handles navigation and page setup
├── mylibrary.py # Contains menu, customization, cart, and checkout logic
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/selfcheckout-app.git
   cd selfcheckout-app

2. **Install dependencies**
   pip install -r requirements.txt

3. **Run the app**
   streamlit run app.py

4. Open the local URL in your browser
