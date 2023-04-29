""" Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

Book - Introduction to Python Programming : Rs 499.00
Book - Python Libraries Cookbook : Rs. 855.00
Book - Data Science in Python : Rs. 645.00

Taxes and additional charges are described as details - 
GST : 12%
Delivery Charges : Rs. 250.00 """


b1=int(input("Enter number of  Introduction to Python Programming books: "))
b2=int(input("Enter number of Python Libraries Cookbook books: "))
b3=int(input("Enter number of Data Science in Python books: "))
tot=(b1*499.00)+(b2*855.00)+(b3*645.00)
gst=0.12     # gst=12%
if tot==0:
    print("Plese enter valid number of books")
else:
    tot_with_gst_del=(gst)*(tot)+250+tot
    print("Total cost: ",tot_with_gst_del)

"""
Test case 1:
Input:
    Enter number of  Introduction to Python Programming books: 1
    Enter number of Python Libraries Cookbook books: 2
    Enter number of Data Science in Python books: 0
Output:
    Total cost:  2724.08

Test case 2:
Input:
    Enter number of  Introduction to Python Programming books: 3
    Enter number of Python Libraries Cookbook books: 5
    Enter number of Data Science in Python books: 2
Output:
    Total cost:  8159.4400000000005

"""