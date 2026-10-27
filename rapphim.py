# -*- coding: utf-8 -*-
"""
CHƯƠNG TRÌNH QUẢN LÝ RẠP CHIẾU PHIM
Ngôn ngữ: Python 3.x
Giao diện: Console
Lưu trữ: các file TXT
Cách chạy: python main.py
"""

import json
import os

FILE_DATA = {
    "phim": "phim.txt",
    "phong": "phong.txt",
    "suat_chieu": "suat_chieu.txt",
    "khach_hang": "khach_hang.txt",
    "ve": "ve.txt",
}

danh_sach_phim = []
danh_sach_phong = []
danh_sach_suat_chieu = []
danh_sach_khach_hang = []
danh_sach_ve = []


def nhap_chuoi(thong_bao, bat_buoc=True):
    while True:
        gia_tri = input(thong_bao).strip()
        if gia_tri or not bat_buoc:
            return gia_tri
        print("Dữ liệu không được để trống.")


def nhap_so_nguyen(thong_bao, toi_thieu=0):
    while True:
        try:
            gia_tri = int(input(thong_bao))
            if gia_tri < toi_thieu:
                print(f"Giá trị phải lớn hơn hoặc bằng {toi_thieu}.")
                continue
            return gia_tri
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ.")


def nhap_so_thuc(thong_bao, toi_thieu=0):
    while True:
        try:
            gia_tri = float(input(thong_bao))
            if gia_tri < toi_thieu:
                print(f"Giá trị phải lớn hơn hoặc bằng {toi_thieu}.")
                continue
            return gia_tri
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")


def tim_theo_ma(danh_sach, truong_ma, ma):
    for doi_tuong in danh_sach:
        if doi_tuong.get(truong_ma, "").lower() == ma.lower():
            return doi_tuong
    return None


def luu_du_lieu():
    """Lưu mỗi danh sách vào một file TXT, dữ liệu ở dạng JSON."""
    cac_danh_sach = {
        "phim": danh_sach_phim,
        "phong": danh_sach_phong,
        "suat_chieu": danh_sach_suat_chieu,
        "khach_hang": danh_sach_khach_hang,
        "ve": danh_sach_ve,
    }
    try:
        for ten, du_lieu in cac_danh_sach.items():
            with open(FILE_DATA[ten], "w", encoding="utf-8") as tep:
                json.dump(du_lieu, tep, ensure_ascii=False, indent=4)
        print("Đã lưu dữ liệu vào các file TXT.")
    except OSError as loi:
        print("Không thể lưu dữ liệu:", loi)


def doc_du_lieu():
    """Đọc dữ liệu từ các file TXT; file chưa tồn tại được bỏ qua."""
    cac_danh_sach = {
        "phim": danh_sach_phim,
        "phong": danh_sach_phong,
        "suat_chieu": danh_sach_suat_chieu,
        "khach_hang": danh_sach_khach_hang,
        "ve": danh_sach_ve,
    }
    for ten, danh_sach in cac_danh_sach.items():
        try:
            with open(FILE_DATA[ten], "r", encoding="utf-8") as tep:
                du_lieu = json.load(tep)
            if isinstance(du_lieu, list):
                danh_sach.clear()
                danh_sach.extend(du_lieu)
        except FileNotFoundError:
            continue
        except (json.JSONDecodeError, OSError) as loi:
            print(f"Không đọc được {FILE_DATA[ten]}: {loi}")
    print("Đã đọc dữ liệu (các file chưa tồn tại sẽ được bỏ qua).")


def them_phim():
    ma = nhap_chuoi("Nhập mã phim: ")
    if tim_theo_ma(danh_sach_phim, "ma_phim", ma):
        print("Mã phim đã tồn tại!")
        return
    phim = {
        "ma_phim": ma,
        "ten_phim": nhap_chuoi("Nhập tên phim: "),
        "the_loai": nhap_chuoi("Nhập thể loại: "),
        "thoi_luong": nhap_so_nguyen("Nhập thời lượng (phút): ", 1),
        "gia_ve": nhap_so_thuc("Nhập giá vé (VNĐ): ", 0),
    }
    danh_sach_phim.append(phim)
    print("Thêm phim thành công.")


