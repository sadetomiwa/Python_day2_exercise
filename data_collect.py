# 1) Create a program that allows a user to continue to add people to an address book until the user quits. Once the user quits, break out of the loop and print out the name and address of everyone in the address book



# def main():

#     address_book = {}

#     while True:

#         name = input("Enter a name: ")

#         if name == "":

#             break

#         address = input("Enter an address: ")

#         address_book[name] = address

#     for name, address in address_book.items():

#         print(name, address)


# main()

# Billy is trying to figure out if there is a time that he and his team can meet to work on the project. His three teammates each give him a list of times they are available ('HH:MM' 24-hour). Create a function that will take in an original list plus any number of lists of teammate's available times (*remember *args*) and return a list of times where everyone can meet.

# person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
# person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
# person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
# person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# # Available Times: '12:00' and '14:30'



# def meeting_times(*args):
    
#         available_times = []
    
#         for time in args[0]:
    
#             for person in args[1:]:
    
#                 if time not in person:
    
#                     break
    
#             else:
    
#                 available_times.append(time)
    
#         return available_times


