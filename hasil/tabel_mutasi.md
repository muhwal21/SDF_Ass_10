| Kerusakan buatan | Test yang gagal | Kesimpulan daya deteksi |
|---|---|---|
| M1: menghapus penerapan diskon (`apply_member_discount` selalu mengembalikan subtotal) | `test_member_gets_ten_percent_discount` (3 kasus), `test_member_total_is_discounted_then_taxed` | Terdeteksi. Diskon diuji langsung dan lewat jalur total, sehingga kerusakan di salah satu tingkat tertangkap. |
| M2: mengubah tarif pajak 0.11 menjadi 0.10 | `test_tax_adds_eleven_percent`, `test_member_total_is_discounted_then_taxed`, `test_non_member_total_is_taxed_only` | Terdeteksi oleh tiga test. Nilai harapan ditulis sebagai angka konkret sehingga tidak ikut berubah bersama kode. |
| M3: menghapus validasi kuantitas (`if quantity <= 0`) | `test_subtotal_rejects_non_positive_quantity` (kuantitas 0 dan -1) | Terdeteksi. Hanya jalur kesalahan yang gagal, sedangkan perhitungan normal tetap lulus. |
