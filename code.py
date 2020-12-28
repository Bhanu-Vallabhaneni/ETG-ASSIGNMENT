from PIL import Image
import pytesseract
words = []
rows = 0
cols = 0
new=[]
flag=0

# opening the image 
image=Image.open('image.png')

#converts the image to text and save it to the output variable  
output=pytesseract.image_to_string(image)

#removing spaces at the beginning and at the end of the text
data = output.strip()

#split the text using next line as a seperator
lines = data.split('\n')

#length of the lines is number of rows in text
rows = len(lines)

#split the first line using space as a seperator and length gives number of coloumns 
cols = len(lines[0].split(' '))

#appending the text into a words array 
for line in lines:
	for word in line.split(' '):
		words.append(word)

#to  modify the elements in the array as having coloumn 1 followed by coloumn 2 and so on 		
for i  in range(0,cols):
	add=0
	for j in range(0,rows):
		k=words[i+add]
		new.append(k)
		print(k)

		add=add+cols

#enter the input to find its corresponding value on another coloumn 
find=input("enter input:  ")

#comparing the input value to elements in array 	
for i in range(0,len(new)):
	#comparing the input value to elements in text array
		if(new[i]==find):
		#if found printing the corresponding values 
		print("corresponding output:")
		print(new[i-rows])
		flag=1

#if the input is not found in the text array 
if(flag==0):
	print("input is invaild")




