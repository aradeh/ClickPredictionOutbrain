import csv
from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


docID = []
entityID = []
conf_entity = []

with open("documents_entities.csv", 'r') as csvfi:
    read = csv.reader(csvfi, delimiter=',')
    next(read)
    for row in read:
        docID.append(int(row[0]))
        entityID.append(row[1])
        conf_entity.append(float(row[2]))

'''plt.scatter(docID, conf_entity, color='g')
plt.xlabel('Document ID')
plt.ylabel('Confidence Level')
plt.legend()
plt.title("Document entities Plot")
#plt.show()'''

categoryID =[]
conf_cat=[]

with open('documents_categories.csv', 'r') as file:
    f = csv.reader(file, delimiter=',')
    next(f)
    for row in f:
        categoryID.append(int(row[1]))
        conf_cat.append(float(row[2]))

'''plt.scatter(categoryID, conf_cat, color='c')
plt.xlabel('Category ID')
plt.ylabel('Confidence Level')
plt.legend()
plt.title("Document Category Plot")
#plt.show()'''

docID = []
topicID = []
conf_topic = []

with open("documents_topics.csv", 'r') as tfile:
    q = csv.reader(tfile, delimiter=',')
    next(q)
    for row in q:
        topicID.append(row[1])
        conf_topic.append(float(row[2]))

'''plt.scatter(topicID, conf_topic, color='g')
plt.xlabel('Topic ID')
plt.ylabel('Confidence Level')
plt.legend()
plt.title("Document Topic Plot")
#plt.show()'''


dict_data = dict(document_id=docID,entity_id=entityID,topic_id=topicID,category_id=categoryID,confidence_level=conf_entity)

document_frame = pd.DataFrame({k : pd.Series(v) for k,v in dict_data.iteritems()})

print document_frame

