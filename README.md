# QR Code Generator

This Python script generates QR codes from a list of links stored in a JSON file. The generated QR codes are saved as image files in a specified output directory.

## Installation

### 1. Clone the Repository  
Clone the project repository to your local machine:

```bash
git clone https://github.com/biagolini/PythonCodeGenerator
cd PythonCodeGenerator
```

### 2. Create the Input File  
Inside the project directory, create a file named `links.json`:

```bash
touch links.json
```

Add your links to this file in the following format:

```json
{
    "Linktree": "https://linktr.ee/biagolini",
    "linkedin": "https://www.linkedin.com/in/biagolini/",
    "github": "https://github.com/biagolini",
    "medium": "https://medium.com/@biagolini"
}
```

### 3. Update pip  
Ensure your package manager is up to date:

```bash
pip install --upgrade pip
```

### 4. Set Up a Virtual Environment  
Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 5. Install Dependencies  
Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Make sure `links.json` is properly configured with the links you want to generate QR codes for.
2. Run the script:

```bash
python main.py
```

3. The script will generate QR code images and save them in the `output` folder.

## Contribution

Feel free to report issues, create pull requests, or fork the repository to improve the project.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). You are free to copy, modify, and use this project as you wish. However, any responsibility for using the code is entirely yours. Use it at your own risk.

