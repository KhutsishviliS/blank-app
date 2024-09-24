import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from streamlit_option_menu import option_menu



st.title(":blue[AI FASHION MNIST Classification]",anchor=False)
#st.markdown("[link](main.py)")

st.markdown("# ტანსაცმლის კლასიფიკაცია ")
st.markdown("""მოგესალმებით მეგობრებო ეს არის ჩემი პირველი ოფიციალური პროექტი *ტანსაცმლის კლასიფიკაცია* ხელოვნური ინტელექტის დახმარებით
ეს პროექტი შექმნილია [Python](https://www.python.org/)-ს და [TensorFlow](https://www.tensorflow.org)-ს გამოყენებით """)
st.markdown("---")
st.markdown("""  **თავდაპირველად გირჩევთ რომ გამოიყენოთ [Google Colab](https://colab.google/) ასე უფრო გაგიმარტივდებათ მონაცემთა დამუშავება და ვიზუალიზაცია. 
თუ გსურთ რო გამოიყენოთ საკუთარი კომპიუტერი/ლეპტოპი მაშნ პირველ რიგში საჭიროა დაინსტალირებული გქონდეთ თქვენს IDE-ში შემდგომი მოდულები:**""")
st.markdown("""
            1. **tensorflow**
            2. **numpy**
            3. **pandas**
            4. **matplotlib**
            """)
st.info("იმ შემთხვევაში თუ იყენებთ Google Colab-ს, ეს მოდულები უკვე დაინსტალირებულია და თქვენ მხოლოდ მისი იმპორტირება დაგჭირდებათ.")
st.code("""
        pip install tensorflow
        pip install numpy
        pip install pandas
        pip install matplotlib
""",language="python")


st.markdown("* **ამის შემდეგ უნდა შემოვიტანოთ მოდულები ჩვენს IDE-ში** ")
st.code("""
        import tensorflow as tf
        import numpy as np
        import pandas as pd
        import random
        import matplotlib.pyplot as plt
""",language="python")

st.markdown("TensorFlow-ს პაკეტს მოყვება ფოტო მონაცემები **fashion_mnist** და ამ მონაცემებს გამოვიყენებთ ჩვენი ხელოვნური ინტელექტის სავარჯიშოდ. ")
st.code("""
        fashion_mnist= tf.keras.datasets.fashion_mnist  #fashion_mnist მონაცემთა იმპორტირება
        # მონაცემთა გაყოფა სავარჯიშო და სატესტო მონაცემებად
        (train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
""",language="python")



st.code("""
        fashion_mnist= tf.keras.datasets.fashion_mnist
        (train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
        train_images_norm = train_images/255.0
        test_images_norm = test_images/255.0
        class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
        plt.figure(figsize=(7,7))
        for i in range(4):
            ax = plt.subplot(2,2,i+1)
            random_index = random.choice(range(len(train_images)))
            plt.title(class_names[train_labels[random_index]])
            plt.imshow(train_images[random_index],cmap=plt.cm.binary)
""",language="python")
st.markdown("> ფოტო მონაცემის მაგალითი:")
fashion_mnist= tf.keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

train_images_norm = train_images/255.0
test_images_norm = test_images/255.0

class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]






def display_random_images(images, labels, class_names):
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    fig.suptitle("4 Random Fashion MNIST Images", fontsize=16)
    
    for i, ax in enumerate(axs.flat):
        random_index = np.random.randint(0, len(images))
        img = images[random_index]
        label = labels[random_index]
        
        ax.imshow(img, cmap='gray')
        ax.set_title(f"{class_names[label]}")
        ax.axis('off')
    
    plt.tight_layout()
    return fig

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #8FD14F;
    foreground-color:#8FD14F;
    border: none !important;
    color:white !important;
}

div.stButton > button:hover {
    background-color: #7AB33D !important;
    color: white !important;
}
</style>""", unsafe_allow_html=True)

if st.button("Show 4 Random Images"):
    fig = display_random_images(train_images, train_labels, class_names)
    st.pyplot(fig)

if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1


st.markdown("---")



