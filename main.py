def main():
    print(generate_report("books/frankenstein.txt"))

def generate_report(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    num_words = len(file_contents.split())

    filtered_dict = {k: v for k, v in count_symbols(file_contents).items() if k.isalpha()}
    
    sorted_dict = sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True)
    
    report = []
    report.append(f"---- Begin report of {file_path} ----")
    report.append("")
    report.append(f"{num_words} words found in a document")
    report.append("")

    for char, count in sorted_dict: 
        report.append(f"The '{char}' character was found {count} times")

    report.append("")
    report.append("---- End report ----")

    return "\n".join(report)

def count_symbols(contents):
    text = contents.lower()

    symbol_count = {}

    for char in text:
        if char in symbol_count:
            symbol_count[char] += 1
        else:
            symbol_count[char] = 1

    return symbol_count

main()