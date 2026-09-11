from openpyxl import load_workbook
import pandas as pd
import logging
from pathlib import Path
from openpyxl.styles import PatternFill,Font,Alignment

#Creating Path for the file

INPUT_FILES = [
    "Sales_file1.xlsx",
    "Sales_file2.xlsx",
    "Sales_file3.xlsx"
]

BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR.parent / "sample_data"
OUTPUT_DIR = BASE_DIR / "output"
LOG_DIR = BASE_DIR / "logs"

OUTPUT_FILE = OUTPUT_DIR / "master_sales.xlsx"
LOG_FILE = LOG_DIR / "excel_consolidator.log"

#Setup logging modules

def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Excel Consolidator Bot started")

# Access the input files

def get_input_files():

    files = []

    if not INPUT_DIR.exists():
        raise FileNotFoundError(
            f"Input directory not found: {INPUT_DIR}"
        )

    for filename in INPUT_FILES:

        file_path = INPUT_DIR / filename

        if file_path.exists():
            files.append(file_path)
            logging.info("Found required file: %s", filename)

        else:
            logging.warning("File not found: %s", filename)

    if not files:
        raise FileNotFoundError(
            f"No required Excel files found in: {INPUT_DIR}"
        )

    logging.info("Found %d required Excel files", len(files))

    return files

# Read the excel files 

def read_excel_files(files):
    dataframes = []

    for file in files:
        logging.info("Reading file: %s", file.name)

        df = pd.read_excel(file)

        df["Source File"] = file.name

        dataframes.append(df)

    return dataframes

#Combine all the data's from all files

def combine_data(dataframes):

    if not dataframes:
        raise ValueError("No Excel files were found to combine.")

    combined_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    return combined_df

#Remove the duplicate files from the combined file

def remove_duplicates(df):
    before_count = len(df)

    df = df.drop_duplicates(
        subset=["Sale ID"],
        keep="first"
    )

    after_count = len(df)

    duplicates_removed = before_count - after_count

    logging.info(
        "Duplicate records removed: %d",
        duplicates_removed
    )

    return df, duplicates_removed

# Create summary for all files

def create_summary(df, file_count, records_before, duplicates_removed):
    summary = {
        "Total Input Files": file_count,
        "Total Records Before Duplicate Removal": records_before,
        "Duplicate Records Removed": duplicates_removed,
        "Final Records": len(df),
        "Total Sales Amount": df["Amount"].sum()
    }

    summary_df = pd.DataFrame(
        summary.items(),
        columns=["Metric", "Value"]
    )

    return summary_df

# Save the updated file in new master file

def save_master_file(df, summary_df, product_summary):
    OUTPUT_DIR.mkdir(exist_ok=True)

    with pd.ExcelWriter(
        OUTPUT_FILE,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            sheet_name="Sales Data",
            index=False
        )

        summary_df.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

        product_summary.to_excel(
            writer,
            sheet_name="Product Summary",
            index=False
        )

    logging.info(
        "Master workbook created: %s",
        OUTPUT_FILE

    )

# Format the excel based on the font and its alignment

def format_excel():
    wb = load_workbook(OUTPUT_FILE)

    for ws in wb.worksheets:

        for cell in ws[1]:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(
                horizontal="center"
            )

        ws.freeze_panes = "A2"

        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                if cell.value is not None:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            ws.column_dimensions[
                column_letter
            ].width = max_length + 2

    wb.save(OUTPUT_FILE)

    logging.info("Excel formatting completed")



def main():

    try:
        setup_logging()

        files = get_input_files()

        dataframes = read_excel_files(files)

        combined_df = combine_data(dataframes)

        records_before = len(combined_df)

        cleaned_df, duplicates_removed = remove_duplicates(
            combined_df
        )

        summary_df = create_summary(
            cleaned_df,
            len(files),
            records_before,
            duplicates_removed
        )

        product_summary = (
            cleaned_df.groupby("Product")["Amount"]
            .sum()
            .reset_index()
        )

        save_master_file(
            cleaned_df,
            summary_df,
            product_summary
        )

        format_excel()

        logging.info(
            "Excel Consolidator Bot completed successfully"
        )

    except Exception as e:

        logging.exception(
            "Bot failed: %s", e
        )

    finally:

        logging.info(
            "Excel Consolidator Bot execution finished"
        )


if __name__ == "__main__":
    main()