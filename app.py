import streamlit as st
from PIL import Image
import io
import os
from rembg import remove
import base64

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Background Remover Tool",
        page_icon="🖼️",
        layout="wide"
    )
    
    # Application title and description
    st.title("🖼️ Background Remover")
    st.markdown("""
    Upload an image and remove its background with a single click.
    This tool uses the Rembg library to process your images.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            # Read the image
            image = Image.open(uploaded_file)
            
            # Create columns for displaying images
            col1, col2 = st.columns(2)
            
            # Display original image
            with col1:
                st.subheader("Original Image")
                st.image(image, use_column_width=True)
            
            # Process button
            if st.button("Remove Background"):
                with st.spinner("Processing image..."):
                    # Remove background
                    output = remove(image)
                    
                    # Display processed image
                    with col2:
                        st.subheader("Processed Image")
                        st.image(output, use_column_width=True)
                    
                    # Add download button
                    buf = io.BytesIO()
                    output.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="Download Processed Image",
                        data=byte_im,
                        file_name=f"bg_removed_{uploaded_file.name.split('.')[0]}.png",
                        mime="image/png"
                    )
                    
                    st.success("Background removed successfully!")
        
        except Exception as e:
            st.error(f"Error processing image: {e}")
            st.info("Please upload a valid image file.")
    
    # Add footer
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit and Rembg")

if __name__ == "__main__":
    main()

