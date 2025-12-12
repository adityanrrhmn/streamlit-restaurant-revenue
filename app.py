import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# ========================================================================
# PENGATURAN HALAMAN
# ========================================================================
st.set_page_config(
    page_title="Dashboard Restoran",
    layout="wide"
)

# ========================================================================
# FUNGSI HELPER
# ========================================================================

def muat_data():
    """Memuat data transaksi restoran dari file CSV."""
    lokasi_file = os.path.join(os.path.dirname(__file__), 'data', 'Restaurant_revenue.csv')
    return pd.read_csv(lokasi_file)

def format_rupiah(angka):
    """Mengubah format angka numerik menjadi string mata uang (USD)."""
    return f"${angka:,.2f}"

def buat_grafik_batang(data, kolom_x, kolom_y, judul):
    """Membuat grafik batang menggunakan Plotly."""
    grafik = px.bar(
        data,
        x=kolom_x,
        y=kolom_y,
        title=judul,
        template="plotly_dark",
        color=kolom_x
    )
    grafik.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return grafik

def buat_grafik_pie(data, kolom_nilai, kolom_nama, judul):
    """Membuat grafik pie menggunakan Plotly."""
    grafik = px.pie(
        data,
        values=kolom_nilai,
        names=kolom_nama,
        title=judul,
        template="plotly_dark",
        hole=0.4
    )
    grafik.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return grafik

# ========================================================================
# LOAD DATA
# ========================================================================
try:
    df = muat_data()
    data_berhasil = True
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    data_berhasil = False

# ========================================================================
# SIDEBAR
# ========================================================================
cuisine_dipilih = []
promo_dipilih = []

with st.sidebar:
    st.subheader("Filter Data")
    
    if data_berhasil:
        if 'Cuisine_Type' in df.columns:
            cuisine_dipilih = st.multiselect(
                "Jenis Masakan",
                options=df['Cuisine_Type'].unique().tolist(),
                help="Pilih jenis masakan"
            )
            
        if 'Promotions' in df.columns:
            promo_options = {0: "Tanpa Promo", 1: "Ada Promo"}
            promo_dipilih = st.multiselect(
                "Status Promosi",
                options=[0, 1],
                format_func=lambda x: promo_options[x],
                help="Filter status promosi"
            )

# ========================================================================
# KONTEN UTAMA
# ========================================================================
if data_berhasil:
    st.title("Dashboard Analisis Pendapatan Restoran")
    st.markdown("*Overview performa dan pendapatan restoran*")
    
    # Filter Data
    df_filter = df.copy()
    if 'Cuisine_Type' in df.columns and cuisine_dipilih:
        df_filter = df_filter[df_filter['Cuisine_Type'].isin(cuisine_dipilih)]
    
    if 'Promotions' in df.columns and promo_dipilih:
        df_filter = df_filter[df_filter['Promotions'].isin(promo_dipilih)]
    
    st.markdown("---")
    
    # KPI Section
    st.subheader("Ringkasan Performa")
    
    total_revenue = df_filter['Monthly_Revenue'].sum() if 'Monthly_Revenue' in df_filter.columns else 0
    total_customers = df_filter['Number_of_Customers'].sum() if 'Number_of_Customers' in df_filter.columns else 0
    rata_rata_revenue = df_filter['Monthly_Revenue'].mean() if 'Monthly_Revenue' in df_filter.columns else 0
    rata_rata_spending = df_filter['Average_Customer_Spending'].mean() if 'Average_Customer_Spending' in df_filter.columns else 0
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(label="Total Pendapatan", value=format_rupiah(total_revenue))
    with kpi2:
        st.metric(label="Total Pelanggan", value=f"{total_customers:,.0f}")
    with kpi3:
        st.metric(label="Rata-rata Revenue", value=format_rupiah(rata_rata_revenue))
    with kpi4:
        st.metric(label="Rata-rata Spending", value=format_rupiah(rata_rata_spending))
    
    st.markdown("---")
    
    # Tabs Section
    tab_grafik, tab_data = st.tabs(["Visualisasi", "Data Detail"])
    
    # Tab Grafik
    with tab_grafik:
        col1, col2 = st.columns(2)
        
        with col1:
            if 'Cuisine_Type' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
                revenue_cuisine = df_filter.groupby('Cuisine_Type')['Monthly_Revenue'].sum().reset_index()
                fig_cuisine = buat_grafik_batang(
                    revenue_cuisine,
                    kolom_x='Cuisine_Type',
                    kolom_y='Monthly_Revenue',
                    judul='Pendapatan per Jenis Masakan'
                )
                st.plotly_chart(fig_cuisine, use_container_width=True)
        
        with col2:
            if 'Cuisine_Type' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
                revenue_pie = df_filter.groupby('Cuisine_Type')['Monthly_Revenue'].sum().reset_index()
                fig_pie = buat_grafik_pie(
                    revenue_pie,
                    kolom_nilai='Monthly_Revenue',
                    kolom_nama='Cuisine_Type',
                    judul='Distribusi Pendapatan'
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        # Promo Analysis
        st.subheader("Analisis Promosi")
        if 'Promotions' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
            promo_analysis = df_filter.groupby('Promotions').agg({
                'Monthly_Revenue': 'mean'
            }).reset_index()
            promo_analysis['Status'] = promo_analysis['Promotions'].map({0: 'Tanpa Promo', 1: 'Ada Promo'})
            
            fig_promo = px.bar(
                promo_analysis,
                x='Status',
                y='Monthly_Revenue',
                title='Rata-rata Pendapatan: Promo vs Non-Promo',
                template='plotly_dark',
                color='Status',
                color_discrete_map={'Tanpa Promo': '#ff6b6b', 'Ada Promo': '#4ecdc4'}
            )
            fig_promo.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            st.plotly_chart(fig_promo, use_container_width=True)
            
    # Tab Data
    with tab_data:
        st.subheader("Tabel Data Transaksi")
        st.info(f"Menampilkan {len(df_filter)} baris data")
        
        rows_to_show = st.number_input(
            "Tampilkan jumlah baris",
            min_value=5,
            max_value=len(df_filter),
            value=min(20, len(df_filter)),
            step=5
        )
        
        st.dataframe(
            df_filter.head(rows_to_show),
            use_container_width=True,
            hide_index=True
        )
        
        csv = df_filter.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"restaurant_data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
        
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888; font-size: 0.8em;'>
        Copyright © 2025 Streamlit Restaurant Dashboard
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("Data tidak ditemukan. Pastikan 'data/Restaurant_revenue.csv' tersedia.")

