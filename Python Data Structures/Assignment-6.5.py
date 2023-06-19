'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475"
# Slicing the string to get a peice starts from the index of 0 to the end of the string
num = text[text.find('0'):]
num = float(num)
print(num)