def hien_thi_phim():
    if not danh_sach_phim:
        print("Danh sách phim đang trống.")
        return
    print("\n{:<12} {:<30} {:<22} {:>12} {:>15}".format(
        "Mã phim", "Tên phim", "Thể loại", "Thời lượng", "Giá vé (VNĐ)"))
    print("-" * 95)
    for p in danh_sach_phim:
        print("{:<12} {:<30} {:<22} {:>12} {:>15,.0f}".format(
            p["ma_phim"], p["ten_phim"][:29], p["the_loai"][:21],
            p["thoi_luong"], p["gia_ve"]))


def cap_nhat_phim():
    ma = nhap_chuoi("Nhập mã phim cần cập nhật: ")
    phim = tim_theo_ma(danh_sach_phim, "ma_phim", ma)
    if not phim:
        print("Không tìm thấy phim.")
        return
    print("Nhập thông tin mới:")
    phim["ten_phim"] = nhap_chuoi("Tên phim mới: ")
    phim["the_loai"] = nhap_chuoi("Thể loại mới: ")
    phim["thoi_luong"] = nhap_so_nguyen("Thời lượng mới (phút): ", 1)
    phim["gia_ve"] = nhap_so_thuc("Giá vé mới (VNĐ): ", 0)
    print("Cập nhật phim thành công.")


def xoa_phim():
    ma = nhap_chuoi("Nhập mã phim cần xóa: ")
    phim = tim_theo_ma(danh_sach_phim, "ma_phim", ma)
    if not phim:
        print("Không tìm thấy phim.")
        return
    if any(s["ma_phim"] == ma for s in danh_sach_suat_chieu):
        print("Không thể xóa: phim đang được dùng trong suất chiếu.")
        return
    danh_sach_phim.remove(phim)
    print("Xóa phim thành công.")


def tim_kiem_phim():
    tu_khoa = nhap_chuoi("Nhập mã hoặc tên phim cần tìm: ").casefold()
    ket_qua = [p for p in danh_sach_phim
               if tu_khoa in p["ma_phim"].casefold()
               or tu_khoa in p["ten_phim"].casefold()]
    if not ket_qua:
        print("Không tìm thấy phim.")
        return
    for p in ket_qua:
        print(f'{p["ma_phim"]} | {p["ten_phim"]} | {p["the_loai"]} | '
              f'{p["thoi_luong"]} phút | {p["gia_ve"]:,.0f} VNĐ')


def menu_phim():
    while True:
        print("\n--- QUẢN LÝ PHIM ---")
        print("1. Thêm phim\n2. Hiển thị phim\n3. Cập nhật phim")
        print("4. Xóa phim\n5. Tìm kiếm phim\n0. Quay lại")
        chon = input("Lựa chọn: ").strip()
        if chon == "1":
            them_phim()
        elif chon == "2":
            hien_thi_phim()
        elif chon == "3":
            cap_nhat_phim()
        elif chon == "4":
            xoa_phim()
        elif chon == "5":
            tim_kiem_phim()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def them_phong():
    ma = nhap_chuoi("Nhập mã phòng: ")
    if tim_theo_ma(danh_sach_phong, "ma_phong", ma):
        print("Mã phòng đã tồn tại!")
        return
    phong = {
        "ma_phong": ma,
        "ten_phong": nhap_chuoi("Nhập tên phòng: "),
        "so_ghe": nhap_so_nguyen("Nhập tổng số ghế: ", 1),
        "trang_thai": nhap_chuoi("Nhập trạng thái phòng (Hoạt động/Bảo trì): "),
    }
    danh_sach_phong.append(phong)
    print("Thêm phòng thành công.")


def hien_thi_phong():
    if not danh_sach_phong:
        print("Danh sách phòng đang trống.")
        return
    for p in danh_sach_phong:
        print(f'{p["ma_phong"]} | {p["ten_phong"]} | {p["so_ghe"]} ghế | {p["trang_thai"]}')


def cap_nhat_phong():
    ma = nhap_chuoi("Nhập mã phòng cần cập nhật: ")
    p = tim_theo_ma(danh_sach_phong, "ma_phong", ma)
    if not p:
        print("Không tìm thấy phòng.")
        return
    p["ten_phong"] = nhap_chuoi("Tên phòng mới: ")
    p["so_ghe"] = nhap_so_nguyen("Số ghế mới: ", 1)
    p["trang_thai"] = nhap_chuoi("Trạng thái mới: ")
    print("Cập nhật phòng thành công.")


