


# def validate_input(message, input_type):
#     while True:
#         user_input = input(message).strip()
#         if input_type == "num":
#             if user_input.isdigit():
#                 return int(user_input)
#             else:
#                 print("please enter a num")
#         elif input_type == "positive_num":
#             if user_input.isdigit() and int(user_input) >= 0:
#                 return int(user_input)
#             else:
#                 print("please enter positive number")
#         elif input_type == "str":
#             if user_input.isalpha():
#                 return user_input
#             else:
#                 print("please enter a string")
#         elif input_type == "not_empty":
#             if user_input.strip():
#                 return user_input
#             else:
#                 print("error empty string")
