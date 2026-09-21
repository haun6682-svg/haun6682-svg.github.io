# ==========================================================
# CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN
# Môn: Toán rời rạc
# Ngôn ngữ: Python
# ==========================================================

FILE_NAME = "sinhvien.txt"

# Danh sách sinh viên
danh_sach_sv = []


# ==========================================================
# 1. XẾP LOẠI SINH VIÊN
# ==========================================================

def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"


# ==========================================================
# 2. KIỂM TRA ĐIỀU KIỆN DỰ THI
# ==========================================================

def du_dieu_kien_du_thi(diem, so_buoi_vang):
    return diem >= 5 and so_buoi_vang <= 3


# ==========================================================
# 3. NHẬP ĐIỂM
# ==========================================================

def nhap_diem():
    while True:
        try:
            diem = float(input("Nhập điểm tổng kết (0 - 10): "))

            if 0 <= diem <= 10:
                return diem
            else:
                print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10.")

        except ValueError:
            print("Lỗi: Điểm phải là một số.")


# ==========================================================
# 4. NHẬP SỐ BUỔI VẮNG
# ==========================================================

def nhap_so_buoi_vang():
    while True:
        try:
            so_buoi_vang = int(input("Nhập số buổi vắng: "))

            if so_buoi_vang >= 0:
                return so_buoi_vang
            else:
                print("Lỗi: Số buổi vắng không được âm.")

        except ValueError:
            print("Lỗi: Số buổi vắng phải là số nguyên.")


# ==========================================================
# 5. THÊM SINH VIÊN
# ==========================================================

def them_sinh_vien():
    print("\n========== THÊM SINH VIÊN ==========")

    while True:
        ho_ten = input("Nhập họ và tên: ").strip()

        if ho_ten == "":
            print("Lỗi: Họ tên không được để trống.")
        else:
            break

    # Kiểm tra trùng tên
    for sv in danh_sach_sv:
        if sv["ho_ten"].lower() == ho_ten.lower():
            print("Lỗi: Sinh viên này đã tồn tại.")
            return

    diem = nhap_diem()
    so_buoi_vang = nhap_so_buoi_vang()

    sinh_vien = {
        "ho_ten": ho_ten,
        "diem": diem,
        "so_buoi_vang": so_buoi_vang
    }

    danh_sach_sv.append(sinh_vien)

    print("=> Thêm sinh viên thành công!")


# ==========================================================
# 6. HIỂN THỊ DANH SÁCH
# ==========================================================

def hien_thi_danh_sach():
    print("\n================ DANH SÁCH SINH VIÊN ================")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    print("-" * 90)

    print(
        f"{'STT':<5}"
        f"{'Họ và tên':<25}"
        f"{'Điểm':<10}"
        f"{'Vắng':<10}"
        f"{'Xếp loại':<18}"
        f"{'Dự thi':<10}"
    )

    print("-" * 90)

    for i, sv in enumerate(danh_sach_sv, start=1):

        loai = xep_loai(sv["diem"])

        if du_dieu_kien_du_thi(
            sv["diem"],
            sv["so_buoi_vang"]
        ):
            du_thi = "Đủ"
        else:
            du_thi = "Không"

        print(
            f"{i:<5}"
            f"{sv['ho_ten']:<25}"
            f"{sv['diem']:<10.2f}"
            f"{sv['so_buoi_vang']:<10}"
            f"{loai:<18}"
            f"{du_thi:<10}"
        )

    print("-" * 90)


# ==========================================================
# 7. TÌM KIẾM SINH VIÊN
# ==========================================================

def tim_sinh_vien():
    print("\n========== TÌM KIẾM SINH VIÊN ==========")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    tu_khoa = input(
        "Nhập tên sinh viên cần tìm: "
    ).strip().lower()

    if tu_khoa == "":
        print("Từ khóa tìm kiếm không được để trống.")
        return

    ket_qua = []

    for sv in danh_sach_sv:
        if tu_khoa in sv["ho_ten"].lower():
            ket_qua.append(sv)

    if len(ket_qua) == 0:
        print("Không tìm thấy sinh viên phù hợp.")
        return

    print("\n========== KẾT QUẢ TÌM KIẾM ==========")

    print("-" * 90)

    print(
        f"{'STT':<5}"
        f"{'Họ và tên':<25}"
        f"{'Điểm':<10}"
        f"{'Vắng':<10}"
        f"{'Xếp loại':<18}"
        f"{'Dự thi':<10}"
    )

    print("-" * 90)

    for i, sv in enumerate(ket_qua, start=1):

        loai = xep_loai(sv["diem"])

        if du_dieu_kien_du_thi(
            sv["diem"],
            sv["so_buoi_vang"]
        ):
            du_thi = "Đủ"
        else:
            du_thi = "Không"

        print(
            f"{i:<5}"
            f"{sv['ho_ten']:<25}"
            f"{sv['diem']:<10.2f}"
            f"{sv['so_buoi_vang']:<10}"
            f"{loai:<18}"
            f"{du_thi:<10}"
        )

    print("-" * 90)


