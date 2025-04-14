import pandas as pd
from fpdf import FPDF
import yagmail
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Create payslips directory if it doesn't exist
os.makedirs("payslips", exist_ok=True)

def read_employee_data(filepath):
    try:
        df = pd.read_excel(filepath)
        df['Net Salary'] = df['Basic Salary'] + df['Allowances'] - df['Deductions']
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def generate_payslip_pdf(row):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt=f"Payslip for {row['Name']} (ID: {row['Employee ID']})", ln=True)
        pdf.cell(200, 10, txt=f"Basic Salary: {row['Basic Salary']}", ln=True)
        pdf.cell(200, 10, txt=f"Allowances: {row['Allowances']}", ln=True)
        pdf.cell(200, 10, txt=f"Deductions: {row['Deductions']}", ln=True)
        pdf.cell(200, 10, txt=f"Net Salary: {row['Net Salary']}", ln=True)

        filename = f"payslips/{row['Employee ID']}.pdf"
        pdf.output(filename)
        return filename
    except Exception as e:
        print(f"Error generating PDF for {row['Name']}: {e}")
        return None

def send_email(to_email, name, attachment_path):
    try:
        yag = yagmail.SMTP(user="princemudete@gmail.com", password="qkty nyyg imcm omds")
        subject = "Your Payslip for This Month"
        body = f"Hi {name},\n\nPlease find your payslip attached.\n\nBest regards,\nHR Team"
        yag.send(to=to_email, subject=subject, contents=body, attachments=attachment_path)
        print(f"Email sent to {name} ({to_email})")
    except Exception as e:  
        print(f"Error sending email to {name}: {e}")

def main():
    df = read_employee_data("employees.xlsx")
    if df is None:
        return

    for _, row in df.iterrows():
        pdf_path = generate_payslip_pdf(row)
        if pdf_path:
            send_email(row["Email"], row["Name"], pdf_path)

if __name__ == "__main__":
    main()