def xoa_phong():
    ma = nhap_chuoi("Nhập mã phòng cần xóa: ")
    p = tim_theo_ma(danh_sach_phong, "ma_phong", ma)
    if not p:
        print("Không tìm thấy phòng.")
        return
    if any(s["ma_phong"] == ma for s in danh_sach_suat_chieu):
        print("Không thể xóa: phòng đang được sử dụng trong suất chiếu.")
        return
    danh_sach_phong.remove(p)
    print("Xóa phòng thành công.")


def menu_phong():
    while True:
        print("\n--- QUẢN LÝ PHÒNG CHIẾU ---")
        print("1. Thêm phòng\n2. Hiển thị phòng\n3. Cập nhật phòng")
        print("4. Xóa phòng\n0. Quay lại")
        chon = input("Lựa chọn: ").strip()
        if chon == "1":
            them_phong()
        elif chon == "2":
            hien_thi_phong()
        elif chon == "3":
            cap_nhat_phong()
        elif chon == "4":
            xoa_phong()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def them_suat_chieu():
    ma = nhap_chuoi("Nhập mã suất chiếu: ")
    if tim_theo_ma(danh_sach_suat_chieu, "ma_suat", ma):
        print("Mã suất chiếu đã tồn tại!")
        return
    ma_phim = nhap_chuoi("Nhập mã phim: ")
    phim = tim_theo_ma(danh_sach_phim, "ma_phim", ma_phim)
    if not phim:
        print("Mã phim không tồn tại.")
        return
    ma_phong = nhap_chuoi("Nhập mã phòng: ")
    phong = tim_theo_ma(danh_sach_phong, "ma_phong", ma_phong)
    if not phong:
        print("Mã phòng không tồn tại.")
        return
    if phong["trang_thai"].casefold() not in ("hoạt động", "hoat dong", "active"):
        print("Phòng không ở trạng thái hoạt động.")
        return
    suat = {
        "ma_suat": ma,
        "ma_phim": phim["ma_phim"],
        "ma_phong": phong["ma_phong"],
        "ngay_chieu": nhap_chuoi("Nhập ngày chiếu (VD 21/09/2026): "),
        "gio_chieu": nhap_chuoi("Nhập giờ chiếu (VD 19:30): "),
    }
    danh_sach_suat_chieu.append(suat)
    print("Thêm suất chiếu thành công.")


def hien_thi_suat_chieu():
    if not danh_sach_suat_chieu:
        print("Danh sách suất chiếu đang trống.")
        return
    for s in danh_sach_suat_chieu:
        phim = tim_theo_ma(danh_sach_phim, "ma_phim", s["ma_phim"])
        phong = tim_theo_ma(danh_sach_phong, "ma_phong", s["ma_phong"])
        ten_phim = phim["ten_phim"] if phim else "Không rõ"
        ten_phong = phong["ten_phong"] if phong else "Không rõ"
        print(f'{s["ma_suat"]} | {ten_phim} | {ten_phong} | '
              f'{s["ngay_chieu"]} {s["gio_chieu"]}')


def cap_nhat_suat_chieu():
    ma = nhap_chuoi("Nhập mã suất chiếu cần cập nhật: ")
    s = tim_theo_ma(danh_sach_suat_chieu, "ma_suat", ma)
    if not s:
        print("Không tìm thấy suất chiếu.")
        return
    ma_phim = nhap_chuoi("Mã phim mới: ")
    phim = tim_theo_ma(danh_sach_phim, "ma_phim", ma_phim)
    ma_phong = nhap_chuoi("Mã phòng mới: ")
    phong = tim_theo_ma(danh_sach_phong, "ma_phong", ma_phong)
    if not phim or not phong:
        print("Mã phim hoặc mã phòng không tồn tại.")
        return
    s["ma_phim"] = phim["ma_phim"]
    s["ma_phong"] = phong["ma_phong"]
    s["ngay_chieu"] = nhap_chuoi("Ngày chiếu mới: ")
    s["gio_chieu"] = nhap_chuoi("Giờ chiếu mới: ")
    print("Cập nhật suất chiếu thành công.")


