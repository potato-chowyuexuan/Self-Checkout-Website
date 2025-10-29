import streamlit as st
import re

# Initialize session state
#session_state act like an object and dictionary
#https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state --> store variable between reruns
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'current_sandwich' not in st.session_state:
    st.session_state.current_sandwich = None
if 'page' not in st.session_state:
    st.session_state.page = 'menu'

#Image(copy image file path and paste here)
logo = "/content/logo image file.png"

 #Menu
 #each sandwich name maps to another dict
SANDWICHES = {
      "KIASU KING": {
          "6inch_price": 7.20,
          "footlong_price": 12.90,
          "calories": 325,
          "description": "“Add everything lor!”: A fully loaded roast beef and turkey ham sandwich.",
          "image": "🦃🥩🍅"
      },
      "BLUR SOTONG": {
          "6inch_price": 6.50,
          "footlong_price": 11.70,
          "calories": 474,
          "description": "Slightly messy lah but still loveable: An egg mayo sandwich that’s slightly overflowing, like a sotong blur-blur one.",
          "image": "🥚🧀🍅"
      },
      "BOJIO BITE": {
          "6inch_price": 7.99,
          "footlong_price": 14.50,
          "calories": 571,
          "description": "A must-try signature grilled cheesy chicken chop sandwich that will make your kakis say “Eh, bojio!”",
          "image": "🍗🧀🥬"
      },
      "STEADY POM PI PI": {
          "6inch_price": 7.90,
          "footlong_price": 14.20,
          "calories": 324,
          "description": "“Damn solid eh!”: A hearty roast turkey sandwich that never disappoints.",
          "image": "🍖🧀❤️"
      },
      "SHIOK SIOL": {
          "6inch_price": 8.70,
          "footlong_price": 15.60,
          "calories": 420,
          "description": "Bursting with flavor: A spicy sambal chicken sandwich that makes you go “Wah, shiok!”, making you feel like you’re in a fast food commercial with wind blowing in your hair.",
          "image": "🍗🌶️🤩"
      },
      "SIAO LIAO": {
          "6inch_price": 8.70,
          "footlong_price": 15.60,
          "calories": 378,
          "description": "“Can tahan or not?”:A fiery chilli beef sandwich that might make your eyes water. (warning: not for the weak!)",
          "image": "🥩🌶️🔥"
      },
      "ANYTHING LOR": {
          "6inch_price": 6.90,
          "footlong_price": 12.40,
          "calories": 352,
          "description": "“What to eat ah?”: A simple but satisfying ham and cheese melt sandwich that you can’t go wrong with.",
          "image": "🥩🧀😋"
      },
      "KU-OO": {
          "6inch_price": 6.50,
          "footlong_price": 11.70,
          "calories": 472,
          "description": "A breakfast-style sandwich with egg, sausage, and cheese that even the morning birds will fight for.",
          "image": "🥚🧀🐦"
      },
      "LEPAK DELUXE": {
          "6inch_price": 6.90,
          "footlong_price": 12.40,
          "calories": 388,
          "description": "“Relax leh!”: A laid back cold cut sandwich, perfect for chilling.",
          "image": "🥩🧀😎"
      }

  }

#list of customization
BREAD_OPTIONS = ["White", "Whole Wheat", "Sourdough", "Rye", "Ciabatta", "Pita"]
SIZE_OPTIONS = ["6-inch", "Footlong"]
VEGETABLES = ["Lettuce", "Tomato", "Onion", "Cucumber", "Bell Pepper", "Spinach", "Avocado", "Pickles"]
CONDIMENTS = ["Mayo", "Mustard", "Ketchup", "Ranch", "Italian Dressing", "Olive Oil", "Hot Sauce"]


