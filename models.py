## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I
       
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 4)
          
        self.pool1 = nn.MaxPool2d(2, 2)
    
        self.conv1_drop = nn.Dropout(p=0.4)
        
        self.conv2 = nn.Conv2d(32, 64, 3)
        
        self.pool2 = nn.MaxPool2d(2, 2)
        
        self.conv2_drop = nn.Dropout(p=0.4)
        
        self.conv3 = nn.Conv2d(64, 128, 2)
        
        self.pool3 = nn.MaxPool2d(2, 2)
        
        self.conv3_drop = nn.Dropout(p=0.4)
        
        self.conv4 = nn.Conv2d(128, 200, 1)
        
        self.conv4_bn = nn.BatchNorm2d(200)
        
        self.pool4 = nn.MaxPool2d(2, 2)
        
        self.conv4_drop = nn.Dropout(p=0.4)

        self.conv5 = nn.Conv2d(200, 256, 1)
        
        self.conv5_bn = nn.BatchNorm2d(256)
        
        self.pool5 = nn.MaxPool2d(2, 2)
        
        self.conv5_drop = nn.Dropout(p=0.3)

        self.fc1 = nn.Linear(256*6*6,1000)
        
        self.fc1_bn = nn.BatchNorm1d(1000)
        
        self.fc1_drop = nn.Dropout(p=0.4)
        
        self.fc2 = nn.Linear(1000, 1000)
        
        self.fc2_bn = nn.BatchNorm1d(1000)
        
        self.fc2_drop = nn.Dropout(p=0.3)
        
        self.fc3 = nn.Linear(1000, 800)
        
        self.fc3_bn = nn.BatchNorm1d(800)
        
        self.fc3_drop = nn.Dropout(p=0.2)

        self.fc4 = nn.Linear(800, 136)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.conv1_drop(x)
        x = self.pool2(F.relu(self.conv2(x)))
        x = self.conv2_drop(x)
        x = self.pool3(F.relu(self.conv3(x)))
        x = self.conv3_drop(x)
        x = self.pool4(F.relu(self.conv4_bn(self.conv4(x))))
        x = self.conv4_drop(x)
        x = self.pool5(F.relu(self.conv5_bn(self.conv5(x))))
        x = self.conv5_drop(x)
        x = x.view(x.size(0),-1)
        x = F.relu(self.fc1_bn(self.fc1(x)))
        x = self.fc1_drop(x)
        x = F.relu(self.fc2_bn(self.fc2(x)))
        x = self.fc2_drop(x)
        x = F.relu(self.fc3_bn(self.fc3(x)))
        x = self.fc3_drop(x)
       
        x = self.fc4(x)    
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
