import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def _load_csv_data(file):
    df = pd.read_csv(file)
    return df

def _display_empty_row():
    st.write("")

def _display_output(output): 
    css = """
        <style>
        .highlight {
            padding: 10px;
            background-color: #f5f5f5;
            border: 1px solid #e3e3e3;
            border-radius: 5px;
            font-weight: bold;
        }
        </style>
    """

    st.write(css, unsafe_allow_html=True)
    st.markdown(f'<div class="highlight">{output}</div>', unsafe_allow_html=True)

def _display_images(images):
    # Create a 2x2 grid for displaying images
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))
    
    # Iterate through the images and display them
    for i, image_path in enumerate(images):
        row = i // 2
        col = i % 2
        axs[row, col].imshow(plt.imread(image_path))
        axs[row, col].axis('off')
    
    # Display the grid of images
    st.pyplot(fig)


def main():
    # Set app title
    st.markdown("<h1 style='text-align: center;'>Demo Application</h1>", unsafe_allow_html=True)
    _display_empty_row()
    _display_empty_row()
    
    # Upload CSV file
    file = st.file_uploader('Upload CSV file', type=['csv'])
    _display_empty_row()
    
    if file is not None:
        # 1. Read the uploaded CSV file
        df = _load_csv_data(file)

        # 2. when button on Clicked
        if st.button('Submit'):
            # model prediction
            ### start code

            prediction = True
            ### end code
            _display_empty_row()
            _display_empty_row()
            _display_empty_row()

            output = "Model Prediction: NORMAL SAMPLE" if prediction else "Model Prediction: ABNORMAL SAMPLE"
            _display_output(output)
                    
            # 3. Display 4 images to visualize the prediction
            image = "test.jpg"
            images = [image, image, image, image]  # Assuming the column name for image paths is 'image_path'
            _display_images(images)
    
if __name__ == '__main__':
    main()
