#Create a function that takes a list of number as input and returns the sum of those numbers
def sum_numbers(numbers):
    total=0
    for number in numbers:
        total+=number
    return total
number_list= [1,2,3,4,5,6]
print(sum_numbers(number_list))
#Write a function  that takes a string as input and returns a number of vowels in that string
def vowel(vowels):
    vowel="aeiou"
    count=0
    for letters in vowels:
        if letters.lower() in vowel:
            count+=1
    return count
word = "esther"
print(vowel(word))

