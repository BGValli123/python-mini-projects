import streamlit as st
import pandas as pd

st.set_page_config(page_title="Smart Data Visualization Tool")

st.title("📊 Smart Data Visualization Tool")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.dataframe(df)

    columns = df.columns.tolist()

    # 🔹 Select X-axis (any column)
    x_axis = st.selectbox("Select X-axis", columns)

    # 🔹 Select only numeric columns for Y-axis
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if not numeric_cols:
        st.error("❌ No numeric columns available for visualization")
    else:
        y_axis = st.selectbox("Select Y-axis (numeric only)", numeric_cols)

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Line Chart", "Bar Chart", "Area Chart"]
        )

        st.subheader("📈 Visualization")

        # ✅ Safe plotting
        if x_axis == y_axis:
            st.warning("⚠️ X-axis and Y-axis should be different!")
        else:
            try:
                # Clean data
                data = df[[x_axis, y_axis]].dropna()

                # Set index safely
                data = data.set_index(x_axis)

                if chart_type == "Line Chart":
                    st.line_chart(data)

                elif chart_type == "Bar Chart":
                    st.bar_chart(data)

                elif chart_type == "Area Chart":
                    st.area_chart(data)

            except Exception as e:
                st.error(f"❌ Error: {e}")
