import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
def log_error(msg):
    logging.error(msg)

def read_file(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        log_error(f"File not found: {fileName}")
        print("File not found")
    finally:
        print("File processing completed.")

