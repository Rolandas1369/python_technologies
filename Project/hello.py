import sys

"Adding data dir to sys.path"
#sys.path.append("/home/rolandas/Desktop/python_technologies/Data")
sys.path.append("../Data")
#print(sys.path)

from data import get_data

get_data()
