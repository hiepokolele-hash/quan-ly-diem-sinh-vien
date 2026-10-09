
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Tạo dữ liệu 10 sinh viên
data = {
    "Họ và tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Văn Cường",
        "Phạm Thị Dung",
        "Hoàng Văn Em",
        "Võ Thị Hạnh",
        "Đặng Văn Khoa",
        "Bùi Thị Lan",
        "Ngô Văn Minh",
        "Phan Thị Ngọc"
    ],
    "Chuyên cần": [8.5, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.5, 6.0, 9.0],
    "Giữa kỳ":    [7.5, 8.0, 6.5, 7.0, 6.0, 9.0, 7.5, 8.0, 5.5, 8.5],
    "Cuối kỳ":    [8.0, 8.5, 7.0, 7.5, 6.5, 9.0, 7.0, 8.5, 6.0, 9.0]
}

df = pd.DataFrame(data)

# 2. Tính điểm tổng kết
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
).round(2)

# 3. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# 4. Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 5. Bảng điểm
st.subheader("Bảng điểm của 10 sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# 6. Thống kê
diem_tb = df["Tổng kết"].mean()
sv_cao_nhat = df.loc[df["Tổng kết"].idxmax()]
sv_thap_nhat = df.loc[df["Tổng kết"].idxmin()]
so_sv_dat = (df["Tổng kết"] >= 5).sum()

st.subheader("Thống kê kết quả")

cot1, cot2, cot3 = st.columns(3)
cot1.metric("Điểm trung bình", f"{diem_tb:.2f}")
cot2.metric("Điểm cao nhất", f"{sv_cao_nhat['Tổng kết']:.2f}")
cot3.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tổng kết']:.2f}")

st.write(
    f"Sinh viên cao nhất: **{sv_cao_nhat['Họ và tên']}**"
)
st.write(
    f"Sinh viên thấp nhất: **{sv_thap_nhat['Họ và tên']}**"
)
st.write(f"Số sinh viên đạt từ 5 điểm: **{so_sv_dat}**")

# 7. Chọn sinh viên
st.subheader("Tra điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Họ và tên"].tolist()
)

sv = df[df["Họ và tên"] == ten_sv].iloc[0]

st.write(f"**Họ và tên:** {sv['Họ và tên']}")
st.write(f"**Điểm chuyên cần:** {sv['Chuyên cần']:.2f}")
st.write(f"**Điểm giữa kỳ:** {sv['Giữa kỳ']:.2f}")
st.write(f"**Điểm cuối kỳ:** {sv['Cuối kỳ']:.2f}")
st.write(f"**Điểm tổng kết:** {sv['Tổng kết']:.2f}")
st.write(f"**Xếp loại:** {sv['Xếp loại']}")

# 8. Biểu đồ điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết của 10 sinh viên")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df["Họ và tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Tên sinh viên")
ax.set_xlim(0, 10)
ax.invert_yaxis()
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thông tin người tạo
st.caption("Người tạo: [Nguyễn Hoàng Hiệp] - MSSV: [042207005312]")