# ==========================================================
# 8. CẬP NHẬT SINH VIÊN
# ==========================================================

def cap_nhat_sinh_vien():
    print("\n========== CẬP NHẬT SINH VIÊN ==========")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    ten_can_sua = input(
        "Nhập tên sinh viên cần cập nhật: "
    ).strip()

    for sv in danh_sach_sv:

        if sv["ho_ten"].lower() == ten_can_sua.lower():

            print("\n--- THÔNG TIN HIỆN TẠI ---")
            print("Họ tên:", sv["ho_ten"])
            print("Điểm:", sv["diem"])
            print("Số buổi vắng:", sv["so_buoi_vang"])

            print("\n--- NHẬP THÔNG TIN MỚI ---")

            while True:
                ho_ten_moi = input(
                    "Nhập họ và tên mới: "
                ).strip()

                if ho_ten_moi != "":
                    break

                print("Lỗi: Họ tên không được để trống.")

            diem_moi = nhap_diem()

            vang_moi = nhap_so_buoi_vang()

            sv["ho_ten"] = ho_ten_moi
            sv["diem"] = diem_moi
            sv["so_buoi_vang"] = vang_moi

            print("=> Cập nhật sinh viên thành công!")
            return

    print("Không tìm thấy sinh viên cần cập nhật.")


# ==========================================================
# 9. XÓA SINH VIÊN
# ==========================================================

def xoa_sinh_vien():
    print("\n========== XÓA SINH VIÊN ==========")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    ten_can_xoa = input(
        "Nhập tên sinh viên cần xóa: "
    ).strip()

    for sv in danh_sach_sv:

        if sv["ho_ten"].lower() == ten_can_xoa.lower():

            xac_nhan = input(
                "Bạn có chắc chắn muốn xóa? (y/n): "
            ).strip().lower()

            if xac_nhan == "y":
                danh_sach_sv.remove(sv)
                print("=> Xóa sinh viên thành công!")
            else:
                print("=> Đã hủy thao tác xóa.")

            return

    print("Không tìm thấy sinh viên cần xóa.")


# ==========================================================
# 10. SẮP XẾP SINH VIÊN
# ==========================================================

def sap_xep_sinh_vien():
    print("\n========== SẮP XẾP SINH VIÊN ==========")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    danh_sach_sv.sort(
        key=lambda sv: sv["diem"],
        reverse=True
    )

    print("=> Đã sắp xếp theo điểm giảm dần.")

    hien_thi_danh_sach()


# ==========================================================
# 11. THỐNG KÊ SINH VIÊN
# ==========================================================

def thong_ke():
    print("\n========== THỐNG KÊ SINH VIÊN ==========")

    if len(danh_sach_sv) == 0:
        print("Danh sách sinh viên đang trống.")
        return

    tong_so = len(danh_sach_sv)

    tong_diem = sum(
        sv["diem"] for sv in danh_sach_sv
    )

    diem_trung_binh = tong_diem / tong_so

    so_gioi = 0
    so_kha = 0
    so_trung_binh = 0
    so_yeu = 0

    so_du_thi = 0
    so_khong_du_thi = 0

    for sv in danh_sach_sv:

        loai = xep_loai(sv["diem"])

        if loai == "Giỏi":
            so_gioi += 1

        elif loai == "Khá":
            so_kha += 1

        elif loai == "Trung bình":
            so_trung_binh += 1

        else:
            so_yeu += 1

        if du_dieu_kien_du_thi(
            sv["diem"],
            sv["so_buoi_vang"]
        ):
            so_du_thi += 1
        else:
            so_khong_du_thi += 1

    print("\n--- KẾT QUẢ THỐNG KÊ ---")

    print("Tổng số sinh viên:", tong_so)

    print(
        f"Điểm trung bình: {diem_trung_binh:.2f}"
    )

    print("\n--- XẾP LOẠI ---")
    print("Giỏi:", so_gioi)
    print("Khá:", so_kha)
    print("Trung bình:", so_trung_binh)
    print("Yếu:", so_yeu)

    print("\n--- ĐIỀU KIỆN DỰ THI ---")
    print(
        "Đủ điều kiện dự thi:",
        so_du_thi
    )

    print(
        "Không đủ điều kiện dự thi:",
        so_khong_du_thi
    )


