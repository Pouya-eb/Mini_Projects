import streamlit as st
from contact_book import ContactBook, contacts

st.title(':book:  Contact Book')
option = st.radio(
                   label='Contact Book', 
                   options=['Add Contact', 'Update Contact', 'Delete Contact', 'Show Contact'],
                   label_visibility='hidden',
                   )

if option == 'Add Contact':
    name = st.text_input(label=f'Name :red[*]', value=None)
    phone = st.text_input(label=f'Phone :red[*]', value=None)
    email = st.text_input(label='Email (Optional)', value=None)
    apply = st.button(label='Apply')

    if apply:
        if name and phone:
            message = contacts.add_contact(name=name, phone=phone, email=email)
            if message == 'The contact is added successfully':
                st.markdown(f':green-background[{message}]')
            else:
                st.markdown(f':blue-background[{message}]')
        else:
            st.markdown(f':red-background[Please make sure you have filled in **Name** and **Phone**]')


elif option == 'Update Contact':
    name = st.text_input(label=f'Name :red[*]', value=None)
    new_phone = st.text_input(label='New Phone', value=None)
    new_email = st.text_input(label='New Email', value=None)
    apply = st.button(label='Apply')

    if apply:
        if name and (new_phone or new_email):
            message = contacts.update_contact(name=name, phone=new_phone, email=new_email)
            if message == 'Contact is updated successfully':
                st.markdown(f':green-background[{message}]')
            else:
                st.markdown(f':blue-background[{message}]')
        else:
            st.markdown(f':red-background[Please make sure you have filled in **Name** and **Phone**/**Email**]')

elif option == 'Delete Contact':
    name = st.text_input(label=f'Name :red[*]', value=None)
    apply = st.button(label='Apply')

    if apply:
        if name:
            message = contacts.delete_contact(name=name)
            if message == 'Contact is deleted successfully':
                st.markdown(f':green-background[{message}]')
            else:
                st.markdown(f':blue-background[{message}]')
        else:
            st.markdown(f':red-background[Please make sure you have filled in **Name**]')


elif option == 'Show Contact':
    pass



