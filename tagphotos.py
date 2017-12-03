import glob
import pprint
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

api_key = 'ebf64f71a9a3456bbedba209cedd8fd6'

# For printing unicode characters to the console.
def encode(text):
	if type(text) is list or type(text) is tuple:
		return [x.encode('utf-8') for x in text]
	elif type(text) is not int:
		return text.encode('utf-8')
	else:
		return text

# Counter variables
index = 0
counter = 0
batch_size = 32

app = ClarifaiApp(api_key=api_key)

pp = pprint.PrettyPrinter(indent=2)

# Image Directory
path = '/users/souhail/Downloads/family/*'
files = glob.glob(path)

# Total file amount
total_files = len(files)
print("Total files: " + str(total_files))

while (counter < total_files):
  #print "Processing batch " + str(index+1)
	
  # Batch Image List
  imageList=[]
	
  for x in range(counter,counter+batch_size - 1):
    try:
      
      imageList.append(ClImage(filename=files[x], image_id=files[x]))

    except:
    	continue
	
  

  #Get predictions from these images
  model = app.models.get('food-items-v1.0')
  pp.pprint(model.predict(imageList))

  counter=counter+batch_size
  index=index+1
