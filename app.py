"""
========================================================================
📊 DASHBOARD ANALISIS PENDAPATAN RESTORAN - STREAMLIT
========================================================================

Ini adalah aplikasi web sederhana untuk menampilkan data pendapatan restoran
dalam bentuk grafik dan tabel yang interaktif.

Dibuat dengan: Python + Streamlit + Pandas + Plotly

Cocok untuk pemula yang ingin belajar membuat dashboard!
========================================================================
"""

# ========================================================================
# BAGIAN 1: IMPORT LIBRARY
# ========================================================================
# Library adalah kumpulan kode yang sudah dibuat orang lain
# yang bisa kita pakai untuk mempermudah pekerjaan kita.

import streamlit as st          # Library utama untuk membuat web dashboard
import pandas as pd             # Library untuk mengolah data dalam bentuk tabel
import plotly.express as px     # Library untuk membuat grafik interaktif
from datetime import datetime   # Library untuk bekerja dengan tanggal
import os                       # Library untuk akses file di komputer


# ========================================================================
# BAGIAN 2: PENGATURAN HALAMAN
# ========================================================================
# Bagian ini mengatur tampilan dasar halaman web kita

st.set_page_config(
    page_title="Dashboard Restoran",   # Judul di tab browser
    layout="wide"                          # Tampilan lebar (full screen)
)

# CSS sederhana untuk mempercantik tampilan
# CSS adalah bahasa untuk mengatur warna, ukuran, dll



# ========================================================================
# BAGIAN 3: FUNGSI-FUNGSI HELPER
# ========================================================================
# Fungsi adalah blok kode yang bisa dipanggil berulang kali.
# Kita buat fungsi agar kode lebih rapi dan tidak berulang.

def muat_data():
    """
    FUNGSI: Memuat data dari file CSV
    
    Apa itu CSV? CSV adalah format file untuk menyimpan data tabel,
    seperti Excel tapi lebih sederhana.
    
    Returns:
        DataFrame: Data dalam bentuk tabel pandas
    """
    # Memuat data dari file Restaurant_revenue.csv
    lokasi_file = os.path.join(os.path.dirname(__file__), 'data', 'Restaurant_revenue.csv')
    df = pd.read_csv(lokasi_file)
    
    return df


def format_rupiah(angka):
    """]
    FUNGSI: Mengubah angka menjadi format mata uang
    
    Contoh: 1500.50 -> "$1,500.50"
    
    Parameter:
        angka: Nilai numerik yang ingin diformat
    
    Returns:
        String dalam format mata uang
    """
    return f"${angka:,.2f}"


def buat_grafik_batang(data, kolom_x, kolom_y, judul):
    """
    FUNGSI: Membuat grafik batang (bar chart) menggunakan Plotly
    
    Grafik batang bagus untuk membandingkan nilai antar kategori.
    
    Parameter:
        data: DataFrame berisi data
        kolom_x: Nama kolom untuk sumbu X (horizontal)
        kolom_y: Nama kolom untuk sumbu Y (vertikal)
        judul: Judul grafik
    
    Returns:
        Figure Plotly yang bisa ditampilkan
    """
    grafik = px.bar(
        data,
        x=kolom_x,
        y=kolom_y,
        title=judul,
        template="plotly_dark",  # Tema gelap
        color=kolom_x            # Warna berbeda tiap kategori
    )
    
    # Mengatur background transparan
    grafik.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return grafik


def buat_grafik_pie(data, kolom_nilai, kolom_nama, judul):
    """
    FUNGSI: Membuat grafik pie (lingkaran) menggunakan Plotly
    
    Grafik pie bagus untuk menunjukkan proporsi/persentase.
    
    Parameter:
        data: DataFrame berisi data
        kolom_nilai: Nama kolom berisi nilai (angka)
        kolom_nama: Nama kolom berisi label/nama kategori
        judul: Judul grafik
    
    Returns:
        Figure Plotly yang bisa ditampilkan
    """
    grafik = px.pie(
        data,
        values=kolom_nilai,
        names=kolom_nama,
        title=judul,
        template="plotly_dark",
        hole=0.4  # Membuat lubang di tengah (donut chart)
    )
    
    grafik.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return grafik


# ========================================================================
# BAGIAN 4: MEMUAT DATA (harus sebelum sidebar agar filter bisa akses data)
# ========================================================================

