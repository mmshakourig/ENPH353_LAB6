# dataOrganizer.py

import cv2
import numpy as np
import os

class DataOrganizer:

    label_lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, in_path, target_path) -> None:
        self.in_path = in_path
        self.target_path = target_path

    def segmentPlate(self, plate_name) -> list:

        plate = cv2.imread(self.in_path + plate_name)

        pl_ch1 = plate[80:240,:,2]
        pl_binary = pl_ch1 > 100

        out1 = pl_binary[:, 10:150]
        out2 = pl_binary[:, 150:290]
        out3 = pl_binary[:, 310:450]
        out4 = pl_binary[:, 450:590]

        pl_name = plate_name.split(".")[0]

        l_char1 = LabelledCharacter(out1, None, pl_name[-4])
        l_char2 = LabelledCharacter(out2, None, pl_name[-3])
        l_char3 = LabelledCharacter(out3, None, pl_name[-2])
        l_char4 = LabelledCharacter(out4, None, pl_name[-1])

        return [l_char1, l_char2, l_char3, l_char4]

    def labelVec(self, label_char) -> np.ndarray:
        # one-hot encoding
        l_vec = np.zeros(36)
        l_ind = self.label_lst.index(label_char)
        l_vec[l_ind] = 1

        return l_vec
    
    def store(self, labelledChar) -> str:
        os.chdir(self.target_path)

        if os.path.isdir(labelledChar.getChar()) is False:
            os.makedirs(labelledChar.getChar())

        os.chdir(self.target_path + labelledChar.getChar())

        img_name = (labelledChar.getChar() + "_" + str(len(os.listdir())) + ".png")
        img_data = labelledChar.getImage().astype(np.uint8)*255

        cv2.imwrite(img_name, img_data)

        return True
        
    def organize(self) -> None:
        print("Organizing...")
        os.chdir(self.in_path)
        plate_names = os.listdir()

        for plate in plate_names:
            if (plate == "blank_plate.png") is False:
                labelledChars = self.segmentPlate(plate)
                for char in labelledChars:
                    self.store(char)
        
        print("Done!")
        return True

class LabelledCharacter:

    def __init__(self, image, label, character) -> None:
        self.image = image
        self.label = label
        self.character = character

    def getImage(self) -> np.ndarray:
        return self.image
    
    def getLabel(self) -> np.ndarray:
        return self.label
    
    def getChar(self) -> str:
        return self.character