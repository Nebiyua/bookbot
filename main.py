def main():
    #open the text file and read its contents
    with open("books/frankenstein.txt") as f:
        text = f.read()
        
        num_words = count_words(text)
        char_count = count_characters(text)
        char_list = convert_to_list(char_count)
        
        #Sort the list of dictionaries in descending order based on character count
        char_list.sort(reverse=True, key=sort_by_count)
        
        display_report(num_words, char_list)
        
        return text

def count_words(text):
    #Count the number of words in the text
    return len(text.split())

def count_characters(text):
    char_count = {}
    text = text.lower()
    #count the occurrences of each character in the text
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def convert_to_list(char_count):
    char_list = []

    #Convert the char_count dictionary into a list of dictionaries
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    return char_list

def sort_by_count(item):
    #Return the count value for sorting
    return item["count"]

def display_report(num_words,char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n\n")
    
    #print the character count
    for item in char_list:
        if item["char"].isalpha():
            print(f"The '{item["char"]}' character was found {item["count"]} times")

#Call the main function
main()