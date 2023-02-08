from blood_calculator import *
print("This is the database.py file")
print("Python thinks this is called{}".format(__name__))
# import blood_calculator as bc
# from blood_calculator import HDL_analysis, HDL_input
# no matter how you import the function in the imported module
# will still be runned, unless use the if statement in that module

HDL = 55
HDL_analysis = HDL_analysis(HDL)

print("The HDL analysis in {}".format(HDL_analysis))