# Memuat data menggunakan fungsi yang sudah kita buat
try:
    df = muat_data()  # Memuat data dari Restaurant_revenue.csv
    data_berhasil = True
except Exception as e:
    st.error(f"Gagal memuat data: {e}")
    data_berhasil = False


# ========================================================================
# BAGIAN 5: SIDEBAR (PANEL SAMPING)
# ========================================================================
# Sidebar adalah panel di sebelah kiri yang berisi kontrol/filter

# Variabel untuk menyimpan pilihan filter (default semua dipilih)
cuisine_dipilih = []
promo_dipilih = []

with st.sidebar:
    # Menampilkan judul di sidebar
    # st.title("Kontrol Panel")
    # st.markdown("---")  # Garis pemisah horizontal
    
    # --- FILTER DATA ---
    # KOMPONEN: st.multiselect() - Dropdown pilihan ganda
    st.subheader("Filter Data")
    
    if data_berhasil:
        # Filter Jenis Masakan (Cuisine_Type)
        if 'Cuisine_Type' in df.columns:
            cuisine_dipilih = st.multiselect(
                "Jenis Masakan",
                options=df['Cuisine_Type'].unique().tolist(),  # Semua jenis masakan unik
                # default=df['Cuisine_Type'].unique().tolist(),  # Default: semua dipilih
                help="Pilih satu atau beberapa jenis masakan"
            )
            
        
        # Filter Promosi (Promotions: 0 atau 1)
        if 'Promotions' in df.columns:
            promo_options = {0: "Tanpa Promo", 1: "Ada Promo"}
            promo_dipilih = st.multiselect(
                "Status Promosi",
                options=[0, 1],
                format_func=lambda x: promo_options[x],
                help="Filter berdasarkan ada/tidaknya promosi"
            )
    



    
# ========================================================================
# BAGIAN 6: KONTEN UTAMA (Hanya ditampilkan jika data berhasil dimuat)
# ========================================================================

