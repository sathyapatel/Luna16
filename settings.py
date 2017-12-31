import os
COMPUTER_NAME = os.environ['COMPUTERNAME']
print("Computer: ", COMPUTER_NAME)

WORKER_POOL_SIZE = 8

TARGET_VOXEL_MM = 1.00
MEAN_PIXEL_VALUE_NODULE = 41
LUNA_SUBSET_START_INDEX = 0
SEGMENTER_IMG_SIZE = 320

BASE_DIR_SSD = "E:\\stage1\\stage1\\"
BASE_DIR = "E:\\stage1\\stage1"
EXTRA_DATA_DIR = "C:\\Users\\Sangryal\\Downloads\\sathya\\2nd place\\kaggle_ndsb2017\\kaggle_ndsb2017-master\\resources\\resources\\"
NDSB3_RAW_SRC_DIR = BASE_DIR + "\\ndsb_raw\\stage12\\"
LUNA16_RAW_SRC_DIR = BASE_DIR + "\\luna_raw\\"

NDSB3_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "ndsb3_extracted_images\\"
LUNA16_EXTRACTED_IMAGE_DIR = BASE_DIR_SSD + "luna16_extracted_images\\"
NDSB3_NODULE_DETECTION_DIR = BASE_DIR_SSD + "ndsb3_nodule_predictions\\"

