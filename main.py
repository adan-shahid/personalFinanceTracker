import pandas as pd
import csv
from datetime import datetime
from data_Entry import get_amount, get_category, get_date, get_description


FORMAT= "%d-%m-%Y"
class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

#INITIALIZING THE CSV FILE

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])
            df.to_csv(cls.CSV_FILE, index=False)

#ADDING THE ENTRY

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description,
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile: # context manager
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    @classmethod
    def get_transactios(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_file)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strftime(start_date, CSV.FORMAT)
        end_date = datetime.strftime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & df["date"] <= end_date
        filtered_df = df.loc[mask]


        if filtered_df.empty:
            print("No transaction found in the given range.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
                  )
            print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT) })

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or enter for today's date ", allow_default=True)

    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


#CSV.initialize_csv()
#CSV.add_entry("20-07-2-25", 125.65, "Income", "Salary" )

add()
        

