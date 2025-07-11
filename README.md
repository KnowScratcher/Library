# Library
Library - A book managing system.

<div align="center">
<img alt="page" src="https://raw.githubusercontent.com/KnowScratcher/Library/refs/heads/main/jounal_img/home.png" height="400px">

Never Lose Your Book Again!
</div>

# How to use
1. Register a book using home > register by scanning the barcode of your book
   
2. Use Borrow & Return to record where your book is.

3. Use Query to find the status of the book.

4. Edit the data using Edit.

# Install

1. Download [python3.10](https://www.python.org/downloads/)
2. git clone this repository.
3. Use the command line, cd to the project folder
4. Execute the following command using powershell or terminal depending on your operating system:
   
Windows:
```sh
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

linux / mac:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

4. Run the program using the command depending on your operating system:

Windows:
```sh
python main.py
```

linux / mac:
```sh
python3 main.py
```

5. Go to https://localhost:8002, and you will see the ui.
> [!NOTE]
> The current version only supports Chinese (traditional).