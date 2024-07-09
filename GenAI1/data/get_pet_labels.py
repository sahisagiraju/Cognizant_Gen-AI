#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sahishnu Sagiraju
# DATE CREATED: 06/30/24                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

 
def get_pet_labels(image_dir):
  """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
  """
  filename_list = listdir(image_dir)
  results_dic = dict()
  
  for filename in filename_list:
    # skip these unnecessary files
    if filename[0] == ".":
      continue
    
    '''
    ### I was gonna add this but wasn't sure if the classifier can only read .jpg, since we were asked to upload .jpg files
    
    filetype_check = filename.lower().split(".")
    if filetype_check[-1] != "jpg": 
      continue
    '''

    # creating label
    pet_name = ""    
    
    # format the filenames for label
    word_list = filename.lower().split("_")
    for word in word_list:
      if word.isalpha():
        pet_name += word + " "
    pet_name = pet_name.strip()

    # check for repeat files
    if filename not in results_dic:
      results_dic[filename] = [pet_name]
    else:
      print("\nKey Already Exists! \n{} exists in dictionary with value {}.".format(filename, pet_name))


    # Replace None with the results_dic dictionary that you created with this
    # function
  return results_dic
