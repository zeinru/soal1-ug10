def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        line1 = lines1[i].strip() if i < len(lines1) else "[BARIS TIDAK ADA]"
        line2 = lines2[i].strip() if i < len(lines2) else "[BARIS TIDAK ADA]"

        if line1 != line2:
            print(f"\nPerbedaan pada baris {i+1}:")
            print(f"File 1: {line1}")
            print(f"File 2: {line2}")

compare_files('file1.txt', 'file2.txt')