# ==========================================================
# 12. LƯU DỮ LIỆU VÀO FILE TXT
# ==========================================================

def luu_file():

    try:

        with open(
            FILE_NAME,
            "w",
            encoding="utf-8"
        ) as file:

            for sv in danh_sach_sv:

                file.write(
                    f"{sv['ho_ten']}|"
                    f"{sv['diem']}|"
                    f"{sv['so_buoi_vang']}\n"
                )

        print(
            "=> Đã lưu dữ liệu vào file:",
            FILE_NAME
        )

    except Exception as e:

        print(
            "Lỗi khi lưu file:",
            e
        )


# ==========================================================
# 13. ĐỌC DỮ LIỆU TỪ FILE TXT
# ==========================================================

def doc_file():

    global danh_sach_sv

    try:

        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:

            danh_sach_sv.clear()

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                ho_ten = parts[0]

                diem = float(parts[1])

                so_buoi_vang = int(parts[2])

                sinh_vien = {
                    "ho_ten": ho_ten,
                    "diem": diem,
                    "so_buoi_vang": so_buoi_vang
                }

                danh_sach_sv.append(
                    sinh_vien
                )

        print(
            "=> Đã đọc dữ liệu từ file thành công."
        )

    except FileNotFoundError:

        print(
            "Chưa có file dữ liệu."
        )

        print(
            "Chương trình sẽ bắt đầu với danh sách rỗng."
        )

    except ValueError:

        print(
            "Lỗi: Dữ liệu trong file không hợp lệ."
        )

    except Exception as e:

        print(
            "Lỗi khi đọc file:",
            e
        )


# ==========================================================
# 14. HIỂN THỊ MENU
# ==========================================================

def hien_thi_menu():

    print("\n")

    print("=" * 60)

    print(
        "           CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN"
    )

    print("=" * 60)

    print("1. Thêm sinh viên")

    print("2. Hiển thị danh sách sinh viên")

    print("3. Cập nhật sinh viên")

    print("4. Xóa sinh viên")

    print("5. Tìm kiếm sinh viên")

    print("6. Sắp xếp sinh viên theo điểm")

    print("7. Thống kê sinh viên")

    print("8. Lưu dữ liệu vào file")

    print("9. Đọc dữ liệu từ file")

    print("0. Thoát")

    print("=" * 60)


# ==========================================================
# 15. CHƯƠNG TRÌNH CHÍNH
# ==========================================================

def main():

    # Đọc dữ liệu cũ khi khởi động
    doc_file()

    while True:

        hien_thi_menu()

        lua_chon = input(
            "Nhập lựa chọn của bạn: "
        ).strip()

        if lua_chon == "1":

            them_sinh_vien()

        elif lua_chon == "2":

            hien_thi_danh_sach()

        elif lua_chon == "3":

            cap_nhat_sinh_vien()

        elif lua_chon == "4":

            xoa_sinh_vien()

        elif lua_chon == "5":

            tim_sinh_vien()

        elif lua_chon == "6":

            sap_xep_sinh_vien()

        elif lua_chon == "7":

            thong_ke()

        elif lua_chon == "8":

            luu_file()

        elif lua_chon == "9":

            doc_file()

        elif lua_chon == "0":

            print("\nĐang lưu dữ liệu trước khi thoát...")

            luu_file()

            print("Chương trình kết thúc.")

            break

        else:

            print(
                "Lỗi: Lựa chọn không hợp lệ."
            )

            print(
                "Vui lòng chọn từ 0 đến 9."
            )


# ==========================================================
# CHẠY CHƯƠNG TRÌNH
# ==========================================================

if __name__ == "__main__":
    main()