def display_menu():
    # Create 2 columns: left is title, middle empty, right for logo
    col1, col2, col3 = st.columns([4, 3, 3])  # adjust ratio depending on spacing

    with col1:
      st.write("")  # empty line
      st.write("")
      st.write("")
      st.write("")
      st.write("")
      st.title("EM MAH TEE") #title in left column

    with col2:
      st.empty()  # nothing in middle column

    with col3:
      st.image(logo, width = 300)  # logo in top-right

    st.markdown("# MENU") #markdown allows markdown syntax --> formatted text diff from write
    st.markdown("### Welcome! Choose your favorite sandwich") # "#"is for the front size, more the # smaller the size


    # Display sandwiches in 3 columns
    cols = st.columns(3)
    count = 0


    for name, details in SANDWICHES.items():
        col = cols[count % 3]

        with col: # "with" means "inside it"
          with st.container(height = 400): #groups the sandwich info in a fixed-height box
            st.markdown(f"### {details['image']} {name}")
            st.markdown(f"**6-inch ${details['6inch_price']:.2f}**")
            st.markdown(f"**Footlong ${details['footlong_price']:.2f}**")
            st.markdown(f"*{details['calories']} calories*")
            st.markdown(details['description'])

            if st.button(f"➕", key=f"order_{name}"): #No two buttons have the same key
                st.session_state.current_sandwich = {
                    'name': name,
                    '6inch_price': details['6inch_price'],
                    'footlong_price': details['footlong_price'],
                    'calories': details['calories']
                }
                st.session_state.page = 'customize' #change page
                st.rerun() #refresh immediately to show new page
        count += 1






def display_customize():
    if st.session_state.current_sandwich is None:
        st.session_state.page = 'menu'
        st.rerun()

    sandwich = st.session_state.current_sandwich

    st.title(f"🍴 Customize your {sandwich['name']} sandwich!")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Bread selection
        st.subheader("🍞 Choose your bread:")
        bread = st.selectbox("Bread type", BREAD_OPTIONS)

        # Size selection
        st.subheader("📏 Choose your size:")
        size = st.selectbox("Size", SIZE_OPTIONS)

        # Vegetables selection
        st.subheader("🥬 Choose your vegetables:")
        vegetables = st.multiselect("Vegetables (select multiple)", VEGETABLES) #return list

        # Condiments selection
        st.subheader("🥫 Choose your condiments:")
        condiments = st.multiselect("Condiments (select up to 2)", CONDIMENTS, max_selections = 2)

        # Special instructions
        st.subheader("📝 Special instructions:")
        special_instructions = st.text_area("Any special requests?", height=100)

    with col2:
        st.subheader("📋 Order Summary")
        st.markdown(f"**Sandwich:** {sandwich['name']}")
        st.markdown(f"**Size:** {size}")

        if size == "6-inch":
            st.markdown(f"**Price:** ${sandwich['6inch_price']:.2f}")
        else:
            st.markdown(f"**Price:** ${sandwich['footlong_price']:.2f}")

        st.markdown(f"**Calories:** {sandwich['calories']}")
        st.markdown(f"**Bread:** {bread}")


        if vegetables:
            st.markdown(f"**Vegetables:** {', '.join(vegetables)}") #join elements in the list to a string
        if condiments:
            st.markdown(f"**Condiments:** {', '.join(condiments)}")

        st.markdown(f"**Special instructions:** {special_instructions}")

        st.markdown("---")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🛒 Add to Cart"):
                if size == "6-inch":
                    selected_price = sandwich['6inch_price']
                else:
                    selected_price = sandwich['footlong_price']

                cart_item = {
                    'name': sandwich['name'],
                    'size': size,
                    'price': selected_price,
                    'calories': sandwich['calories'],
                    'bread': bread,
                    'vegetables': vegetables,
                    'condiments': condiments,
                    'special_instructions': special_instructions,
                }
                st.session_state.cart.append(cart_item) #add dictionary cart_item into empty/cart list
                st.success("Added to cart!") #when command successfully executes, popup message appear
                st.session_state.page = 'menu'
                st.rerun()

        with col_btn2:
            if st.button("← Back to Menu"):
                st.session_state.page = 'menu'
                st.rerun()




