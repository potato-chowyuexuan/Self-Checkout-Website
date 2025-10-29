import streamlit as st
import mylibrary as ml

import importlib
importlib.reload(ml)


# Configure the page --> sets up the browser tab title
st.set_page_config(
    page_title="EM MAH TEE",
    page_icon="🥪",
    layout="wide"
)

# Sidebar navigation
with st.sidebar:
    st.title("🚇EM MAH TEE")

    # Cart summary in sidebar
    cart_count = len(st.session_state.cart)
    cart_total = 0

    for item in st.session_state.cart:
        cart_total += item['price']

    st.markdown(f"🛒 Cart: {cart_count} items")
    if cart_count > 0:
        st.markdown(f"💰 Total: ${cart_total:.2f}")

    st.markdown("---")

    if st.button("🏠 Menu", use_container_width=True): #automatically stretch to the full width of the container it’s in (here is the sidebar)
        st.session_state.page = 'menu'
        st.rerun()

    if st.button(f"🛒 Cart ({cart_count})", use_container_width=True):
        st.session_state.page = 'cart'
        st.rerun()

    if cart_count > 0:
        if st.button("💳 Checkout", use_container_width=True):
            st.session_state.page = 'checkout'
            st.rerun()

    st.markdown("---")
    st.markdown("### Contact Us")
    st.markdown("📞 +65 9044 0813")
    st.markdown("📧 emmahtee@emt.com.sg")
    st.markdown("🕒 Mon-Sun: 11AM-5PM")



# Main content based on current page --> calling fuctions
if st.session_state.page == 'menu':
    ml.display_menu()
elif st.session_state.page == 'customize':
    ml.display_customize()
elif st.session_state.page == 'cart':
    ml.display_cart()
elif st.session_state.page == 'checkout':
    ml.display_checkout()