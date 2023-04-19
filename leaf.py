#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/udiya/Desktop/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/model.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_plant_dieas(any_plant):
    test_image = load_img(any_plant, target_size = (128, 128)) # load image 
    print("@@ Got Image for prediction")
    
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
    
    result = model.predict(test_image) # predict diseased palnt or not
    print('@@ Raw result = ', result)  
    pred = np.argmax(result, axis=1)
    print(pred)
    if pred==0:
        return "Apple - Healthy",'Apple_Healthy.html'
    elif pred==1:
        return "Apple - Scab Disease", 'apple__apple_scab.html'
    elif pred==2:
        return "Apple - Black Rot Disease", 'Apple__Black_rot.html'
    elif pred==3:
        return "Apple - Cedar Disease", 'Apple__cedar_rust.html'
    elif pred==4:
        return "Chilli - Healthy", 'chilli_healthy.html'
    elif pred==5:
        return "Chilli - LeafSpot Disease", 'chilli_leafspot.html'
         
    elif pred==6:
        return "Chilli- Leaf Curl Disease", 'chili_leafcurl.html'
          
    elif pred==7:
        return "Chilli- Whitefly Disease", 'chilli_whitefly.html'
          
    elif pred==8:
        return "Chilli - Yellowish Disease", 'chilli_yellow.html'
          
    elif pred==9:
        return "Corn - Blight Disease", 'corn_blight.html'
    elif pred==10:
        return "Corn - Corn Common Rust Disease", 'corn_commonrust.html'
    elif pred==11:
        return "Corn - Corn Gray Leafspot Disease", 'corn_greyleafspot.html'
    elif pred==12:
        return "Corn - Healthy", 'corn_healthy.html'
    elif pred==13:
        return "Cotton - Bacterial Blight Disease", 'Cotton_Bacteial_Bright.html'
    elif pred==14:
       return "Cotton - Curl Virus Disease", 'Cotton_Curl_Leaf.html'
    elif pred==15:
       return "Cotton - Fussarium Wilt Disease", 'Cotton_Fussarium_Wilt.html'
    elif pred==16:
       return "Cotton - Healthy" , 'cotton_healthy.html'
    elif pred==17:
        return "Poptato - Early Blight" , 'potato__early_blight.html'
    elif pred==18:
        return "Potato - Late Blight" , 'potato__late_blight.html'
    elif pred==19:
        return "Potato - Healthy" , 'potato_healthy.html'
    elif pred==20:
        return "Rice - Bacterial Leaf Blight" , 'rice_bacterialblight.html'
    elif pred==21:
        return "Rice - Brown Spot" , 'rice_blackspot.html'
    elif pred==22:
        return "Rice - Healthy" , 'Rice_Healthy.html'
    elif pred==23:
        return "Rice - Leaf Smut" , 'rice__leafsmut.html'
    elif pred==24:
        return "Sugarcane - Healthy" , 'Sugarcane_Healthy.html'
    elif pred==25:
        return "Sugarcane - Red Rot Disease" , 'Sugarcane_Red_Rot.html'
    elif pred==26:
        return "Sugarcane - Red Rust Disease" , 'Sugarcane_Red_Rust.html'
    elif pred==27:
       return "Tomato - Bacteria Spot Disease", 'Tomato_Bacteria_Spot.html'
    elif pred==28:
        return "Tomato - Early Blight Disease", 'Tomato_Early_Blight.html'
    elif pred==29:
        return "Tomato - Healthy", 'Tomato-Healthy.html'
    elif pred==30:
        return "Tomato - Late_Blight Disease", 'Tomato_Late_Blight.html'
    elif pred==31:
        return "Tomato - Leaf Mold Disease", 'Tomato_Leaf_Mold.html'
    elif pred==32:
        return "Tomato - Yellow Leaf Curl Virus", 'Tomato_Yellow_Leaf_Curl_Virus.html'
    elif pred==33:
        return "Tomato - Two Spotted spider mite Disease", 'Tomato_Two-spotted_spider_mite.html'
    elif pred==34:
        return "Wheat - Healthy", "Wheat_Healthy.html"
    elif pred==35:
        return "Wheat - Septoria Disease","Wheat_Septoria.html"
    elif pred==36:
        return "Wheat - Stripe Rust Disease","Wheat_Stripe_Rust.html"
# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('C:/Users/udiya/Desktop/Plant-Leaf-Disease-Prediction-main/Plant-Leaf-Disease-Prediction-main/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_plant_dieas(any_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
