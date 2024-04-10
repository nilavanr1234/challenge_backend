import PyPDF2
import tabula
import json
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text


def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    return tables


def convert_tables_to_json(tables):
    json_data = []
    for table in tables:
        table_json = table.to_dict(orient="records")
        json_data.append(table_json)
    return json_data


def main(pdf_path, output_path):
    # TODO: Extract text from PDF
    extracted_text = extract_text_from_pdf("input.pdf")

    # TODO: Extract tables from PDF
    extracted_tables = extract_tables_from_pdf("input.pdf")

    # TODO: Convert tables to JSON
    tables_json = convert_tables_to_json("input.pdf")

    # TODO: Create dictionary with text and tables data
    data = {
        "text": extracted_text,
        "tables": tables_json
    }

    # TODO: Save data to JSON file
    with open(output_path, "w") as outfile:
        json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    # Specify input PDF path and output JSON path
    pdf_path = "input.pdf"  # Update with the path to your input PDF file
    output_path = "result.json" # Update with desired output JSON file path
    main(pdf_path, output_path)