def xoa_suat_chieu():
    ma = nhap_chuoi("Nhập mã suất chiếu cần xóa: ")
    s = tim_theo_ma(danh_sach_suat_chieu, "ma_suat", ma)
    if not s:
        print("Không tìm thấy suất chiếu.")
        return
    if any(v["ma_suat"] == ma and v["trang_thai"] == "Da dat" for v in danh_sach_ve):
        print("Không thể xóa suất chiếu đang có vé đã đặt.")
        return
    danh_sach_suat_chieu.remove(s)
    print("Xóa suất chiếu thành công.")


def tim_kiem_suat_chieu():
    tu_khoa = nhap_chuoi("Nhập mã suất, mã phim hoặc ngày chiếu: ").casefold()
    ket_qua = [s for s in danh_sach_suat_chieu
               if tu_khoa in s["ma_suat"].casefold()
               or tu_khoa in s["ma_phim"].casefold()
               or tu_khoa in s["ngay_chieu"].casefold()]
    if not ket_qua:
        print("Không tìm thấy suất chiếu.")
    else:
        for s in ket_qua:
            print(s)


def menu_suat_chieu():
    while True:
        print("\n--- QUẢN LÝ SUẤT CHIẾU ---")
        print("1. Thêm suất chiếu\n2. Hiển thị suất chiếu")
        print("3. Cập nhật suất chiếu\n4. Xóa suất chiếu")
        print("5. Tìm kiếm suất chiếu\n0. Quay lại")
        chon = input("Lựa chọn: ").strip()
        if chon == "1":
            them_suat_chieu()
        elif chon == "2":
            hien_thi_suat_chieu()
        elif chon == "3":
            cap_nhat_suat_chieu()
        elif chon == "4":
            xoa_suat_chieu()
        elif chon == "5":
            tim_kiem_suat_chieu()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def them_khach_hang():
    ma = nhap_chuoi("Nhập mã khách hàng: ")
    if tim_theo_ma(danh_sach_khach_hang, "ma_khach", ma):
        print("Mã khách hàng đã tồn tại!")
        return
    so_dien_thoai = nhap_chuoi("Nhập số điện thoại: ")
    if not so_dien_thoai.isdigit() or not 9 <= len(so_dien_thoai) <= 11:
        print("Số điện thoại phải gồm 9 đến 11 chữ số.")
        return
    email = nhap_chuoi("Nhập email: ")
    kh = {
        "ma_khach": ma,
        "ho_ten": nhap_chuoi("Nhập họ tên: "),
        "so_dien_thoai": so_dien_thoai,
        "email": email,
    }
    danh_sach_khach_hang.append(kh)
    print("Thêm khách hàng thành công.")


def hien_thi_khach_hang():
    if not danh_sach_khach_hang:
        print("Danh sách khách hàng đang trống.")
        return
    for kh in danh_sach_khach_hang:
        print(f'{kh["ma_khach"]} | {kh["ho_ten"]} | '
              f'{kh["so_dien_thoai"]} | {kh["email"]}')


def cap_nhat_khach_hang():
    ma = nhap_chuoi("Nhập mã khách hàng cần cập nhật: ")
    kh = tim_theo_ma(danh_sach_khach_hang, "ma_khach", ma)
    if not kh:
        print("Không tìm thấy khách hàng.")
        return
    kh["ho_ten"] = nhap_chuoi("Họ tên mới: ")
    so_dt = nhap_chuoi("Số điện thoại mới: ")
    if not so_dt.isdigit() or not 9 <= len(so_dt) <= 11:
        print("Số điện thoại không hợp lệ; giữ nguyên số cũ.")
    else:
        kh["so_dien_thoai"] = so_dt
    kh["email"] = nhap_chuoi("Email mới: ")
    print("Cập nhật khách hàng thành công.")


def xoa_khach_hang():
    ma = nhap_chuoi("Nhập mã khách hàng cần xóa: ")
    kh = tim_theo_ma(danh_sach_khach_hang, "ma_khach", ma)
    if not kh:
        print("Không tìm thấy khách hàng.")
        return
    if any(v["ma_khach"] == ma for v in danh_sach_ve):
        print("Không thể xóa khách hàng đã có thông tin vé.")
        return
    danh_sach_khach_hang.remove(kh)
    print("Xóa khách hàng thành công.")


