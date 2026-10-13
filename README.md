# Tugas Praktik Sesi 10 – Unit Testing dengan PyTest

## Isi
- `pricing.py` – modul asli, tidak diubah (acuan)
- `tests/test_pricing.py` – 19 test (13 fungsi test, beberapa dengan parametrize)
- `pytest.ini` – konfigurasi agar `pytest` menemukan test tanpa argumen tambahan
- `tools/mutation_test.py` – skrip pengujian mutasi
- `hasil/pytest_v.txt` – keluaran `pytest -v` pada kode yang benar
- `hasil/mutasi_output.txt` – keluaran skrip pengujian mutasi
- `hasil/tabel_mutasi.md` – tabel hasil pengujian mutasi
- `JAWABAN_ANALISIS.md` – jawaban pertanyaan analisis

## Cara menjalankan
```bash
pip install pytest
pytest -v                      # menjalankan seluruh test
python tools/mutation_test.py  # menjalankan pengujian mutasi
```
