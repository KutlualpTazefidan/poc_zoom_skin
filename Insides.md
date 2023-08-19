Some insides to the project:

The goal is to have NN which computationally light so it can be used locally on mobile devices.
It saves energy resources, expands the user base and provides privacy, because of the local storage.

MobileNet architecture allows complete tensor operations on a mobile device

Understanding convolution / advantage of using depthwise and pointwise convolution:

An image of size 1024x1024x3 (three color channels) with a filter of kernel size 10x10x3.
The first pixel of the image is multiplied with first pixel of the filter for each 3 layers and added together.
Number of mutiplications: 10x10x3 for each 1024x1024 pixels -> 10x10x3x1024x1024 300x1050000 -> 300,000,000 for one filter /
For 250 outputs : 300,000,000 \* 250 -> 75,000,000,000 75 billion operations
The goal is the reduction of computationally heavy multiplication operations.

To reduce the number of operations, it's divided into depthwise and pointwise convolution

depthwise convolution:
The depth of the filter and the image is seperated. 10x10x1 and 1024x1024x1.
These are multiplied seperately -> (10x10x1024x1024)\*3 = 300,000,000 and then apply BN and RELU

pointwise convolution:
Filter is divided into 1x1x3, so is multiplied to each layer and added together, and repeated along the image 1024x1024
-> 3 \* 1,000,000 = 3,000,000 applying BN and RELU
for 256 layers = 750,0000,000

total: 1,000,000,000
75 times less operations

State of the art for the mobilenet:
https://www.youtube.com/watch?v=0oqs-inp7sA&ab_channel=MaciejBalawejder
