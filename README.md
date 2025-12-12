# 📊 Sales Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, interactive data visualization dashboard built with **Streamlit** for analyzing sales data. This project demonstrates the power of Streamlit's components for creating professional-grade analytics applications.

![Dashboard Preview](https://img.shields.io/badge/Dashboard-Live-success)

---

## 🌟 Features

### 📦 Basic Components Used (10+ Components)

| No. | Component | Description | Location |
|-----|-----------|-------------|----------|
| 1 | `st.title()` | Main page title | Header |
| 2 | `st.sidebar` | Navigation panel | Left sidebar |
| 3 | `st.file_uploader()` | Custom data upload | Sidebar |
| 4 | `st.selectbox()` | Theme selection | Sidebar |
| 5 | `st.radio()` | Animation toggle & granularity | Sidebar & Tab 2 |
| 6 | `st.multiselect()` | Category/Region/Product filters | Filter section |
| 7 | `st.slider()` | Date range selection | Filter section |
| 8 | `st.metric()` | KPI display cards | Metrics section |
| 9 | `st.tabs()` | Content organization | Main content |
| 10 | `st.columns()` | Layout management | Throughout |
| 11 | `st.dataframe()` | Data table display | Raw Data tab |
| 12 | `st.download_button()` | Export functionality | Raw Data tab |
| 13 | `st.number_input()` | Row count selection | Raw Data tab |

### 📈 Interactive Visualizations

- **Line Charts** - Sales and quantity trends over time
- **Bar Charts** - Category and product performance comparison
- **Pie/Donut Charts** - Distribution analysis by region
- **Scatter Plots** - Correlation analysis with dynamic coloring
- **Heatmaps** - Feature correlation matrix

### ✨ Key Features

- 🎨 **Dark Theme** - Modern, professional dark mode design
- 🔄 **Real-time Updates** - Charts update instantly with filter changes
- 📤 **File Upload** - Analyze your own CSV data
- 📥 **Data Export** - Download filtered data as CSV
- 📱 **Responsive** - Works on desktop and mobile devices
- 🚀 **Fast Loading** - Optimized with `@st.cache_data`

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/streamlit-sales-dashboard.git
   cd streamlit-sales-dashboard
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - The app will open automatically at `http://localhost:8501`

---

## 📁 Project Structure

```
streamlit-sales-dashboard/
├── 📄 app.py                  # Main Streamlit application
├── 📁 data/
│   └── 📊 sample_data.csv     # Sample sales dataset
├── 📁 utils/
│   └── 🔧 helpers.py          # Helper functions & chart creators
├── 📋 requirements.txt        # Python dependencies
├── 📖 README.md               # Project documentation
└── 🚫 .gitignore              # Git ignore rules
```

---

## 📊 Dataset Format

The dashboard expects CSV files with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| Date | datetime | Transaction date |
| Product | string | Product name |
| Category | string | Product category |
| Sales | numeric | Sales amount |
| Quantity | numeric | Quantity sold |
| Region | string | Sales region |
| Customer_Type | string | Customer segment |

### Sample Data Preview

```csv
Date,Product,Category,Sales,Quantity,Region,Customer_Type
2024-01-01,Laptop,Electronics,1500000,10,Jakarta,Corporate
2024-01-01,Smartphone,Electronics,800000,15,Surabaya,Retail
```

---

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Set main file path to `app.py`
6. Click "Deploy"

Your app will be live at: `https://your-app-name.streamlit.app`

---

## 🎯 Usage Guide

### 1. Data Loading
- Use the **sample data** provided, or
- **Upload your own CSV** via the sidebar uploader

### 2. Filtering Data
- Select categories, regions, and products using **multiselect**
- Adjust date range with the **slider**
- Changes apply instantly to all visualizations

### 3. Exploring Visualizations
- **Overview Tab**: Summary charts and KPIs
- **Trend Analysis Tab**: Time-series analysis
- **Deep Dive Tab**: Correlation and scatter analysis
- **Raw Data Tab**: View and download filtered data

### 4. Customization
- Change **chart theme** in sidebar
- Toggle **animations** on/off

---

## 💡 Reflection Questions

### 1. Mengapa penting untuk mendeploy project ke Streamlit, dan apa manfaat utama bagi pengguna dibandingkan hanya menyimpan hasil analisis dalam notebook?

Mendeploy project ke Streamlit sangat penting karena beberapa alasan fundamental:

#### 🌐 Aksesibilitas
- **Tanpa Instalasi**: Stakeholder non-teknis dapat mengakses dashboard melalui web browser tanpa perlu menginstall Python, Jupyter, atau dependencies lainnya.
- **Device Agnostic**: Dashboard dapat diakses dari laptop, tablet, atau smartphone.
- **Always Available**: Dengan deployment di cloud, aplikasi tersedia 24/7.

#### 🔄 Interaktivitas
- **Real-time Exploration**: User dapat mengubah filter dan melihat perubahan secara langsung, berbeda dengan notebook yang static.
- **No Coding Required**: Stakeholder tidak perlu mengerti code untuk melakukan eksplorasi data.
- **What-If Analysis**: Memungkinkan skenario "bagaimana jika" dengan mengubah parameter secara interaktif.

#### 👥 Kemudahan bagi Stakeholder Non-Teknis
- **User-Friendly Interface**: Tampilan visual yang intuitif tanpa perlu melihat code.
- **Shareable URL**: Mudah dibagikan melalui link, tidak perlu share file notebook yang besar.
- **Professional Presentation**: Tampilan yang lebih polished dan presentable untuk meeting dengan klien atau manajemen.
- **Collaborative**: Semua stakeholder melihat data yang sama dan up-to-date.

#### 📊 Perbandingan dengan Notebook

| Aspek | Jupyter Notebook | Streamlit App |
|-------|------------------|---------------|
| Audience | Data Scientists | Semua Stakeholder |
| Akses | Perlu Python environment | Hanya browser |
| Interaktivitas | Jalankan cell satu-satu | Real-time interaction |
| Sharing | Share file .ipynb | Share URL |
| Update Data | Rerun semua cell | Refresh page |

---

### 2. Mengapa interaktivitas justru menjadi bagian penting dari dashboard atau ML app?

Komponen interaktif seperti slider, selectbox, atau file uploader BUKAN "opsional" melainkan **fundamental** untuk dashboard yang efektif. Berikut alasannya:

#### 🔍 Eksplorasi Data
- **Drill-Down Analysis**: User dapat fokus pada subset data tertentu (misalnya, hanya melihat sales di Jakarta, atau hanya kategori Electronics).
- **Pattern Discovery**: Dengan mengubah filter, user dapat menemukan pola tersembunyi yang mungkin tidak terlihat dalam view agregat.
- **Comparative Analysis**: Memungkinkan perbandingan cepat antar kategori, periode, atau region.

```
Contoh: Dengan slider tanggal, user bisa melihat bahwa penjualan Laptop 
meningkat signifikan di minggu terakhir bulan - insight yang mungkin 
tidak terlihat jika hanya melihat data agregat bulanan.
```

#### 🤖 Eksperimen Model (untuk ML Apps)
- **Parameter Tuning**: User dapat melihat bagaimana perubahan threshold atau hyperparameter mempengaruhi hasil prediksi.
- **Feature Selection**: Memahami kontribusi masing-masing feature terhadap model.
- **Model Comparison**: Membandingkan performa beberapa model secara visual dan interaktif.

```
Contoh: Pada aplikasi credit scoring, slider untuk mengatur threshold 
probability memungkinkan user melihat trade-off antara precision dan 
recall secara real-time.
```

#### 📈 Pengambilan Keputusan
- **Data-Driven Decisions**: Stakeholder dapat mengeksplorasi data sendiri untuk mendukung keputusan bisnis.
- **Scenario Planning**: "Bagaimana jika kita fokus ke region A?" atau "Apa dampaknya jika kita stop jual produk B?"
- **Immediate Insights**: Tidak perlu menunggu data analyst untuk generate laporan baru.
- **Self-Service Analytics**: Memberdayakan tim non-teknis untuk menjawab pertanyaan mereka sendiri.

#### 💡 Value Proposition Interaktivitas

| Tanpa Interaktivitas | Dengan Interaktivitas |
|---------------------|----------------------|
| Laporan statis | Eksplorasi dinamis |
| One-size-fits-all | Personalized view |
| Perlu request ke analyst | Self-service |
| Delayed insights | Real-time insights |
| Passive consumption | Active engagement |

#### 🎯 Kesimpulan
Interaktivitas mengubah dashboard dari **presentasi satu arah** menjadi **alat eksplorasi dua arah**. Ini meningkatkan:
1. **Engagement** - User lebih tertarik dan invested
2. **Understanding** - User memahami data lebih dalam
3. **Adoption** - Dashboard lebih sering digunakan
4. **Value** - ROI dari project analisis lebih tinggi

---

## 🔧 Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation
- **[Plotly](https://plotly.com/python/)** - Interactive visualizations
- **[NumPy](https://numpy.org/)** - Numerical computing

---

## 📸 Screenshots

### Dashboard Overview
The main dashboard provides a comprehensive view of sales KPIs and interactive filters.

### Interactive Filters
Users can filter data by category, region, product, and date range.

### Trend Analysis
Time-series visualization with customizable granularity (daily/weekly).

### Deep Dive Analysis
Scatter plots and correlation heatmaps for advanced analysis.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Data Analyst Portfolio**

- GitHub: [@Aditya Nurrohman](https://github.com/adityanrrhmn)
- LinkedIn: [Aditya Nurrohman](https://linkedin.com/in/adityanrhmn)

---

## 🙏 Acknowledgments

- Streamlit team for the amazing framework
- Plotly for beautiful interactive charts
- The Python data science community

---

<p align="center">
  Made with ❤️ using Streamlit
</p>
