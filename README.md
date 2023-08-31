# Morse code
My first own project. I made it when I was learning Python functions. 
The program can encode English text and digits into Morse code and decode Morse code into English letters and digits back to Morse code.
## Resources
Wikipedia - Morse code
## Project structure
The data are presented in the form of two lists. The first is a list of letters and digits, the second is an indexed Morse code of letters and digits.
I use three functions, while loop, simple logic of data checking if/elif/else.

## Graphical representation
![](https://github.com/Aleshichev/code_morse/blob/main/1.png)

## Program process
1.	The program asks to confirm the start of the process (the loop will run until the user answers "No").
2.	The user must also answer whether he wants to encode or decode the data. Then enter the data. After input, the **def del_gap()** function removes extra spaces from the text.
3.	Depending on the user's choice, the entered data is encoded with  **def morze_encode()** or decoded with **def morze_decode()** . Each function outputs the corresponding result. The cycle is repeated
