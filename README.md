# Multilingual Invoice Extractor App

## Overview

The **Multilingual Invoice Extractor** is a powerful application designed to automatically extract key information from invoices in multiple languages. Leveraging advanced Optical Character Recognition (OCR) and Natural Language Processing (NLP) technologies, this app provides a streamlined solution for extracting data such as invoice numbers, dates, amounts, and vendor information, regardless of the language or format of the invoices.

## Features

- **Multilingual Support:** Extracts data from invoices in various languages, including but not limited to English, Spanish, French, German, Chinese, and more.
- **Customizable Extraction:** Configure which fields to extract based on your specific needs, such as invoice number, issue date, total amount, line items, and more.
- **High Accuracy:** Utilizes state-of-the-art OCR and NLP models to ensure high accuracy in data extraction, even from complex or poorly scanned documents.
- **User-Friendly Interface:** Intuitive UI for easy upload and management of invoices, with visual feedback on the extraction process.
- **Export Options:** Save extracted data in multiple formats including CSV, JSON, and Excel for easy integration into other systems.

## Installation

To get started with the Multilingual Invoice Extractor, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/PynaPavani/multilingual-invoice-extractor.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd multilingual-invoice-extractor
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

## Usage

1. **Upload Invoice:** Use the file upload interface to select and upload an invoice.
2. **Configure Extraction:** Adjust settings as needed to specify the fields to extract and the languages to support.
3. **Query input:** Ask any questions based on the given invoice picture.
4. **Results:** get the result response using llm.
