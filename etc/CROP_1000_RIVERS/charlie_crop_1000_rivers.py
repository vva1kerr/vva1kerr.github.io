from PIL import Image

# Load the image
image_path = r"C:\Users\razer\Desktop\walkerrh.github.io\assets\art\Wang_Ximeng._A_Thousand_Li_of_Rivers_and_Mountains._(Complete,_51,3x1191,5_cm)._1113._Palace_museum,_Beijing.png"
image = Image.open(image_path)

# Define the dimensions for the slices based on the aspect ratio 16:9
slice_width = 355
slice_height = 200  # Full height of the image

# Calculate the number of slices needed
num_slices = image.width // slice_width
if image.width % slice_width != 0:
    num_slices += 1  # Include the remaining part as an additional slice

# Slice the image into segments with a 16:9 aspect ratio
slices = []
for i in range(num_slices):
    left = i * slice_width
    right = min(left + slice_width, image.width)  # Ensure the right boundary does not exceed image width
    slice_image = image.crop((left, 0, right, slice_height))
    slices.append(slice_image)

# Save the slices
slice_paths = []
for index, slice_image in enumerate(slices):
    slice_path = fr"C:\Users\razer\Desktop\OSA_art\A_thousand_rivers\cuts\atr_{index + 1}.png"
    slice_image.save(slice_path)
    slice_paths.append(slice_path)

print(slice_paths)
