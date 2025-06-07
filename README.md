# 📱 Indian Mobile Market Analysis Dashboard

This project is an interactive Streamlit dashboard that analyzes mobile phone listings from Flipkart in the Indian market. It helps visualize trends in pricing, brands, specifications, and user ratings.

---

## 📊 Features

- **Price Segment Analysis**: Low range, mid range, and premium mobile segments.
- **Brand Insights**: Brands with the most product offerings.
- **Segment Coverage**: Brands catering to all segments.
- **Common Specifications**: RAM, Storage, Ratings distribution.
- **Interactive Filters**: Filter data by brand.
- **Visualizations**: Built using Plotly, Seaborn, and Matplotlib.

---

## 🚀 How to Run the App Locally

### 1. Clone the repository

```bash
git clone https://github.com/RutujaSankhe/mobile-dashboard-app.git
cd mobile-dashboard-app
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run mobile_dashboard.py
```

---

## 🌐 Deploy on Streamlit Cloud

You can deploy this app online for free using [Streamlit Cloud](https://streamlit.io/cloud).

### Steps:

1. Push this project to your GitHub (already done).
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and log in with GitHub.
3. Click **“New App”**, select your repo and `mobile_dashboard.py` as the entry point.
4. Click **Deploy** — done!

---

## 📁 Files Included

* `mobile_dashboard.py`: Main Streamlit application
* `Flipkart_Mobiles.csv`: Mobile data scraped from Flipkart
* `requirements.txt`: List of required Python packages

---

## 🧠 Insights from the Data

### 1. What are the different price range segments for mobiles in India?

* **Low Range**: Below ₹10,000
* **Mid Range**: ₹10,000 to ₹20,000
* **Premium Range**: Above ₹20,000

These segments reflect affordability, performance, and features.

---

### 2. Which brand provides the most product offerings for the Indian Market?

* 📈 **Xiaomi**, **Samsung**, and **Realme** are the top contributors in terms of number of products available.

---

### 3. Which brand caters to all different segments?

* ✅ **Samsung**, **Realme**, and **Motorola** have products in **all three price segments** (low, mid, premium), showing their broad market coverage.

---

### 4. What specifications are the most common that are offered by various brands?

* **RAM**: 4 GB and 6 GB are the most common.
* **Storage**: 64 GB and 128 GB dominate.
* **Battery**: 5000 mAh is the most offered battery capacity.
* **Camera Setup**: Dual and Triple cameras are widespread.
* **Ratings**: Most phones have user ratings between **4.0 and 4.4** stars.

---

### 5. Additional Insights

* 💰 **Budget brands** like Infinix, Tecno, and Poco dominate the low-cost market.
* ⭐ **Premium offerings** come from Apple, OnePlus, and Samsung.
* 📷 Phones with better camera setups and battery life usually fall in mid or premium range.
* 📊 Most products are priced between ₹8,000 and ₹18,000 — indicating a strong mid-tier market in India.

---

## 🙌 Acknowledgements

* Flipkart for the dataset (scraped)
* Streamlit, Plotly, Matplotlib, and Seaborn for interactive visualizations

---

## 👩‍💻 Author

Built with ❤️ by **Rutuja Sankhe**
