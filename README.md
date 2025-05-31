# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**

## **Business Understanding**
Jaya Jaya Institut merupakan lembaga pendidikan tinggi yang telah beroperasi sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah meluluskan banyak alumni dengan rekam jejak yang membanggakan. Namun demikian, tidak sedikit pula mahasiswa yang tidak berhasil menyelesaikan studi mereka alias mengalami dropout.

### **Permasalahan Bisnis**
Tingginya angka mahasiswa yang mengalami dropout menjadi tantangan serius bagi institusi pendidikan seperti Jaya Jaya Institut. Untuk itu, pihak institusi ingin melakukan deteksi dini terhadap mahasiswa yang berpotensi dropout agar bisa segera diberikan pendampingan dan intervensi yang tepat.

### **Cakupan Proyek**
Sebagai upaya menjawab permasalahan tersebut, proyek ini bertujuan untuk menggali wawasan dari data guna mengidentifikasi faktor-faktor utama yang memengaruhi keputusan mahasiswa untuk tidak menyelesaikan studi. Selain itu, akan dikembangkan pula sebuah business dashboard yang dapat membantu institusi dalam memantau dan mengawasi indikator-indikator penting terkait potensi dropout mahasiswa.

### **Persiapan**

Sumber data: [Students' Performance]](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

**Setup environment:**
**1. Clone repository**
```
git clone https://github.com/rizaisnakhoir/students-performance-dashboard.git
cd students-performance-dashboard
```

**2. Buat virtual environment**
```
python -m venv venv
```

**3. Aktifkan virtual environment**

**Windows**
```
venv\Scripts\activate
```
**macOS/Linux**
```
source venv/bin/activate
```

**4. Install dependencies**
```
pip install -r requirements.txt
```

**5. Jalankan Jupyter Notebook**

## **Business Dashboard**
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.
Link Dashboard: [Students' Performance Dashboard](https://lookerstudio.google.com/reporting/4ecb0ad1-7c86-4204-a1cd-22d3c677f766)

## **Menjalankan Sistem Machine Learning**
Running kode berikut untuk menjalankan protoype sistem machine learning yang telah dibuat menggunakan Streamlit secara lokal. 
```
streamlit run app.py
```
Adapun akses ke prototype tersebut dapat dilakukan secara online melalui: https://jji-students-performance.streamlit.app/

## **Conclusion**
Berdasarkan analisis data dan model prediktif yang telah dikembangkan, dapat disimpulkan bahwa beberapa faktor utama yang berkontribusi terhadap kemungkinan mahasiswa melakukan dropout antara lain adalah performa akademik di semester awal, keterlambatan pembayaran uang kuliah, dan nilai saat masuk. Model klasifikasi yang dibangun menggunakan 10 fitur terpenting mampu memprediksi status dropout mahasiswa dengan cukup baik, dan dapat digunakan sebagai alat bantu dalam proses pengambilan keputusan oleh pihak institusi.

Dengan adanya sistem prediksi ini, institusi dapat mendeteksi lebih awal mahasiswa yang berisiko tinggi untuk dropout dan memberikan perhatian atau intervensi secara lebih proaktif.

### **Rekomendasi Action Items**
Berikut beberapa langkah strategis yang direkomendasikan bagi Jaya Jaya Institut untuk menurunkan tingkat dropout:
1. Implementasikan dashboard monitoring
   Gunakan dashboard interaktif untuk memantau secara real-time mahasiswa dengan risiko tinggi dropout berdasarkan indikator yang telah teridentifikasi.

2. Program bimbingan akademik khusus
   Sediakan layanan bimbingan atau mentoring bagi mahasiswa yang terdeteksi berisiko dropout, dengan fokus pada peningkatan performa akademik dan motivasi belajar.

3. Keringanan atau fleksibilitas biaya
   Evaluasi kemungkinan memberi keringanan biaya kuliah atau skema pembayaran yang lebih fleksibel bagi mahasiswa yang mengalami kesulitan keuangan namun menunjukkan potensi akademik yang baik.