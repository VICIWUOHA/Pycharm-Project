import numpy as np

comfort = np.arange(0, 26)
print(comfort)

comfort2 = np.array(['cheerful', 'beautiful', 'questionnaire', 'happy', 'lovely'])
comfort2.sort()
print(comfort2)


# # print(arr[0:5])
#
# arr[0:5] = 20
# print(arr)
#
# arr2 = arr[0:7]
# arr2[:] = 30
#
# print(arr)
#
# #creating new array copy
#
# arrcopy = arr.copy()


# Visualizing the decision tree
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True, special_characters=True,
                feature_names=features, class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Iris.png')
Image(graph.create_png())




