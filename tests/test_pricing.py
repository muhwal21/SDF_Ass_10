import pytest

from pricing import (
    add_tax,
    apply_member_discount,
    calculate_subtotal,
    calculate_total,
    write_receipt,
)


@pytest.mark.parametrize(
    ("unit_price", "quantity", "expected"),
    [
        (1000, 1, 1000),
        (1500, 3, 4500),
        (250, 4, 1000),
        (0, 5, 0),
    ],
)
def test_subtotal_is_price_times_quantity(unit_price, quantity, expected):
    assert calculate_subtotal(unit_price, quantity) == expected


def test_subtotal_rejects_negative_price():
    with pytest.raises(ValueError, match="unit_price must not be negative"):
        calculate_subtotal(-1, 2)


@pytest.mark.parametrize("quantity", [0, -1])
def test_subtotal_rejects_non_positive_quantity(quantity):
    with pytest.raises(ValueError, match="quantity must be positive"):
        calculate_subtotal(1000, quantity)


@pytest.mark.parametrize(
    ("subtotal", "expected"),
    [(1000, 900), (2000, 1800), (1, 0.9)],
)
def test_member_gets_ten_percent_discount(subtotal, expected):
    assert apply_member_discount(subtotal, is_member=True) == pytest.approx(expected)


def test_non_member_pays_full_subtotal():
    assert apply_member_discount(2000, is_member=False) == 2000


def test_tax_adds_eleven_percent():
    assert add_tax(1000) == pytest.approx(1110)


def test_member_total_is_discounted_then_taxed():
    # 2000 - 10% = 1800, + 11% = 1998
    assert calculate_total(1000, 2, is_member=True) == pytest.approx(1998)


def test_non_member_total_is_taxed_only():
    # 2000 + 11% = 2220
    assert calculate_total(1000, 2, is_member=False) == pytest.approx(2220)


def test_total_raises_on_invalid_input():
    with pytest.raises(ValueError, match="unit_price must not be negative"):
        calculate_total(-100, 1, is_member=True)


def test_receipt_lines_end_with_newline(tmp_path):
    receipt = tmp_path / "struk.txt"
    write_receipt(receipt, ["Kopi 1000", "Total 1110"])
    assert receipt.read_text(encoding="utf-8") == "Kopi 1000\nTotal 1110\n"


def test_empty_receipt_writes_single_newline(tmp_path):
    receipt = tmp_path / "kosong.txt"
    write_receipt(receipt, [])
    assert receipt.read_text(encoding="utf-8") == "\n"


def test_receipt_overwrites_existing_file(tmp_path):
    receipt = tmp_path / "struk.txt"
    write_receipt(receipt, ["baris lama"])
    write_receipt(receipt, ["baris baru"])
    assert receipt.read_text(encoding="utf-8") == "baris baru\n"


def test_receipt_keeps_utf8_characters(tmp_path):
    receipt = tmp_path / "utf8.txt"
    write_receipt(receipt, ["Café susu – Rp 1.000"])
    assert receipt.read_text(encoding="utf-8") == "Café susu – Rp 1.000\n"
