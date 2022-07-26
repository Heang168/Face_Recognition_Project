import os

#incomplete
def remove_outlier():
    path = 'aligned_img'
    all_dir = []
    all_file = []
    print('Remove outlier is starting.....')
    
    print("Only directories:")
    all_dir = [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
    print("\nOnly files:")
    all_file = [ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ]

    print(all_dir)
    print(all_file)
    
if __name__ == "__main__":
    remove_outlier()