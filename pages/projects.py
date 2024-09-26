import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from streamlit_option_menu import option_menu
from streamlit_app import page_design

page_design()

language = st.session_state.get('language', 'Georgian')


#text_title = "<p color=#FE6F00>AI FASHION MNIST Classification</p>"

st.markdown('<h1 style="color:#FE6F00";>AI FASHION MNIST Classification</h1>',unsafe_allow_html=True)

#st.markdown("[link](main.py)")

if language =="Georgian":
        st.markdown('<h2 style="color:#3A485F">ტანსაცმლის კლასიფიკაცია</h2>',unsafe_allow_html=True)
        st.markdown(""":gray[მოგესალმებით მეგობრებო ეს არის ჩემი პირველი ოფიციალური პროექტი *ტანსაცმლის კლასიფიკაცია* ხელოვნური ინტელექტის დახმარებით
        ეს პროექტი შექმნილია [Python](https://www.python.org/)-ს და [TensorFlow](https://www.tensorflow.org)-ს გამოყენებით] """)
        st.markdown("---")
        st.markdown("""
        <span style="color:#3A485F; font-weight:bold;">
        თავდაპირველად გირჩევთ რომ გამოიყენოთ <a href="https://colab.google/" target="_blank">Google Colab</a> ასე უფრო გაგიმარტივდებათ მონაცემთა დამუშავება და ვიზუალიზაცია. 
        თუ გსურთ რო გამოიყენოთ საკუთარი კომპიუტერი/ლეპტოპი მაშნ პირველ რიგში საჭიროა დაინსტალირებული გქონდეთ თქვენს IDE-ში შემდგომი მოდულები:
        </span>
        """, unsafe_allow_html=True)
else:
        st.markdown('<h2 style="color:#3A485F">Clothing Classification</h2>', unsafe_allow_html=True)
        st.markdown(""":gray[Welcome friends, this is my first official project *Clothing Classification* with the help of artificial intelligence. 
        This project is created using [Python](https://www.python.org/) and [TensorFlow](https://www.tensorflow.org).] """)
        st.markdown("---")
        st.markdown("""
        <span style="color:#3A485F; font-weight:bold;">
        First, I recommend that you use <a href="https://colab.google/" target="_blank">Google Colab</a> as it will make data processing and visualization easier for you. 
        If you want to use your own computer/laptop, first, you need to have the following modules installed in your IDE:
        </span>
        """, unsafe_allow_html=True)



st.markdown("""
            
    <p style="color: #3A485F;">1. <b>tensorflow</b></p>
    <p style="color: #3A485F;">2. <b>numpy</b></p>
    <p style="color: #3A485F;">3. <b>pandas</b></p>
    <p style="color: #3A485F;">4. <b>matplotlib</b></p>
    """, unsafe_allow_html=True)

if language =="Georgian":
        st.markdown("""
        <div style='background-color:#d9edf7; padding:10px; border-radius:5px;'>
        <strong style='color:#3A485F;'>ℹ️ იმ შემთხვევაში თუ იყენებთ Google Colab-ს, ეს მოდულები უკვე დაინსტალირებულია და თქვენ მხოლოდ მისი იმპორტირება დაგჭირდებათ.</strong>
        </div>
        """, unsafe_allow_html=True)
