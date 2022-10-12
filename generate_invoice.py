import os

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator

from InvoiceGenerator.pdf import SimpleInvoice

# choosing English as the document language

os.environ["INVOICE_LANG"] = "en"

client = Client('Client company')

provider = Provider('Pythonbrand', bank_account='9101-4473-749392', bank_code='1384')

creator = Creator('Shreyash Mhashilkar')

invoice = Invoice(client, provider, creator)

invoice.add_item(Item(26, 200, description="chicken"))

invoice.add_item(Item(14, 380, description="bag"))

invoice.add_item(Item(10, 180, description="Rice"))

invoice.add_item(Item(3, 65, description="Biscuits"))

invoice.currency = "Rs."

invoice.number = "10242556"

docu = SimpleInvoice(invoice)

docu.gen("invoice.pdf", generate_qr_code=False)