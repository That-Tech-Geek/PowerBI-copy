import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Power BI-like Data Visualization Tool")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    # Read the data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Show the raw data
    st.subheader("Raw Data")
    st.write(df)

    # Select columns to visualize
    st.subheader("Select Columns for Visualization")
    x_axis = st.selectbox("Choose X-axis", df.columns)
    y_axis = st.selectbox("Choose Y-axis", df.columns)
    
    # Chart type selection
    st.subheader("Select Chart Type")
    chart_type = st.selectbox(
        "Choose a chart type",
        ["Line", "Bar", "Scatter", "Area", "Histogram", "Pie"]
    )
    
    # Generate chart based on user selection
    if chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "Scatter":
        fig = px.scatter(df, x=x_axis, y=y_axis)
    elif chart_type == "Area":
        fig = px.area(df, x=x_axis, y=y_axis)
    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis)
    elif chart_type == "Pie":
        fig = px.pie(df, names=x_axis, values=y_axis)
    
    # Display the chart
    st.subheader("Generated Chart")
    st.plotly_chart(fig)

    # Download button for filtered data
    st.subheader("Download Filtered Data")
    filtered_data = df[[x_axis, y_axis]]
    st.download_button(
        label="Download CSV",
        data=filtered_data.to_csv(index=False),
        file_name="filtered_data.csv",
        mime="text/csv"
    )
else:
    st.write("Please upload a CSV file to get started.")

# Sidebar - About
st.sidebar.header("About")
st.sidebar.info("This is a simple Streamlit application that mimics some of the basic functionalities of Power BI. "
                "You can upload your data, select columns to visualize, and generate different types of charts.")
