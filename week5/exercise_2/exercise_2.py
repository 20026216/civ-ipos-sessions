def main():
        # Phase 1: File Navigation
    with open ("data.bin", "rb") as file:
        file.seek(5)
        bytes_data = file.read()
        print(bytes_data)
            # Navigate to the 5th byte position

            # Read and print the next 4 bytes from the current position
        next_four_bytes = bytes_data[1:5]
        print(next_four_bytes)

            # Move the file pointer to the beginning of the file
        file.seek(0)
        bytes_data = file.read()
        print(bytes_data)
            # Read and print the first 8 bytes from the file
        first_eight_bytes = bytes_data[0:7].decode("utf-8")
        print(first_eight_bytes)


            # Print the current file pointer position
        current_pointer = file.tell()
        print (current_pointer)


            # Use the find() method to search for the string "ABC" in the file







        # Re-open the data.bin file in binary write-append mode

            # Use the tell() method to get the current file pointer position and store it as a bookmark


            # Write the string "XYZ" to the file


            # Use the bookmarked pointer position to append the string "123" to the file

    # create three non naked exception handlers for: 
    # not finding the file, i/o error & all other exceptions


if __name__ == "__main__":
    main()