def tim_kiem_khach_hang():
    tu_khoa = nhap_chuoi("Nhập mã hoặc tên khách hàng: ").casefold()
    ket_qua = [kh for kh in danh_sach_khach_hang
               if tu_khoa in kh["ma_khach"].casefold()
               or tu_khoa in kh["ho_ten"].casefold()]
    if not ket_qua:
        print("Không tìm thấy khách hàng.")
    else:
        for kh in ket_qua:
            print(f'{kh["ma_khach"]} | {kh["ho_ten"]} | '
                  f'{kh["so_dien_thoai"]} | {kh["email"]}')


def dat_ve():
    ma_khach = nhap_chuoi("Nhập mã khách hàng: ")
    kh = tim_theo_ma(danh_sach_khach_hang, "ma_khach", ma_khach)
    if not kh:
        print("Khách hàng không tồn tại. Vui lòng thêm khách hàng trước.")
        return
    ma_suat = nhap_chuoi("Nhập mã suất chiếu: ")
    suat = tim_theo_ma(danh_sach_suat_chieu, "ma_suat", ma_suat)
    if not suat:
        print("Suất chiếu không tồn tại.")
        return
    phong = tim_theo_ma(danh_sach_phong, "ma_phong", suat["ma_phong"])
    if not phong:
        print("Không tìm thấy phòng của suất chiếu.")
        return
    so_ghe = nhap_chuoi("Nhập số ghế (VD A05): ").upper()
    if not so_ghe:
        print("Số ghế không hợp lệ.")
        return
    so_ve_ghe = sum(1 for v in danh_sach_ve
                    if v["ma_suat"] == ma_suat and v["so_ghe"].upper() == so_ghe
                    and v["trang_thai"] == "Da dat")
    if so_ve_ghe:
        print("Ghế này đã được đặt cho suất chiếu.")
        return
    if len([c for c in so_ghe if c.isdigit()]) == 0:
        print("Số ghế cần có ít nhất một chữ số, ví dụ A05.")
        return
    ma_ve = nhap_chuoi("Nhập mã vé: ")
    if tim_theo_ma(danh_sach_ve, "ma_ve", ma_ve):
        print("Mã vé đã tồn tại.")
        return
    phim = tim_theo_ma(danh_sach_phim, "ma_phim", suat["ma_phim"])
    gia = phim["gia_ve"] if phim else 0
    ve = {
        "ma_ve": ma_ve,
        "ma_khach": kh["ma_khach"],
        "ma_suat": suat["ma_suat"],
        "so_ghe": so_ghe,
        "gia_ve": gia,
        "trang_thai": "Da dat",
    }
    danh_sach_ve.append(ve)
    luu_du_lieu()
    print(f"Đặt vé thành công. Giá vé: {gia:,.0f} VNĐ.")


def huy_ve():
    ma = nhap_chuoi("Nhập mã vé cần hủy: ")
    ve = tim_theo_ma(danh_sach_ve, "ma_ve", ma)
    if not ve:
        print("Không tìm thấy vé.")
        return
    if ve["trang_thai"] != "Da dat":
        print("Vé này đã được hủy trước đó.")
        return
    ve["trang_thai"] = "Da huy"
    luu_du_lieu()
    print("Hủy vé thành công.")


def hien_thi_ve():
    if not danh_sach_ve:
        print("Danh sách vé đang trống.")
        return
    for v in danh_sach_ve:
        kh = tim_theo_ma(danh_sach_khach_hang, "ma_khach", v["ma_khach"])
        suat = tim_theo_ma(danh_sach_suat_chieu, "ma_suat", v["ma_suat"])
        ten_khach = kh["ho_ten"] if kh else "Không rõ"
        ngay_gio = f'{suat["ngay_chieu"]} {suat["gio_chieu"]}' if suat else "Không rõ"
        print(f'{v["ma_ve"]} | Khách: {ten_khach} | Suất: {v["ma_suat"]} '
              f'({ngay_gio}) | Ghế: {v["so_ghe"]} | '
              f'{v["gia_ve"]:,.0f} VNĐ | {v["trang_thai"]}')