def display_cart():
    st.title("🛒 Your Cart")

    if not st.session_state.cart: #not indicates list is empty
        st.info("Your cart is empty. Go back to the menu to add items!")
        if st.button("← Back to Menu"):
            st.session_state.page = 'menu'
            st.rerun()
        return

    total_price = 0
    total_calories = 0

    for item in st.session_state.cart:

        with st.expander(f"{item['name']} - ${item['price']:.2f}"):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**Bread:** {item['bread']}")
                st.markdown(f"**Size:** {item['size']}")
                if item['vegetables']:
                    st.markdown(f"**Vegetables:** {', '.join(item['vegetables'])}")
                if item['condiments']:
                    st.markdown(f"**Condiments:** {', '.join(item['condiments'])}")
                if item['special_instructions']:
                    st.markdown(f"**Special Instructions:** {item['special_instructions']}")
                st.markdown(f"**Calories:** {item['calories']}")

            with col2:
                i = st.session_state.cart.index(item)
                if st.button("🗑️ Remove", key=f"remove_{i}"):
                    st.session_state.cart.pop(i)
                    st.rerun()

        total_price += item['price']
        total_calories += item['calories']


    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Items", len(st.session_state.cart)) #first item being the lable of matric, second is the value of metric --> numb of item
    with col2:
        st.metric("Total Price", f"${total_price:.2f}")
    with col3:
        st.metric("Total Calories", f"{total_calories}")

    st.markdown("---")

    col_btn1, col_btn2, col_btn3 = st.columns(3)
    with col_btn1:
        if st.button("← Continue Shopping"):
            st.session_state.page = 'menu'
            st.rerun()

    with col_btn2:
        if st.button("🗑️ Clear Cart"):
            st.session_state.cart = []
            st.rerun()

    with col_btn3:
        if st.button("💳 Proceed to Checkout"):
            st.session_state.page = 'checkout'
            st.rerun()







