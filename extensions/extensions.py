# Implement a program that prompts the user for the name of a file and then outputs that file's media type if the file's name ends,
# case-insensitively, in any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file's name ends with some other suffix or has no suffix at all, output "application/octet-stream"
# instead, which is a common default.

def main():
    # Prompt the user for the file name
    file_name = input("Enter the name of the file: ").strip()
    # Determine the media type based on the file's suffix
    if file_name.lower().endswith(('.gif', '.jpg', '.jpeg')):
        media_type = "image/jpeg"
    elif file_name.lower().endswith('.png'):
        media_type = "image/png"
    elif file_name.lower().endswith('.pdf'):
        media_type = "application/pdf"
    elif file_name.lower().endswith('.txt'):
        media_type = "text/plain"
    elif file_name.lower().endswith('.zip'):
        media_type = "application/zip"
    else:
        media_type = "application/octet-stream"
    # Output the media type
    print(media_type)   

main()