if data_berhasil:
    
    # --- JUDUL HALAMAN ---
    # KOMPONEN: st.title() - Menampilkan judul besar
    st.title("Dashboard Analisis Pendapatan Restoran")
    st.markdown("*Dashboard interaktif untuk melihat data pendapatan restoran*")
    
    # Menerapkan filter ke data
    # Filter hanya menampilkan baris yang sesuai pilihan
    df_filter = df.copy()
    
    if 'Cuisine_Type' in df.columns and cuisine_dipilih:
        df_filter = df_filter[df_filter['Cuisine_Type'].isin(cuisine_dipilih)]
    
    if 'Promotions' in df.columns and promo_dipilih:
        df_filter = df_filter[df_filter['Promotions'].isin(promo_dipilih)]
    
    st.markdown("---")
    
    # --- KEY PERFORMANCE INDICATORS (KPI) ---
    # KPI adalah angka-angka penting yang menunjukkan performa bisnis
    
    st.subheader("Ringkasan Performa")
    
    # Menghitung metrics dari data yang sudah difilter
    total_revenue = df_filter['Monthly_Revenue'].sum() if 'Monthly_Revenue' in df_filter.columns else 0
    total_customers = df_filter['Number_of_Customers'].sum() if 'Number_of_Customers' in df_filter.columns else 0
    rata_rata_revenue = df_filter['Monthly_Revenue'].mean() if 'Monthly_Revenue' in df_filter.columns else 0
    rata_rata_spending = df_filter['Average_Customer_Spending'].mean() if 'Average_Customer_Spending' in df_filter.columns else 0
    
    # KOMPONEN: st.columns() - Membuat 4 kolom untuk 4 metric
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    
    with kpi1:
        # KOMPONEN: st.metric() - Menampilkan angka dengan style KPI
        st.metric(
            label="Total Pendapatan",   # Label di atas angka
            value=format_rupiah(total_revenue)  # Nilai utama
        )
    
    with kpi2:
        st.metric(
            label="Total Pelanggan",
            value=f"{total_customers:,.0f}"  # Format dengan pemisah ribuan
        )
    
    with kpi3:
        st.metric(
            label="Rata-rata Revenue",
            value=format_rupiah(rata_rata_revenue)
        )
    
    with kpi4:
        st.metric(
            label="Rata-rata Spending",
            value=format_rupiah(rata_rata_spending)
        )
    
    st.markdown("---")
    
    # --- TABS UNTUK GRAFIK ---
    # KOMPONEN: st.tabs() - Membuat tab yang bisa diklik
    tab_grafik, tab_data = st.tabs(["Grafik", "Data Mentah"])
    
    # --- TAB 1: GRAFIK ---
    with tab_grafik:
        st.subheader("Visualisasi Data")
        
        # Membuat 2 kolom untuk 2 grafik
        kolom_grafik1, kolom_grafik2 = st.columns(2)
        
        with kolom_grafik1:
            # Grafik Batang: Pendapatan per Jenis Masakan
            if 'Cuisine_Type' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
                # Menghitung total pendapatan per jenis masakan
                revenue_cuisine = df_filter.groupby('Cuisine_Type')['Monthly_Revenue'].sum().reset_index()
                
                # Membuat grafik menggunakan fungsi yang sudah kita buat
                grafik_cuisine = buat_grafik_batang(
                    revenue_cuisine,
                    kolom_x='Cuisine_Type',
                    kolom_y='Monthly_Revenue',
                    judul='Pendapatan per Jenis Masakan'
                )
                
                # KOMPONEN: st.plotly_chart() - Menampilkan grafik Plotly
                st.plotly_chart(grafik_cuisine, use_container_width=True)
        
        with kolom_grafik2:
            # Grafik Pie: Distribusi Pendapatan per Jenis Masakan
            if 'Cuisine_Type' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
                revenue_pie = df_filter.groupby('Cuisine_Type')['Monthly_Revenue'].sum().reset_index()
                
                grafik_pie = buat_grafik_pie(
                    revenue_pie,
                    kolom_nilai='Monthly_Revenue',
                    kolom_nama='Cuisine_Type',
                    judul='Distribusi Pendapatan per Masakan'
                )
                
                st.plotly_chart(grafik_pie, use_container_width=True)
        
        # Grafik tambahan: Perbandingan Promo vs Non-Promo
        st.subheader("Perbandingan: Dengan Promo vs Tanpa Promo")
        
        if 'Promotions' in df_filter.columns and 'Monthly_Revenue' in df_filter.columns:
            # Menghitung rata-rata revenue untuk promo dan non-promo
            promo_analysis = df_filter.groupby('Promotions').agg({
                'Monthly_Revenue': 'mean',
                'Number_of_Customers': 'mean'
            }).reset_index()
            promo_analysis['Status'] = promo_analysis['Promotions'].map({0: 'Tanpa Promo', 1: 'Ada Promo'})
            
            grafik_promo = px.bar(
                promo_analysis,
                x='Status',
                y='Monthly_Revenue',
                title='Rata-rata Pendapatan: Promo vs Non-Promo',
                template='plotly_dark',
                color='Status',
                color_discrete_map={'Tanpa Promo': '#ff6b6b', 'Ada Promo': '#4ecdc4'}
            )
            
            grafik_promo.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            
            st.plotly_chart(grafik_promo, use_container_width=True)
    
    # --- TAB 2: DATA MENTAH ---
    with tab_data:
        st.subheader("Tabel Data")
        
        # Info jumlah data
        st.info(f"Menampilkan {len(df_filter)} baris data")
        
        # KOMPONEN: st.number_input() - Input angka
        jumlah_baris = st.number_input(
            "Jumlah baris yang ditampilkan",
            min_value=5,
            max_value=len(df_filter),
            value=min(20, len(df_filter)),
            step=5,
            help="Pilih berapa banyak baris yang ingin ditampilkan"
        )
        
        # KOMPONEN: st.dataframe() - Menampilkan tabel data
        st.dataframe(
            df_filter.head(jumlah_baris),  # Ambil N baris pertama
            use_container_width=True,       # Lebar penuh
            hide_index=True                 # Sembunyikan nomor indeks
        )
        
        # KOMPONEN: st.download_button() - Tombol download
        csv = df_filter.to_csv(index=False)  # Konversi ke CSV
        st.download_button(
            label="Download Data (CSV)",
            data=csv,
            file_name=f"data_restoran_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            help="Klik untuk mendownload data yang sudah difilter"
        )
    
    # --- FOOTER ---
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>Dashboard Restoran | Dibuat menggunakan Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Pesan error jika data gagal dimuat
    st.error("Tidak dapat memuat data. Pastikan file Restaurant_revenue.csv ada di folder data.")
