from datetime import datetime
import humanize
import streamlit as st
from constants import CURRENCIES
from currency_converter import convert_currency, get_exchange_rate

st.title(':dollar: Currency Converter')

st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.

Enter the amount and choose the currencies to see the result.
""")

base_currency = st.selectbox(label='Base Currency: ', options=CURRENCIES)
quote_currency = st.selectbox(label='Quote Currency: ', options=CURRENCIES)

amount = st.number_input('Enter Amount: ', min_value=0.0, value=100.0)
apply = st.button('Convert')

if amount > 0 and base_currency and quote_currency and apply:
    exchange_rate, time_last_updated = get_exchange_rate(base_currency, quote_currency)
    time_diff = datetime.now() - datetime.fromtimestamp(time_last_updated)
    time_ago = humanize.naturaltime(time_diff)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f} (Last Updated: {time_ago})")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Quote Currency", value=f"{converted_amount:.2f} {quote_currency}")
    else:
        st.error('Error fetching exchange rate.')
else:
    st.info(body='Amount sohuld be greater than 0', icon='ℹ️')
