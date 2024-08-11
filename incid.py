from PIL import Image, ImageFilter, ImageOps

def add_drop_shadow(image_path, output_path):
    original = Image.open(image_path)
    shadow = original.convert("RGBA").copy()
    
    # Create the shadow
    shadow_layer = Image.new("RGBA", shadow.size, (0, 0, 0, 255))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(10))
    
    # Offset the shadow
    combined = Image.new("RGBA", (shadow.width + 20, shadow.height + 20), (0, 0, 0, 0))
    combined.paste(shadow_layer, (10, 10))
    combined.paste(original, (0, 0), mask=original)
    
    combined.save(output_path)

add_drop_shadow('input_image.png', 'output_image_with_shadow.png')
