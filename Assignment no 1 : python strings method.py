# -------------------------------------------------------------
# TASK 1 & 2: Create 3 variables and take input from the user
# -------------------------------------------------------------
print("--- Please provide three different types of inputs ---")
# Variable 1: Best for testing casing, splitting, and padding methods (e.g., "  hello WORLD  ")
var1 = input("1. Enter a sentence with mixed case and spaces: ")

# Variable 2: Best for testing search, count, and replacement methods (e.g., "apple,banana,apple,cherry")
var2 = input("2. Enter a repeating, comma-separated list of items: ")

# Variable 3: Best for testing validation methods like numbers or alphabets (e.g., "12345")
var3 = input("3. Enter a specific word, number, or code: ")

print("\n" + "="*50)
# -------------------------------------------------------------
# TASK 3 & 4: Apply string methods and display outputs
# -------------------------------------------------------------

# --- Case Conversion Methods (1 to 5 & 30) ---
print("\n--- [PART 1] CASE CONVERSION METHODS ---")
print(f"Original Variable 1: '{var1}'\n")
print(f"1. upper():      {var1.upper()}")
print(f"2. lower():      {var1.lower()}")
print(f"3. title():      {var1.title()}")
print(f"4. capitalize(): {var1.capitalize()}")
print(f"5. swapcase():   {var1.swapcase()}")
print(f"30. casefold():  {var1.casefold()}  (Aggressive lower-casing for matching)")

# --- Whitespace Trimming Methods (6 to 8) ---
print("\n--- [PART 2] STRIPPING / TRIMMING METHODS ---")
print(f"Original Variable 1: '{var1}'\n")
print(f"6. strip():   '{var1.strip()}'   (Removes spaces from both sides)")
print(f"7. lstrip():  '{var1.lstrip()}'  (Removes spaces from left side)")
print(f"8. rstrip():  '{var1.rstrip()}'  (Removes spaces from right side)")

# --- Modification, Splitting & Joining Methods (9 to 11) ---
print("\n--- [PART 3] ALTERING & SPLITTING METHODS ---")
print(f"Original Variable 2: '{var2}'\n")
print(f"9. replace(): {var2.replace(',', ' | ')} (Replaced commas with pipes)")

# split() turns a string into a list
list_from_var2 = var2.split(',')
print(f"10. split():   {list_from_var2} (Split into a list by comma)")

# join() merges a list back into a string using a separator
print(f"11. join():    {' - '.join(list_from_var2)} (Joined the list back with hyphens)")

# --- Searching & Counting Methods (12 to 16) ---
print("\n--- [PART 4] SEARCHING & COUNTING METHODS ---")
print(f"Original Variable 2: '{var2}'")
search_term = input("Enter a small portion of text to look for in Variable 2: ")

print(f"\n12. find():       Index found at: {var2.find(search_term)} (-1 if not found)")
try:
    print(f"13. index():      Index found at: {var2.index(search_term)}")
except ValueError:
    print("13. index():      ValueError generated! (Substring not found)")

print(f"14. count():      Occurrences of search term: {var2.count(search_term)}")
print(f"15. startswith(): Does it start with '{search_term}'? {var2.startswith(search_term)}")
print(f"16. endswith():   Does it end with '{search_term}'? {var2.endswith(search_term)}")

# --- Character Type Validation Methods (17 to 23) ---
print("\n--- [PART 5] CHARACTER VALIDATION METHODS ---")
print(f"Original Variable 3: '{var3}'\n")
print(f"17. isalpha():  Is it alphabet letters only?   {var3.isalpha()}")
print(f"18. isdigit():  Is it digits/numbers only?     {var3.isdigit()}")
print(f"19. isalnum():  Is it alphanumeric?            {var3.isalnum()}")
print(f"20. isspace():  Is it whitespace characters only? {var3.isspace()}")
print(f"21. islower():  Are all letters lowercase?      {var3.islower()}")
print(f"22. isupper():  Are all letters uppercase?      {var3.isupper()}")
print(f"23. istitle():  Is it in Title Case format?     {var3.istitle()}")

# --- Text Formatting & Alignment Methods (24 to 27) ---
print("\n--- [PART 6] ALIGNMENT & PADDING METHODS ---")
# Using strip() first to ensure text aligns clearly without user's extra typed spaces
clean_var3 = var3.strip()
print(f"Cleaned Variable 3 base text: '{clean_var3}'\n")
print(f"24. center(): '{clean_var3.center(20)}'")
print(f"25. ljust():  '{clean_var3.ljust(20)}'")
print(f"26. rjust():  '{clean_var3.rjust(20)}'")
print(f"27. zfill():  '{clean_var3.zfill(10)}' (Pads with zeros up to 10 width)")

# --- Text Partitioning Methods (28 to 29) ---
print("\n--- [PART 7] PARTITION METHODS ---")
print(f"Original Variable 2: '{var2}'")
part_char = input("Enter a single character from Variable 2 to split on: ")

print(f"\n28. partition():  {var2.partition(part_char)} (Splits at the FIRST occurrence)")
print(f"29. rpartition(): {var2.rpartition(part_char)} (Splits at the LAST occurrence)")
print("="*50)
