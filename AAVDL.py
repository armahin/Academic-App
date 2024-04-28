import streamlit as st

def analysis(total_length, udl):
    DH = total_length
    load_per_ft = udl
    dh = DH - 2 * (DH * 0.1)
    Dd = Hh = (DH) * 0.1
    d = h = (load_per_ft * dh) / 2
    D = H = d + DH * 0.1 * load_per_ft
    Md = Mh = d * DH * 0.1 + load_per_ft * Dd * Dd / 2
    return {
        "Reaction Left": D,
        "Reaction Right": H,
        "Moment Left": Md,
        "Moment Right": Mh
    }

def main():
    st.title("Approx Analysis of Vertical DL")

    total_length = st.number_input("Total Length:", value=20.0, step=0.1)
    udl = st.number_input("UDL:", value=10.0, step=0.1)

    if st.button("Analyze"):
        results = analysis(total_length, udl)
        st.write("### Results:")
        for key, value in results.items():
            st.write(f"- {key}: {value}")

if __name__ == "__main__":
    main()
