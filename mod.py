import torch
from torchvision import transforms, datasets
import torchvision
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from pynput import keyboard
import pymem
import threading
import time
def get_arrow():
    transform = transforms.Compose(
            [transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    classes=("0","1","2","3")
    class CustomDataset(Dataset):
        def __init__(self, img_folder, label_file, transform=None):
            self.img_folder = "./arrow_pic"
            self.transform = transform

            # Read labels
            with open("label.txt", 'r') as f:
                lines = f.readlines()
            self.img_names = [line.split()[0] for line in lines]
            self.labels = [int(line.split()[1]) for line in lines]

        def __len__(self):
            return len(self.img_names)

        def __getitem__(self, idx):
            img_path = os.path.join(self.img_folder, self.img_names[idx])
            image = Image.open(img_path).convert('RGB')
            label = self.labels[idx]

            if self.transform:
                image = self.transform(image)

            return image, label

    dataset = CustomDataset(img_folder='./arrow_pic', label_file='', transform=transform)
    trainloader = DataLoader(dataset, batch_size=4, shuffle=False)
    dataiter = iter(trainloader)
    images, labels = next(dataiter)
    import torch
    import torch.nn as nn
    import torch.nn.functional as F

    class Net(nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = nn.Conv2d(3, 6, kernel_size=5, stride=1, padding=2)  
            self.pool = nn.MaxPool2d(kernel_size=2, stride=2)  
            self.conv2 = nn.Conv2d(6, 16, kernel_size=5, stride=1, padding=2)  
            self.fc1 = nn.Linear(16 * 32 * 32, 120)  
            self.fc2 = nn.Linear(120, 84)
            self.fc3 = nn.Linear(84, 4)

        def forward(self, x):
            x = self.pool(F.relu(self.conv1(x)))
            x = self.pool(F.relu(self.conv2(x)))
            x = torch.flatten(x, 1)
            x = F.relu(self.fc1(x))
            x = F.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    def imshow(img):
        img = img / 2 + 0.5     # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()
    net = Net()
    net.load_state_dict(torch.load('arrow_rune.pth'))
    net.eval()
    outputs=net(images)
    _, predicted = torch.max(outputs, 1)
    imshow(torchvision.utils.make_grid(images))

    _, predicted = torch.max(outputs, 1)

    arrow_list=[]
    for j in range(4):
        arrow_list.append(int((classes[predicted[j]])))
    return arrow_list
print(get_arrow())
"""
def get_rune_status():
    while True:
        p=pymem.Pymem("MapleStory.exe")
        if p.read_int(0x13FFF0D16) == 1:
            r=get_arrow()
            print(r)
            # p.write_int(0x13FFF0800,r[0])
            # p.write_int(0x13FFF0804,r[1])
            # p.write_int(0x13FFF0808,r[2])
            # p.write_int(0x13FFF080C,r[3])
            # p.write_int(0x13FFF0D16,0)
        time.sleep(0.1)
threading.Thread(target=get_rune_status).start()
global s
s=0


def p(switch):
    p=pymem.Pymem("MapleStory.exe")
    p.write_int(0x13FFF0810,switch)
    p.write_int(0x13FFF0840,switch)
    p.write_int(0x13FFF0CF0,switch)
    p.close_process()
        
def on_press(key):
    if key == keyboard.Key.f3:
        global s
        if s==0:
            p(1)
            s=1
        else:
            p(0)
            s=0

        
def on_release(key):
    pass

listener=keyboard.Listener(on_press=on_press,on_release=on_release)
listener.daemon=True
listener.start()
"""