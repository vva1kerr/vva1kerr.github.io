from PIL import Image

# Load the image
image_path = r"C:\Users\razer\Desktop\walkerrh.github.io\assets\art\Wang_Ximeng._A_Thousand_Li_of_Rivers_and_Mountains._(Complete,_51,3x1191,5_cm)._1113._Palace_museum,_Beijing.png"
image = Image.open(image_path)

# Define the dimensions for the Razer 15 desktop screen size
razer_15_width = 1920
razer_15_height = 1080

# Calculate the number of horizontal slices needed
num_slices = image.width // razer_15_width

# Slice the image into Razer 15 desktop screen sizes
slices = []
for i in range(num_slices):
    left = i * razer_15_width
    right = left + razer_15_width
    slice_image = image.crop((left, 0, right, razer_15_height))
    slices.append(slice_image)

# Save the slices
slice_paths = []
for index, slice_image in enumerate(slices):
    slice_path = fr"C:\Users\razer\Desktop\OSA_art\A_thousand_rivers_{index + 1}.png"
    slice_image.save(slice_path)
    slice_paths.append(slice_path)

print(slice_paths)
