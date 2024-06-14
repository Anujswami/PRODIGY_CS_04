# Keylogger

This project is a simple keylogger that captures keystrokes and logs them to a file. The log file is then encrypted using AES encryption for secure storage.

## Features

- Captures keystrokes and logs them to a text file.
- Encrypts the log file using AES encryption.
- Can be configured to run for a specified number of iterations and duration.

## Requirements

- Python 3.x
- `pynput` library
- `pycryptodome` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Anujswami/PRODIGY_CS_04.git
    cd PRODIGY_CS_04
    ```

2. Install the required libraries:
    ```bash
    pip install pynput pycryptodome
    ```

## Usage

1. Modify the `keylogger.py` file to set your desired configurations:
    - `keys_information`: Name of the log file.
    - `file_path`: Path where the log file will be stored.
    - `time_iteration`: Duration for each iteration (in seconds).
    - `number_of_itration_end`: Number of iterations the keylogger will run.

2. Run the keylogger:
    ```bash
    python keylogger.py
    ```

## How It Works

1. The keylogger captures keystrokes using the `pynput` library.
2. Keystrokes are logged to a specified file.
3. After capturing keystrokes, the log file is encrypted using AES encryption.

### Code Explanation

#### Main Loop

The main loop runs until the specified number of iterations is reached. It sets up the keylogger to listen for key presses and releases.

#### Key Press Handler (`on_press`)

This function is called every time a key is pressed. It logs the key and writes it to the file when the count reaches a threshold.

#### Writing Keys to File (`write_file`)

This function writes the captured keys to a file, handling spaces and special characters appropriately.

#### Key Release Handler (`on_release`)

This function stops the keylogger when the `esc` key is pressed or the time limit for the iteration is reached.

#### Encryption

The `encrypt_data` function encrypts the log file using AES encryption, encoding the initialization vector (IV) and ciphertext in base64 for secure storage.


## Disclaimer

This software is provided for educational purposes only. Use it at your own risk. The author is not responsible for any misuse of this software.


