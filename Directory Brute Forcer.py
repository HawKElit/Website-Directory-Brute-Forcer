import requests
website_url = input("Enter the website you want to brute force:")
print(f"Scanning for directories at {website_url}...")
with open("Directories_Common.wordlist") as file:
    for line in file:
        directory_word = (f"{website_url}/{line.strip()}")
        responce = requests.get(directory_word)
        status_code = responce.status_code
        if status_code == 200:
            print(f"Url Found at {directory_word}!")
print(f"Scan complete.")
