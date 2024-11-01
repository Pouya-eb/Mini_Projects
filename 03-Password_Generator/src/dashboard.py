import streamlit as st
from password_generator import PinCodeGenerator, RandomPasswordGenerator, MemorablePasswordGenerator

st.title(':lock: Password Generator')

option = st.radio(
                  label='Password Type', 
                  options=['Pin Code', 'Random Password', 'Memorable Password'],
                  )

if option == 'Pin Code':
    length = st.slider(
                       label='Length',
                       min_value=8, 
                       max_value=32, 
                       value=16,
                       )
    generator = PinCodeGenerator(length=length)

elif option == 'Random Password':
    length = st.slider(
                       label='Length', 
                       min_value=8, 
                       max_value=32, 
                       value=16,
                       )
    include_numbers = st.toggle('Include Numbers')
    include_symbols = st.toggle('Include Symbols')

    generator = RandomPasswordGenerator(
                                        length=length, 
                                        include_numbers=include_numbers, 
                                        include_symbols=include_symbols,
                                        )
    
else:
    no_of_words = st.slider(
                            label='Number of Words', 
                            min_value=4, 
                            max_value=16, 
                            value=4,
                            ) 
    capitalization = st.toggle('Capitalization')
    separator = st.text_input('Separator', value='-')
   
    generator = MemorablePasswordGenerator(
                                           no_of_words=no_of_words, 
                                           sep=separator, 
                                           capitalization=capitalization,
                                           )

password = generator.generate()
st.write(fr'Your {option} is:')
st.code(fr'{password}')