import tkinter as tk
import traceback
from tkinter import filedialog

from adapter.util.pdf import convert_to_proper_pdf


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        process_file(file_path)


def process_file(file_path):
    try:
        output_file_path = file_path.replace(".pdf", "-FINAL.pdf")

        convert_to_proper_pdf(file_path, output_file_path)

        result_label.config(text="PDF datoteka uspješno kreirana")
    except Exception as err:
        print(traceback.format_exc())
        result_label.config(text="Greška: " + str(err))


print("Starting Bacchus adapter")

# Create the main application window
app = tk.Tk()
app.title("Bacchus adapter")
app.geometry("300x100")

# Create a button to select a file
select_button = tk.Button(app, text="Odaberi PDF datoteku", command=select_file)
select_button.pack(pady=20)

# Label to show processing result
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.pack()

print("Bacchus adapter started!")

# Start the GUI event loop
app.mainloop()
