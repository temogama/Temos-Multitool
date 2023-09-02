import zipfile
import threading

def REGZipCracker(zip_file, wordlist, num_threads):
    def check_password(start, step):
        with open(wordlist, 'r', encoding='latin-1') as wordlist_file:
            for i, password in enumerate(wordlist_file):
                if i % num_threads == start:
                    password = password.strip()
                    try:
                        with zipfile.ZipFile(zip_file, 'r') as zfile:
                            zfile.extractall(pwd=password.encode())
                        return password
                    except (RuntimeError, zipfile.BadZipFile, RuntimeError):
                        continue
        return None

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=check_password, args=(i, num_threads))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    print("Welcome to the Zip Cracker!\n")
    wordlist_file = input("Please enter the wordlist file location: ")
    zip_file = input("Please enter the zip file location: ")
    num_threads = int(input("Please enter the number of threads to use: "))

    password_found = REGZipCracker(zip_file, wordlist_file, num_threads)

    if password_found:
        print(f"\nZip file password successfully cracked! Password: {password_found}")
    else:
        print("\nZip file password not found in the wordlist. Cracking failed.")

if __name__ == "__main__":
    main()