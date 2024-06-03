# GPT_CLI
A simple Hacky way to run ChatGPT in CLI without an API key headless

# Instructions to Install Playwright

This guide assumes you already have Python with pip installed.

## Step 1: Install Playwright

To install Playwright, run the following command:

```sh
pip install playwright
```

## Step 2:  Install Playwright Browsers:

After installing Playwright, you need to install the browsers. Run the following command:

```sh
playwright install
```

# Instructions to Run Python Script from Anywhere

## For Windows

1. Create a batch file named  `gpt.bat` with the following contents:
    
    ```sh
    @echo off
    python C:\Others\gpt_file.py %*
    ```

2. Place `gpt.bat` in a directory that is in your PATH environment variable.

3. Open Command Prompt and run your script by typing:
    
    ```sh
    gpt
    ```

## For Linux

1. Create a shell script named `gpt.sh` with the following contents:
    
    ```sh
    #!/bin/bash
    python /path/to/your/gpt_file.py "$@"
    ```

2. Make the script executable:
    
    ```sh
    chmod +x gpt.sh
    ```

3. Place `gpt.sh` in a directory that is in your PATH environment variable or run it from its location by typing:
    
    ```sh
    ./gpt.sh
    ```
