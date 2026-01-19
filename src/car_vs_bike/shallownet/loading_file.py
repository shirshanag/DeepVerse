images=[]
labels=[]
dataset_path="/content/drive/MyDrive/Car-Bike-Dataset"
for label,category in enumerate(["Bike","Car"]):
  folder_path=os.path.join(dataset_path,category)
  for image_name in os.listdir(folder_path):
    image_path=os.path.join(folder_path,image_name)
    img=cv2.imread(image_path)
    img=cv2.resize(img,(224,224))
    images.append(img)
    labels.append(label)
print(len(images))
print(len(labels))
