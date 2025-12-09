"""
Utility functions for file handling and image processing.
Contains helper functions for image cropping and file validation.
"""

import os
from werkzeug.utils import secure_filename
from PIL import Image
from config import ALLOWED_EXTENSIONS, TARGET_IMAGE_SIZE


def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename (str): Name of the file to check
        
    Returns:
        bool: True if file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def crop_image(image_path, output_path, target_size=TARGET_IMAGE_SIZE):
    """
    Crop and resize an image to the target size while maintaining aspect ratio.
    The image is cropped from the center to match the target aspect ratio,
    then resized to the exact target dimensions.
    
    Args:
        image_path (str): Path to the source image file
        output_path (str): Path where the cropped image will be saved
        target_size (tuple): Target dimensions as (width, height). Defaults to (450, 350)
        
    Returns:
        str: Path to the cropped image file
        
    Example:
        >>> crop_image('input.jpg', 'output.jpg', (450, 350))
        'output.jpg'
    """
    # Open the source image
    img = Image.open(image_path)
    
    # Calculate aspect ratios
    target_aspect = target_size[0] / target_size[1]  # width / height
    img_aspect = img.width / img.height
    
    # Crop to match target aspect ratio
    if img_aspect > target_aspect:
        # Image is wider than target aspect ratio, crop width
        new_width = int(img.height * target_aspect)
        left = (img.width - new_width) // 2
        img = img.crop((left, 0, left + new_width, img.height))
    else:
        # Image is taller than target aspect ratio, crop height
        new_height = int(img.width / target_aspect)
        top = (img.height - new_height) // 2
        img = img.crop((0, top, img.width, top + new_height))
    
    # Resize to exact target size
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    
    # Save the cropped image
    img.save(output_path)
    return output_path


def secure_file_path(filename, upload_folder):
    """
    Generate a secure file path for uploaded files.
    
    Args:
        filename (str): Original filename
        upload_folder (str): Folder where the file should be saved
        
    Returns:
        tuple: (secure_filename, full_filepath)
    """
    secure_name = secure_filename(filename)
    filepath = os.path.join(upload_folder, secure_name)
    return secure_name, filepath


def process_uploaded_image(file, upload_folder, prefix='cropped'):
    """
    Process an uploaded image: save, crop, and return the cropped filename.
    The original file is removed after cropping.
    
    Args:
        file: File object from Flask request
        upload_folder (str): Folder to save the image
        prefix (str): Prefix for the cropped filename. Defaults to 'cropped'
        
    Returns:
        str: Filename of the cropped image
        
    Raises:
        ValueError: If file processing fails
    """
    if not file or not allowed_file(file.filename):
        raise ValueError('Invalid file type')
    
    # Generate secure file paths
    original_filename, original_path = secure_file_path(file.filename, upload_folder)
    cropped_filename = f"{prefix}_{original_filename}"
    cropped_path = os.path.join(upload_folder, cropped_filename)
    
    # Save original file
    file.save(original_path)
    
    try:
        # Crop the image
        crop_image(original_path, cropped_path)
        
        # Remove original file
        if os.path.exists(original_path):
            os.remove(original_path)
        
        return cropped_filename
    except Exception as e:
        # Clean up on error
        if os.path.exists(original_path):
            os.remove(original_path)
        raise ValueError(f'Error processing image: {str(e)}')

