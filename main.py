# a = (input("what is your name?"))
# b = (input("who is your crush?"))
# c= int(input("how old is she?"))
# length_1 = len(a)
# length_2 = len(b)
# if (length_1 + length_2 + c) % 2 == 0:
#     print("you both are compatible with each other")
# else:
#     print("sorry! you are not compatible.")

import streamlit as st

def compatibility_check(a, b, c):
    length_1 = len(a)
    length_2 = len(b)

    if (length_1 + length_2 + c) % 2 == 0:
        return "You both are compatible with each other!"
    else:
        return "Sorry! You are not compatible."

def main():
    st.title("Compatibility Checker")

    name = st.text_input("What is your name?")
    crush_name = st.text_input("Who is your friend?")
    crush_age = st.number_input("How old is your friend?", min_value=0, max_value=150, value=18)

    if st.button("Check Compatibility"):
        if name and crush_name:
            result = compatibility_check(name, crush_name, crush_age)
            st.write(result)
        else:
            st.warning("Please enter both names!")

if __name__ == "__main__":
    main()










