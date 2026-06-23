from torchvision.datasets import ImageFolder
import os
 
# Mean and std computed from the training set (your supervisor's split).
# To recompute, run mean_std.py against the training_set folder.
OLIVETTI_MEAN = (0.5454,)
OLIVETTI_STD  = (0.1722,)
 
NUM_CLASSES = 40
 
 
class OlivettiFacesDataset(ImageFolder):
    """
    Dataset for the pre-split Olivetti faces dataset stored on Google Drive.
 
    Folder structure expected:
        root/
        ├── training_set/
        │   ├── class_00/  *.png
        │   ├── class_01/  *.png
        │   └── ...
        └── validation_set/
            ├── class_00/  *.png
            ├── class_01/  *.png
            └── ...
 
    Labels are assigned alphabetically by folder name:
        class_00 → 0, class_01 → 1, ..., class_39 → 39
    """
 
    def __init__(self, root, train=True, transform=None, download=None):
        split_folder = 'training_set' if train else 'validation_set'
        split_path = os.path.join(root, split_folder)
        super().__init__(root=split_path, transform=transform)