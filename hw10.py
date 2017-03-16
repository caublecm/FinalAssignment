# This final project was designed to help my customers select the correct objective lens for their microscopes
# Begin the program by typing the following two arguments into the command line: optics.csv, 2 (optics.csv accesses the file and 2 is the column for the medium.)
# The program counts and returns the number of objective lenses available for use with each of the four different mediums: Air, Water, Normal oil and Silicone oil.
# The customer is prompted to select the medium they want to use.
# The program returns a list of magnifications available to choose from.
# The customer is prompted to select the magnification from the available objective lenses
# The program returns the highest numerical aperture and calculates the smallest feature the customer can resolve with this objective/medium combination.



import sys #imports the sys.argv functions
import csv #imports the csv functions

# Begin the program by typing the following two arguments into the command line: optics.csv, 2 (optics.csv accesses the file and 2 is the column for the medium.)

my_file = sys.argv[1]
medium_material = int(sys.argv[2])

# opens and reads/returns the file
def read_in_csv(file_path):
    try:
        f = open(file_path)
        my_file = csv.reader(f)
    except IOError:
        print("The file you requested cannot be found")
    return my_file

# This function counts and returns the number of objective lenses available for use with each of the four different mediums: Air, Water, Normal oil and Silicone oil.
def count_mediums(in_file, medium):
    obj_dict = {}  #uses a dictionary
    try:
        my_file = read_in_csv(in_file)
    except IOError:
        print("The file you requested cannot be found")

    #loop through objectives to find medium and objective count for each

    for row in my_file:
        key_obj = row[medium]
        # for every row, check if medium in dictionary
        if key_obj in obj_dict:
            obj_dict[key_obj] = obj_dict[key_obj] + 1
        #if not, add it, and set the count to 1
        else:
            obj_dict[key_obj] = 1
    return obj_dict  # return dictionary of objective lenses for each medium



# The customer is prompted to select the medium they want to use and what magnifications are available for that medium.

def select_mag(in_file, in_medium):
    obj_list = []  # uses a list to collect magnifications for each medium
    try:
        my_file = read_in_csv(in_file)
    except IOError:
        print("The file you requested cannot be found")

    # loops through rows checking for the medium the customer selected.
    for row in my_file:
        if row[2] == in_medium:
            obj_list.append(str(row[1])) # if medium is in row the magnifications are appended into a list
        else:
            continue
    unique_obj = set(obj_list) # Since there may be more than one magnification, we don't want to list it more than one time, so "set" is used.
    return unique_obj # a list of available magnifications for the medium the customer wants is returned.


# This function returns the highest numerical aperture and calculates the smallest feature they can resolve with this objective.

def max_NA(in_file, mag, med):
    NA_list = [] #uses a list to collect NA for each medium
    try:
        my_file = read_in_csv(in_file)
    except IOError:
        print("The file you requested cannot be found")

    #loops through rows checking for the magnification and the medium the customer selected

    for row in my_file:
        if row[1] == mag and row[2] == med:
            NA_list.append(float(row[3]))
        else:
            continue


    numerical_aperture =  max(NA_list) #finds the maximum numerical aperture
    resolution = 0.61*550/(numerical_aperture) # calculates the resolution
    print("\nThe maximum numerical aperture for this {}x / {} combination is: {}".format(mag,med,numerical_aperture))#prints the NA for the medium/mag combo
    print("\nThis combination will allow you to resolve a {} um feature if you are using 550 nm wavelength light.".format(round(resolution,2))) # prints the resolving power

    # writes the same information to the file 'HW10.txt'
    file = open('HW10.txt', 'w')
    file.write("\nThe maximum numerical aperture for this {}x / {} combination is: {}".format(mag,med,numerical_aperture))
    file.write("\nThis combination will allow you to resolve a {} um feature if you are using 550 nm wavelength light.".format(round(resolution,2)))

    file.close()



##main


my_file = "./optics.csv" #file name

#have the user specify input file
in_file = sys.argv[1]

medium_count = count_mediums(my_file, medium_material)
print ("\nHere are the number of objectives that are designed for use with the following mediums:\n{}".format(medium_count))

#try/except to catch non-number value
try:
    medium = int(input("\nEnter the number for the medium you want to use: enter '1' for Air, '2' for Water, '3' for Normal oil, '4' for Silicone oil: "))
except ValueError:
    print("That was not a number. Restart the program")


if medium == 1:
    medium_choice = "Air"
elif medium == 2:
    medium_choice = "Water"
elif medium == 3:
    medium_choice = "Normal oil"
elif medium == 4:
    medium_choice = "Silicone oil"

#try/except to catch invalid number choice

try:

    mag_options = select_mag(my_file, medium_choice)

except NameError:
    print("Your entry wasn't valid. Please restart the program")

print("\nThese are the magnification options for the medium '{}' ".format(medium_choice))
print(mag_options)

#try/except to catch magnification that is not available for chosen medium

try:

    magnification = str(input("\nEnter the magnification you want to use for this medium: "))
    num_apt_max = max_NA(my_file, magnification, medium_choice)

except:
    print("This is an invalid entry. Please restart the program")