def display_checkout():
    st.title("💳 Checkout")

    if not st.session_state.cart:
        st.error("Your cart is empty!")
        if st.button("← Back to Menu"):
            st.session_state.page = 'menu'
            st.rerun()
        return

    # Order summary
    st.subheader("📋 Order Summary")
    total_price = 0
    for item in st.session_state.cart:
        total_price += item['price']
    GST = total_price * 0.09  # 9% GST
    final_total = total_price + GST

    for item in st.session_state.cart:
        st.markdown(f"- {item['name']} (${item['price']:.2f})")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Subtotal", f"${total_price:.2f}")
    with col2:
        st.metric("GST (9%)", f"${GST:.2f}")
    with col3:
        st.metric("**Total**", f"${final_total:.2f}")

    st.markdown("---")

    # Customer information
    st.subheader("👤 Customer Information")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name*", placeholder="SVY") #placeholder --> faded text inside the input box
        phone = st.text_input("Phone Number*", placeholder="+65 8888 8888")
        email = st.text_input("Email*", placeholder="emmahtee@emt.com.sg")


        valid_name = True
        valid_phone = True
        valid_email = True


        if name.strip() == "":
            valid_name = False
            st.error("⚠️ Please enter your name.")

        phone_pattern = r"^\+65\s?\d{4}\s?\d{4}$" # s? --> Optional space after +65
        if not re.match(phone_pattern, phone):
            valid_phone = False
            st.error("⚠️ Phone number must start with '+65' and have 8 digits, e.g., +65 8888 8888.")


        email_pattern = r"^[^@]+@[^@]+\.com$" #[^@]One or more characters that are not @, @, and .com ends the string
        if not re.match(email_pattern, email):
            valid_email = False
            st.error("⚠️ Please enter a valid email containing '@' and ending with '.com'.")


    with col2:
        order_type = st.selectbox("Order Type", ["Pickup", "Delivery"])

        if order_type == "Delivery":
            address = st.text_area("Delivery Address*",
                                 placeholder="8 Somapah Road, Singapore 487372")
        else:
            st.info("📍 Pickup Location: 59 Changi South Ave 1, Singapore 485999")

    # Payment method
    st.subheader("💰 Payment Method")
    payment_method = st.selectbox("Choose Payment Method",
                                ["Credit Card", "Debit Card", "Apple Pay", "Google Pay", "Cash (Pickup Only)"])

    if payment_method in ["Credit Card", "Debit Card"]:
        col1, col2 = st.columns(2)
        with col1:
            card_number = st.text_input("Card Number", placeholder="8888 8888 8888 8888")
            cardholder_name = st.text_input("Cardholder Name", placeholder="SVY")
        with col2:
            expiry = st.text_input("MM/YY", placeholder="12/25")
            cvv = st.text_input("CVV", placeholder="123", type="password") #type='passoword' hides text input -> ******

    elif payment_method in ["Apple Pay", "Google Pay"]:
        st.info(f"You will be redirected to {payment_method} to complete your payment.")

    elif payment_method == "Cash (Pickup Only)" and order_type == "Delivery":
        st.error("Cash payment is only available for pickup orders.")

    # Special instructions
    delivery_instructions = st.text_area("Delivery/Pickup Instructions",
                                       placeholder="Ring doorbell, leave at door, etc.")

    st.markdown("---")

    # Place order button
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("← Back to Cart"):
            st.session_state.page = 'cart'
            st.rerun()

    with col2:
        if st.button("🏠 Back to Menu"):
            st.session_state.page = 'menu'
            st.rerun()

    with col3:

        if st.button("✔️ Place Order", type="primary"): #type='primary' -> highlighted button
            # Validate required fields
            required_fields = [name, phone, email]
            if order_type == "Delivery":
                if 'address' in locals():
                    required_fields.append(address) #locals() -> check if address exists in the function
                else:
                    required_fields.append("")

            valid_credit = True
            valid_expiry = True
            valid_cvc = True

            if payment_method in ["Credit Card", "Debit Card"]:
            # Credit card number: must be 16 digits

                if not re.fullmatch(r"\d{16}", card_number or ""):
                    valid_credit = False
                    st.error("⚠️ Credit card number must have exactly 16 digits.")


                if not re.fullmatch(r"(0[1-9]|1[0-2])/([0-9]{2})", expiry or ""):
                    valid_expiry = False
                    st.error("⚠️ Expiry date must be in MM/YY format, e.g., 08/26.")


                if not re.fullmatch(r"\d{3}", cvv or ""):
                    valid_cvc = False
                    st.error("⚠️ CVV must have exactly 3 digits.")

            if not all(required_fields): #check if all items in the required_fields are true
                st.error("⚠️ Please fill in all required fields (name, phone, email, address if delivery).")
            elif payment_method in ["Credit Card", "Debit Card"] and not (valid_credit and valid_expiry and valid_cvc):
                st.error("⚠️ Please correct your credit card details.")
            else:
            # Generate order confirmation
                st.success("🎉 Order placed successfully!")
                st.balloons()

                st.info(f"""
                **Order Confirmation**

                Customer: {name}
                Phone: {phone}
                Email: {email}

                Order Type: {order_type}
                Payment: {payment_method}

                Total: ${final_total:.2f}

                Expected {order_type.lower()} time: 15-20 minutes

                We'll send you a confirmation email shortly!
                """)

                st.session_state.order_placed = True #An order is placed

            #else:
                #st.error("Please fill in all required fields and payment information.")

        # Clear cart after successful order
        if st.session_state.get("order_placed"):
            if st.button("Start New Order"):
                st.session_state.cart = []
                st.session_state.current_sandwich = None
                st.session_state.page = 'menu'
                st.session_state.order_placed = False

                st.rerun()
