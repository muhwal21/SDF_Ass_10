# Jawaban Pertanyaan Analisis

**1. Kenapa pakai pytest.approx untuk float?**
Float tidak bisa menyimpan semua desimal dengan tepat, jadi hasil seperti 1998 bisa muncul sebagai 1997.9999999999998. Kalau pakai `==`, test bisa gagal padahal logikanya benar. `pytest.approx` memberi toleransi kecil untuk selisih seperti itu, tapi tetap menangkap kesalahan logika.

**2. Kenapa file nyata lebih berisiko dibanding tmp_path?**
Test yang menulis ke file asli bisa menimpa atau menghapus data, bergantung pada izin folder, dan meninggalkan sisa file yang memengaruhi test berikutnya. `tmp_path` membuat folder baru yang kosong untuk setiap test dan otomatis dihapus setelahnya, jadi hasilnya lebih konsisten.

**3. Test paling lemah**
Menurut saya `test_tax_adds_eleven_percent`. Versi awalnya menghitung harapan dengan rumus yang sama seperti kode aslinya, jadi kurang berguna. Sudah saya ganti dengan angka 1110. Namun aturan pajak setelah diskon masih sulit diuji, karena perkalian berlaku sebaliknya juga. Mutan yang menukar urutan pajak dan diskon akan lolos.

**4. Pengaruh pengujian mutasi**
Sebelumnya saya menilai test dari jumlahnya saja. Setelah pengujian mutasi, saya sadar yang penting adalah apakah test gagal ketika kode salah. Tiga mutan tertangkap, tapi mutan penukaran urutan lolos, jadi test masih punya celah.

**5. Padanan PyTest dan JUnit 5**
- `pytest.raises` → `assertThrows`
- `@pytest.mark.parametrize` → `@ParameterizedTest` dengan `@ValueSource` atau `@CsvSource`
- Fixture (`tmp_path`) → `@BeforeEach` dan `@TempDir`

**6. Kenapa "total anggota selalu lebih besar dari subtotal" salah?**
Total anggota = 2000 × 0.9 × 1.11 = 1998, lebih kecil dari subtotal 2000. Yang lebih besar adalah total non-anggota: 2000 × 1.11 = 2220. Diskon 10% lebih besar pengaruhnya daripada pajak 11%, jadi total anggota selalu sedikit di bawah subtotal.