def tim_kiem_ve():
    tu_khoa = nhap_chuoi("Nhập mã vé hoặc mã khách hàng: ").casefold()
    ket_qua = [v for v in danh_sach_ve
               if tu_khoa in v["ma_ve"].casefold()
               or tu_khoa in v["ma_khach"].casefold()]
    if not ket_qua:
        print("Không tìm thấy vé.")
    else:
        for v in ket_qua:
            print(v)


def thong_ke():
    tong_ve_hop_le = sum(1 for v in danh_sach_ve if v["trang_thai"] == "Da dat")
    doanh_thu = sum(v["gia_ve"] for v in danh_sach_ve if v["trang_thai"] == "Da dat")
    print("\n========== THỐNG KÊ ==========")
    print("Tổng số phim:", len(danh_sach_phim))
    print("Tổng số phòng:", len(danh_sach_phong))
    print("Tổng số suất chiếu:", len(danh_sach_suat_chieu))
    print("Tổng số khách hàng:", len(danh_sach_khach_hang))
    print("Tổng số vé đã đặt:", tong_ve_hop_le)
    print(f"Doanh thu từ vé đã đặt: {doanh_thu:,.0f} VNĐ")
    print("===============================")


def menu_khach_hang():
    while True:
        print("\n--- QUẢN LÝ KHÁCH HÀNG ---")
        print("1. Thêm khách hàng\n2. Hiển thị khách hàng")
        print("3. Cập nhật khách hàng\n4. Xóa khách hàng")
        print("5. Tìm kiếm khách hàng\n0. Quay lại")
        chon = input("Lựa chọn: ").strip()
        if chon == "1":
            them_khach_hang()
        elif chon == "2":
            hien_thi_khach_hang()
        elif chon == "3":
            cap_nhat_khach_hang()
        elif chon == "4":
            xoa_khach_hang()
        elif chon == "5":
            tim_kiem_khach_hang()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def menu_ve():
    while True:
        print("\n--- QUẢN LÝ VÉ ---")
        print("1. Đặt vé\n2. Hủy vé\n3. Hiển thị vé\n4. Tìm kiếm vé\n0. Quay lại")
        chon = input("Lựa chọn: ").strip()
        if chon == "1":
            dat_ve()
        elif chon == "2":
            huy_ve()
        elif chon == "3":
            hien_thi_ve()
        elif chon == "4":
            tim_kiem_ve()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")


def tim_kiem_tong_hop():
    print("\n--- TÌM KIẾM VÀ TRA CỨU ---")
    print("1. Tìm phim\n2. Tìm suất chiếu\n3. Tìm khách hàng\n4. Tìm vé")
    chon = input("Lựa chọn: ").strip()
    if chon == "1":
        tim_kiem_phim()
    elif chon == "2":
        tim_kiem_suat_chieu()
    elif chon == "3":
        tim_kiem_khach_hang()
    elif chon == "4":
        tim_kiem_ve()
    else:
        print("Lựa chọn không hợp lệ.")


def main():
    doc_du_lieu()
    while True:
        print("\n" + "=" * 55)
        print("       CHƯƠNG TRÌNH QUẢN LÝ RẠP CHIẾU PHIM")
        print("=" * 55)
        print("1. Quản lý phim")
        print("2. Quản lý phòng chiếu")
        print("3. Quản lý suất chiếu")
        print("4. Quản lý khách hàng")
        print("5. Quản lý vé")
        print("6. Tìm kiếm và tra cứu")
        print("7. Thống kê")
        print("8. Lưu dữ liệu")
        print("9. Đọc dữ liệu")
        print("0. Thoát")
        chon = input("Lựa chọn: ").strip()

        if chon == "1":
            menu_phim()
        elif chon == "2":
            menu_phong()
        elif chon == "3":
            menu_suat_chieu()
        elif chon == "4":
            menu_khach_hang()
        elif chon == "5":
            menu_ve()
        elif chon == "6":
            tim_kiem_tong_hop()
        elif chon == "7":
            thong_ke()
        elif chon == "8":
            luu_du_lieu()
        elif chon == "9":
            doc_du_lieu()
        elif chon == "0":
            luu_du_lieu()
            print("Đã lưu dữ liệu. Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()
