import PyPDF2
from datetime import datetime

# Input the path to the invoice PDF file
file = input()
# Initialize variables to store extracted data
total_charge = 0
electricity_consumed = 0
price_per_kWh = 0
time_frame = ""
time_checked = 0
result = 0
total = 0
count = 0
# Read information from the PDF file
if file!="":
    try:
        open(file, "rb")
    except FileNotFoundError:
        print(0)
        exit()
    # Handle the missing file as needed, e.g., show an error message or exit the program.
    else:
        pdf_file = PyPDF2.PdfReader(open(file, "rb"))
        page1 = pdf_file.pages[0]
        page2 = pdf_file.pages[1]
        text1 = page1.extract_text()
        text2 = page2.extract_text()
        # Split text by lines
        lines1 = text1.split("\n")
        lines2 = text2.split("\n")

        keywords = ["Elektroenerģija", "kWh", "€"]

        for line in lines2:
            if "Elektroenerģija" in line and not line.startswith("Elektroenerģija FIKSĒTAIS"):
                electricity_consumed_str = line.split("kWh")[0].strip().replace(" ", "").replace("Elektroenerģija", "").replace(",", ".")
                electricity_consumed = float(electricity_consumed_str)


                price_per_kWh_str = line.split(" ")[4].strip().replace(",", ".")
                price_per_kWh = float(price_per_kWh_str)
                try:
                    total_charge = float(line.split(" ")[5].strip().replace(",", ".").replace("Elektroenerģija", ""))
                except IndexError:
                    total_charge = float(0.00)
            
            elif " - " in line and time_checked == 0:
                parts = line.split(" - ")
                if len(parts) == 2:
                    time_frame_start = parts[0].strip().replace(".", "-")
                    time_frame_end = parts[1].strip().replace("Apjoms Mērv. Cena,","").replace(".", "-")
                    time_checked = 1
                

nordpool_rates = {}

with open("nordpool.csv", "r") as f:
    next(f)  # Skip the header line
    for line in f:
        ts_start, ts_end, price = line.strip().split(",")
        nordpool_rates[(ts_start, ts_end)] = float(price)


time_frame_start = datetime.strptime(time_frame_start, "%d-%m-%Y")
time_frame_end = datetime.strptime(time_frame_end, "%d-%m-%Y")


for (ts_start, ts_end), price in nordpool_rates.items():
    date_start = datetime.strptime(ts_start.split()[0], "%Y-%m-%d")
    date_end = datetime.strptime(ts_end.split()[0], "%Y-%m-%d")
    
    
    if time_frame_start <= date_start <= time_frame_end or time_frame_start <= date_end <= time_frame_end:
        nordpool_price = price
        total += price
        count += 1
if count == 0:
    print(0)
    exit()
nordpool_average = total/count
# varbut sis japamaina (nonemt round)
nordpool_total = round(nordpool_average, 3) * electricity_consumed
result = round(total_charge - nordpool_total, 1)
if result == 0.0:
    result = 0
print(result)
