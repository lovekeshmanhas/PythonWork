# import module
import sys
print(sys.path)

# import sklearn as sk
# print(sk.__version__)

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())

import FilePy
print(FilePy.a)
FilePy.printFunction("Test")