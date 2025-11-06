def extract_domain(email):
    """
    Extract the domain from an email address.
    
    Args:
        email: A string containing an email address
        
    Returns:
        The domain part of the email address, or None if invalid
    """
    if '@' in email:
        parts = email.split('@')
        if len(parts) == 2:
            return parts[1].strip()
    return None


def count_emails_from_domain(filename, target_domain):
    """
    Count how many emails in the archive are from the specified domain.
    
    Args:
        filename: The name of the email archive file
        target_domain: The domain to search for
        
    Returns:
        The count of emails from that domain
    """
    count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Look for lines that start with "From: "
                if line.startswith('From: '):
                    # Extract the email address (everything after "From: ")
                    email = line[6:].strip()
                    
                    # Extract the domain from the email
                    domain = extract_domain(email)
                    
                    # Check if it matches the target domain
                    if domain == target_domain:
                        count += 1
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    
    return count


def main():
    """
    Main function to run the email domain counter program.
    """
    # Get the filename from the user
    filename = input("Enter the filename for the email archive: ")
    
    # Get the domain to search for
    domain = input("Enter the domain: ")
    
    # Count emails from that domain
    count = count_emails_from_domain(filename, domain)
    
    # Display the result
    if count >= 0:
        print(f"There are {count} emails from {domain}.")


if __name__ == "__main__":
    main()