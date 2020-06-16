from util.config import *


#experiments/test_continuous_fully_connected
# --dataset_folder /media/leaps/dvs --checkpoint_filedef

def main(config):
    print(config)

if __name__ == '__main__':
    main(Config('trian.yml'))