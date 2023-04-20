from flask import Flask, render_template, request

from deepface import DeepFace

app = Flask(__name__)

# define face comparing function
def face_comparing(url1, url2):
    
    # use DeepFace to compare faces
    result = DeepFace.verify(url1, url2, distance_metric='euclidean')
    
    # get the Euclidean distance between the faces
    distance = result['distance']
    
    # set a threshold to determine if the faces match or not
    threshold = 0.6
    
    # compare the distance with the threshold
    if distance <= threshold:
        return 'Both photographs are of same person'
    else:
        return 'Both photographs are of two different persons'

# define home page route and view
@app.route('/')
def home():
    return render_template('index.html')

# define result page route and view
@app.route('/compare', methods=['POST'])
def compare():
    url1 = request.form['url1']
    url2 = request.form['url2']
    message = face_comparing(url1, url2)
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
