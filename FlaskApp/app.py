from flask import Flask, render_template, request
from PIL import Image
import rembg
from flask import redirect
from io import BytesIO
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, save_img, load_img
from tensorflow.keras.models import load_model
import os

app = Flask(__name__)


model = load_model("model.h5")

classes = [
    "Africanized Honey Bees (Killer Bees)",
    "Aphids",
    "Armyworms",
    "Brown Marmorated Stink Bugs",
    "Cabbage Loopers",
    "Citrus Canker",
    "Colorado Potato Beetles",
    "Corn Borers",
    "Corn Earworms",
    "Fall Armyworms",
    "Fruit Flies",
    "Spider Mites",
    "Thrips",
    "Tomato Hornworms",
    "Western Corn Rootworms"
]

def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def resize_image(image):
    img = Image.open(image)
    img = img.resize((224, 224))
    return img

def remove_background(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    f_img = img_byte_arr.read()
    f_out = rembg.remove(f_img)
    processed_img = Image.open(BytesIO(f_out))
    return processed_img

def save_image(image, filename, dest_dir):
    image.save(dest_dir + filename)

def augment_and_save(image, filename, dest_dir):
    img_array = img_to_array(image)
    img_array = img_array.reshape((1,) + img_array.shape)
    
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='nearest'
    )
    
    for i in range(20):  
        augmented_datagen = datagen
        augmented_img_array = next(augmented_datagen.flow(img_array, batch_size=1))[0].astype('uint8')
        augmented_img = Image.fromarray(augmented_img_array)
        new_img_path = dest_dir + f"aug_{i}_{filename}"
        save_img(new_img_path, augmented_img)
        
def predict_insect_class(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  
    img_array /= 255.  


    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)
    predicted_class = classes[predicted_class_index]
    
    return predicted_class

def predict_insect_classes_in_folder(folder_path):
    class_hits = {class_name: 0 for class_name in classes}
    for filename in os.listdir(folder_path):
        if filename.startswith("aug_"):  # Filter augmented images
            img_path = os.path.join(folder_path, filename)
            predicted_class = predict_insect_class(img_path)
            class_hits[predicted_class] += 1
    
    max_hits_class = max(class_hits, key=class_hits.get)
    return max_hits_class

def delete_files_in_folder(folder_path):
    """Delete all files in the specified folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
            
@app.route("/c1")
def c1():
    return render_template("c1.html")

@app.route("/c2")
def c2():
    return render_template("c2.html")

@app.route("/c3")
def c3():
    return render_template("c3.html")

@app.route("/c4")
def c4():
    return render_template("c4.html")

@app.route("/c5")
def c5():
    return render_template("c5.html")

@app.route("/c6")
def c6():
    return render_template("c6.html")

@app.route("/c7")
def c7():
    return render_template("c7.html")

@app.route("/c8")
def c8():
    return render_template("c8.html")

@app.route("/c9")
def c9():
    return render_template("c9.html")


@app.route("/c10")
def c10():
    return render_template("c10.html")

@app.route("/c11")
def c11():
    return render_template("c11.html")

@app.route("/c12")
def c12():
    return render_template("c12.html")

@app.route("/c13")
def c13():
    return render_template("c13.html")

@app.route("/c14")
def c14():
    return render_template("c14.html")

@app.route("/c15")
def c15():
    return render_template("c15.html")





def Redirect(name):
    if name == "Africanized Honey Bees (Killer Bees)":
        return c1()
    elif name == "Aphids":
        return c2()
    elif name == "Armyworms":
        return c3()
    elif name == "Brown Marmorated Stink Bugs":
        return c4()
    elif name == "Cabbage Loopers":
        return c5()
    elif name == "Citrus Canker":
        return c6()
    elif name == "Colorado Potato Beetles":
        return c7()
    elif name == "Corn Borers":
        return c8()
    elif name == "Corn Earworms":
        return c9()
    elif name == "Fall Armyworms":
        return c10()
    elif name == "Fruit Flies":
        return c11()
    elif name == "Spider Mites":
        return c12()
    elif name == "Thrips":
        return c13()
    elif name == "Tomato Hornworms":
        return c14()
    elif name == "Western Corn Rootworms":
        return c15()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    delete_files_in_folder("uploads/")
    if "picture" not in request.files:
        return "No file part"
    file = request.files["picture"]
    if file.filename == "":
        return "No selected file"
    if file and is_allowed_file(file.filename):

        resized_img = resize_image(file)
     
        removed_bg_img = remove_background(resized_img)
        
        save_image(removed_bg_img, "processed.png", "uploads/")

        augment_and_save(removed_bg_img, "processed.png", "uploads/")

        max_hits_class = predict_insect_classes_in_folder("uploads/")
        print(f"Class with maximum hits: {max_hits_class}")
        Redirect(max_hits_class)
        return Redirect(max_hits_class)
    else:
        return "Invalid file format. Please upload a PNG, JPG, or JPEG file."

if __name__ == "__main__":
    app.run(debug=True)
