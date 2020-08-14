from os import getcwd
from os.path import join

ROOT_PATH = getcwd()
HAARCASCADE_PATH = join(ROOT_PATH, 'haarcascade_frontalface_alt.xml')
MODEL_PATH = join(ROOT_PATH, 'model/facenet_keras.h5')
DATA_PATH = join(ROOT_PATH, 'train_images')
TEST_DATA_PATH = join(ROOT_PATH, 'test_images')

