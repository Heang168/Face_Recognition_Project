from ast import Try
from preprocess import preprocesses

def _data_preprocessing():
    input_datadir = './train_img'
    output_datadir = './aligned_img'

    obj=preprocesses(input_datadir,output_datadir)
    nrof_images_total,nrof_successfully_aligned=obj.collect_data()


    print('Total number of images: %d' % nrof_images_total)
    print('Number of successfully aligned images: %d' % nrof_successfully_aligned)

if __name__ == "__main__":
    _data_preprocessing()
    

