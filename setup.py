from colorama import Fore, Style

def get_user_choice():
    while True:
        choice = input(f"{Fore.CYAN}Do you want to add to existing documents (a) or overwrite them (o)? {Style.RESET_ALL}").lower()
        if choice in ('a', 'o'):
            return choice
        print(f"{Fore.RED}Invalid choice. Please enter 'a' or 'o' for 'add' or 'overwrite' respectively.{Style.RESET_ALL}")

def get_documents():
    documents = []
    while True:
        title = input(f"{Fore.YELLOW}>{Fore.WHITE} Enter document title (or 'done' to finish): {Style.RESET_ALL}")
        if title.lower() == 'done':
            break
        content = input(f"{Fore.YELLOW}>{Fore.WHITE}Enter document content: {Style.RESET_ALL}")
        documents.append(f"\n## Title: \"{title}\"\nContent: {content}\n")
    return "\n".join(documents)

def save_to_file(documents, mode='w'):
    with open("documents.txt", mode) as file:
        file.write(documents)

def main():
    choice = get_user_choice()

    if choice == 'a':
        existing_documents = ""
        try:
            with open("documents.txt", 'r') as file:
                existing_documents = file.read()
        except FileNotFoundError:
            pass

        documents_to_add = get_documents()
        all_documents = existing_documents + documents_to_add
        save_to_file(all_documents)
        print(f"{Fore.GREEN}Documents added successfully.{Style.RESET_ALL}")

    elif choice == 'o':
        documents_to_overwrite = get_documents()
        save_to_file(documents_to_overwrite, mode='w')
        print(f"{Fore.GREEN}Documents overwritten successfully.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