else:
        st.markdown("""
        <div style='background-color:#d9edf7; padding:10px; border-radius:5px;'>
        <strong style='color:#3A485F;'>ℹ️ If you are using Google Colab, these modules are already installed, and you only need to import them.</strong>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.code("""
        pip install tensorflow
        pip install numpy
        pip install pandas
        pip install matplotlib
""",language="python")

if language =="Georgian":
        st.markdown("""
        <span style="color:#3A485F; font-weight:bold;">
        ამის შემდეგ უნდა შემოვიტანოთ მოდულები ჩვენს IDE-ში/Google Colab-ში</span>
        """, unsafe_allow_html=True)
else:
        st.markdown("""
        <span style="color:#3A485F; font-weight:bold;">
        After this, we need to import the modules into our IDE/Google Colab.</span>
        """, unsafe_allow_html=True)




st.code("""
        import tensorflow as tf
        import numpy as np
        import pandas as pd
        import random
        import matplotlib.pyplot as plt
""",language="python")
if language == "Georgian:":
        st.markdown('<blockquote style="color:#3A485F;">TensorFlow-ს პაკეტს მოყვება ფოტო მონაცემები **fashion_mnist** და ამ მონაცემებს გამოვიყენებთ ჩვენი ხელოვნური ინტელექტის სავარჯიშოდ.</blockquote> ', unsafe_allow_html=True)
        st.code("""
                # fashion_mnist მონაცემთა იმპორტირება
                fashion_mnist= tf.keras.datasets.fashion_mnist 
                
                # მონაცემთა გაყოფა სავარჯიშო და სატესტო მონაცემებად
                (train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()
        """,language="python")
else:
        st.markdown('<blockquote style="color:#3A485F;">The TensorFlow package comes with image data **fashion_mnist**, and we will use this data for training our artificial intelligence.</blockquote> ', unsafe_allow_html=True)
        st.code("""
                # Importing the fashion_mnist dataset
                fashion_mnist = tf.keras.datasets.fashion_mnist 
                
                # Splitting the data into training and testing datasets
                (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        """, language="python")




st.code("""
        # მონაცემთა ნორმალიზება: პიქსელების 
        
        train_images_norm = train_images/255.0
        test_images_norm = test_images/255.0

        # თვალსაჩინოებისთვის შეგიძლიათ გამოსახოთ განსხვავება ნორმალიზებულ და არა ნორმალიზებულ მონაცემებს შორის
        #print(train_images[0]) # ვაჩვენებთ პირველი ფოტოს პიქსელურ მონაცემს
        #print(train_images_norm[0]) # ვაჩვენებთ პირველი ფოტოს ნორმალიზებულ ვარიანტს 

        # ვაჩვენოთ 4 რენდომ ფოტო fashion mnist მონაცემებიდან:
        class_names = ["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"]
        plt.figure(figsize=(7,7))
        for i in range(4):
            ax = plt.subplot(2,2,i+1)
            random_index = random.choice(range(len(train_images)))
            plt.title(class_names[train_labels[random_index]])
            plt.imshow(train_images[random_index],cmap=plt.cm.binary)
""",language="python")
st.markdown("<p style='color:#3A485F;' ფოტო მონაცემის მაგალითი:</p>", unsafe_allow_html=True)
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

if st.button("Show 4 Random Images",key="randomImage"):
    fig = display_random_images(train_images, train_labels, class_names)
    st.pyplot(fig)

if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1


st.markdown("---")


if language =="Georgian":
        st.markdown('''
        <p style="color:#3A485F;">
        <i>იმისათვის რომ ჩვენმა მოდელმა რაც შეიძლება მაქსიმალური შედეგი აჩვენოს, მოდით გადავიყვანოთ train_labels და test_labels მონაცემები კოდირების ფორმატში რომელსაც 
        <b>one_hot_encoding</b> ეწოდება. ეს არის მონაცემთა კოდირების მეთოდი რომელიც ძალიან ხშირად გამოიყენება კატეგორიული მონაცემების დასამუშავებლად.</i>
        <br>ვრცლად :
        <a href="https://en.wikipedia.org/wiki/One-hot" target="_blank">Wikipedia</a>, 
        <a href="https://www.tensorflow.org/api_docs/python/tf/one_hot" target="_blank">TensorFlow</a>
        </p>  

        ''', unsafe_allow_html=True)

else:
        st.markdown('''
        <p style="color:#3A485F;">
        <i>In order for our model to achieve the best possible results, let’s convert the train_labels and test_labels data into an encoding format called 
        <b>one_hot_encoding</b>. This is a data encoding method that is commonly used for processing categorical data.</i>
        <br>For more details:
        <a href="https://en.wikipedia.org/wiki/One-hot" target="_blank">Wikipedia</a>, 
        <a href="https://www.tensorflow.org/api_docs/python/tf/one_hot" target="_blank">TensorFlow</a>
        </p>  
        ''', unsafe_allow_html=True)


st.code("""
        train_labels_one_hot = tf.one_hot(train_labels,depth=10)
        test_labels_one_hot = tf.one_hot(test_labels,depth=10)
""")



if language == "Georgian":
        # Custom color and heading for "შევქმნათ მოდელის არქიტექტურა"
        st.markdown('<h4 style="color:#3A485F;">შევქმნათ მოდელის არქიტექტურა:</h4>', unsafe_allow_html=True)

        # Custom color for the quote text
        st.markdown('<blockquote style="color:#3A485F;">მე ამ პროცესს შემოკლებით CCF პროცესს ვუწოდებ (Create, Compile, Fit)</blockquote>', unsafe_allow_html=True)

else:
        # Custom color and heading for "Let's Create the Model Architecture"
        st.markdown('<h4 style="color:#3A485F;">Let\'s Create the Model Architecture:</h4>', unsafe_allow_html=True)

        # Custom color for the quote text
        st.markdown('<blockquote style="color:#3A485F;">I refer to this process as the CCF process (Create, Compile, Fit)</blockquote>', unsafe_allow_html=True)


st.code("""
        # Create The Model

        tf.random.set_seed = 42

        model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(10,activation="relu"),
        tf.keras.layers.Dense(10,activation="relu"),
        tf.keras.layers.Dense(10,activation="relu"),
        tf.keras.layers.Dense(10,activation="softmax")
        ])

        # Compile The Model
        model.compile(
        loss = tf.keras.losses.CategoricalCrossentropy(),
        optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001),
        metrics = ["accuracy"]
        )

        # Fit The Model

        history = model.fit(train_images_norm,
                            train_labels_one_hot,
                            epochs = 20
                            )
""")

st.code("""
        # მონაცემთა ვიზუალიზაცია
        pd.DataFrame(history.history).plot()
""")

if language == "Georgian":
        st.markdown('<p style="color:#3A485F;">ეს არის ჩვენი პირველი მოდელი. მოდით ახლა ვნახოთ თუ რამდენად კარგი მოდელია და რამდენად სწორად ისწავლა ტანსაცმლის განსხვავება.</p>', unsafe_allow_html=True)

else:
        st.markdown('<p style="color:#3A485F;">This is our first model. Now let’s see how good the model is and how accurately it has learned to differentiate between clothing items.</p>', unsafe_allow_html=True)


st.code("""
        
        model_prediction = model.predict(test_images_norm)
        y_pred = model_prediction.argmax(axis=1)
""")

st.code("""
        # შევამოწმოთ პირველ 100 მონაცემზე რამდენად სწორად მოახდინა მათი კლასიფიკაცია
        y_pred[:100] == test_labels[:100]
""")
