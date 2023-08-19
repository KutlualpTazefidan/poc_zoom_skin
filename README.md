# poc_zoom_skin

Building an end-to-end machine learning solution for the classification of skin diseases.

My Journey to the Top 10 of ML Engineers
Project 1

Goals:

1. Simple implementation using MobileNetv1 using Keras
2. Simple implementation using MobileNetv3 using Pytorch
3. Comparing models
4. Making web app.

Data:

I'll try to use the following data set:

@data{DVN/DBW86T_2018,
author = {Tschandl, Philipp},
publisher = {Harvard Dataverse},
title = {{The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions}},
UNF = {UNF:6:KCZFcBLiFE5ObWcTc2ZBOA==},
year = {2018},
version = {V4},
doi = {10.7910/DVN/DBW86T},
url = {https://doi.org/10.7910/DVN/DBW86T}
}

Installation notes:

- setting up wsl2 :
  https://www.youtube.com/watch?v=1HzYU2_t3yc&ab_channel=Archive
- switched using anaconda
- Using wsl2 and following this to install cuda with graphics support:
  https://www.youtube.com/watch?v=0S81koZpwPA&ab_channel=JeffHeaton

- https://www.tensorflow.org/install/pip#windows-wsl2
- Be aware of tensorflow compatibiltiy with cuda

Short cuts:
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
