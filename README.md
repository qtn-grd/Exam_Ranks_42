# Common Core Exam Exercises

This repository contains solutions to exercises from the Common Core exams.

## 📚 Content

### Rank 02

Since Rank 02 has not changed with the introduction of the new Common Core, this section only includes exercises that I personally encountered during my exam.

### Rank 03

For Rank 03, this repository lists all exercises I have heard about so far.

⚠️ Some exercise names may be inaccurate due to limited or unofficial information.

Explanations:

<details>
<summary>anagram</summary>
<br/>

    The function normalizes both input strings by converting them to uppercase,
    ensuring a case-insensitive comparison.

    It then filters out any non-alphabetic characters, keeping only letters.

    The cleaned strings are sorted and compared.

    If they match, it means both strings contain the same characters with the same frequency,and are therefore anagrams.
</details>

<details>
<summary>bracket_validator</summary>
<br/>

    We use a stack to track opening brackets as we scan the string from left to right.

    Each time we encounter an opening bracket ((, [, {), we push it onto the stack.
    
    When we encounter a closing bracket (), ], }), we first check if the stack is empty,
    which would mean there is no matching opening bracket.

    If not empty, we compare the top element of the stack with the expected matching opening bracket.

    If they do not match, the string is invalid.
    
    Otherwise, we remove the top element from the stack, as the pair is correctly matched.

    After processing all characters, the string is valid only if the stack is empty,
    meaning all brackets were properly opened and closed in the correct order.
</details>

<details>
<summary>convert_base</summary>
<br/>

    The function converts a number from one base to another by using an intermediate base-10 representation.

    It first validates that both bases are within the allowed range (2 to 36).
    
    The input string is normalized to uppercase to handle case-insensitive digits.

    Then, it iterates through each character, converts it to its numeric value using a lookup string, and ensures it is valid for the source base.
    
    The total value is computed progressively using positional notation (multiplying the current value by the base and adding the digit).

    Once the base-10 value is obtained, the function converts it to the target base by repeatedly dividing by the target base and collecting remainders.
    These remainders correspond to digits in the new base.

    The result is built as a string, who is reversed and returned.

    If the value is zero, the function directly returns "0". Any invalid input triggers an error message.
</details>

<details>
<summary>is_palindrome</summary>
<br/>

    The function first normalizes the input string by removing all non-alphanumeric characters and converting the remaining ones to lowercase, ensuring that case and formatting do not affect the comparison.

    This is done using a generator expression combined with join, producing a cleaned version of the string.

    Once normalized, the function compares this cleaned string to its reversed version, obtained using slicing ([::-1]).
    
    If both are identical, the string reads the same forward and backward, so it is a palindrome and the function returns True.

    Otherwise, it returns False.
</details>

<details>
<summary>merge_list</summary>
<br/>

    The function combines two input lists and returns a new sorted list containing all their elements.

    It first checks whether either list is empty or None, and replaces such cases with empty lists to ensure safe concatenation.

    The two lists are then merged using list addition, creating a new list that contains all elements from both inputs.

    Finally, the sorted() function is applied to this merged list, returning a new list with elements in ascending order.
</details>

<details>
<summary>pattern_tracker</summary>
<br/>

    The function iterates through the string starting from the second character, comparing each character with its immediate predecessor.

    For each pair of adjacent characters, it first checks whether both are digits using isdigit().

    If so, it converts them to integers and verifies whether the current digit is exactly one greater than the previous one.
    
    If this condition is satisfied, the counter is incremented.

    By restricting the check to consecutive positions, the function ensures only adjacent pairs are considered.

    After processing the entire string, it returns the total count of valid digit pairs.
</details>

<details>
<summary>reverse_matrix</summary>
<br/>

    The function reverses a 2D matrix by treating it as a flattened sequence of elements.

    It first handles the edge case of an empty matrix by returning an empty list.

    Then, it determines the number of columns from the first row to preserve the original dimensions.

    The matrix is flattened into a single list using a nested comprehension, collecting all elements in row-major order.
    
    This flat list is then reversed using slicing.

    Finally, the function reconstructs a new matrix by splitting the reversed list into chunks of the original row size, appending each chunk as a new row.

    The result is a matrix with the same shape as the input, but with all elements in fully reversed order.
</details>

<details>
<summary>sculptor</summary>
<br/>

    The function transforms the input string by alternating the case of alphabetic characters while leaving non-alphabetic characters unchanged.

    It first converts the entire string to lowercase to ensure a consistent starting point.
    
    A boolean flag is used to track whether the next alphabetic character should be uppercase or lowercase, beginning with lowercase.

    As the function iterates through each character, it checks if the character is alphabetic.
    
    If not, it is added to the result unchanged and does not affect the alternation.
    
    If it is alphabetic, the function applies the appropriate case based on the flag, then toggles the flag for the next letter.
</details>

<details>
<summary>shift_alphabet</summary>
<br/>

    The function applies a shift to each alphabetic character in the string while preserving case and leaving other characters unchanged.

    It iterates through each character and checks if it is a letter.

    For alphabetic characters, it determines the correct ASCII base ('a' for lowercase, 'A' for uppercase) to maintain case consistency.

    The character’s position in the alphabet is calculated using its ASCII value, then shifted by the given amount using modular arithmetic to ensure wrap-around within the 26-letter alphabet.

    The shifted value is converted back to a character and added to the result.

    Non-alphabetic characters are appended unchanged.

    Finally, the result is joined into a string and returned.
   
</details>

<details>
<summary>sort_string</summary>
<br/>

    The function sorts a list of strings using multiple criteria combined into a single sorting key.

    It defines a set of vowels (both lowercase and uppercase) for efficient membership checks.

    The sorted() function is then used with a custom key defined by a lambda function.

    For each word, the key is a tuple containing: the number of vowels in the word (computed by iterating through its characters), the length of the word, and the word itself for lexicographical comparison.
</details>

<details>
<summary>twister</summary>
<br/>

    The function rotates a list by shifting its elements to the right by n positions while preserving order.
    
    It first handles the edge case of an empty list by returning an empty result.
    
    The value of n is normalized using modulo with the list length, ensuring that rotations larger than the list size (or negative values) are correctly handled.
    
    The rotation is performed using slicing: the last n elements are moved to the front, and the remaining elements follow.
    
    This effectively wraps elements around the list without modifying the original.
    
    The result is a new list containing the rotated elements.
</details>

## 🔄 Updates

This repository will be updated over time as I take additional exams and gather more accurate information.

The content is based on personal experience and shared information.