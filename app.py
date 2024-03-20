import streamlit as st
import pandas as pd
import requests
import pdfkit

def generate_pdf(json_url):
    try:
        # Fetch JSON data from URL
        response = requests.get(json_url)
        data = response.json()

        # Create DataFrame from JSON data
        df = pd.DataFrame(data)

        # Generate HTML report using DataFrame
        html = df.to_html()

        # Save HTML to a temporary file
        with open("temp.html", "w") as f:
            f.write(html)

        # Provide the path to wkhtmltopdf
        pdfkit.from_file("temp.html", "report.pdf", configuration=pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf'))

        st.success("PDF report generated successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("JSON to PDF Report Generator")
    
    json_url = st.text_input("Enter JSON URL:")
    if st.button("Generate PDF Report"):
        if json_url:
            generate_pdf(json_url)
        else:
            st.warning("Please enter a valid JSON URL.")

if __name__ == "__main__":
    main()
