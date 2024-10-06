"""task 3:
This code will calculate total pixels entered by user """

#define width & height
screen_width = int(input("Enter screen width in pixels: "))
screen_height = int(input("Enter screen height in pixels: "))

#print
print(f"Resolution: {screen_width} x {screen_height}")
print(f"Total pixels: {screen_width*screen_height}")
