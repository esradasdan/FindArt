## FindArt


FindArt is an artificial intelligence themed website. Image Classification by ModelArts from Huawei Cloud services was used to estimate painters from classical period paintings on this site.

The main purpose of the project is to guess which painter is a picture you upload to the site and to provide artificial intelligence service. It also gives a brief information about the artist shown as a result and shows the accuracy rate of the result. This website was built with Python's Django library used for website development and distributed with Huawei Services.


The data consists of 50 painters and approximation 8k tables.
Source: _https://www.kaggle.com/code/supratimhaldar/deepartist-identify-artist-from-art/data_

The storage of the data is done with OBS from Huawei Cloud services, and the training is done with Modelarts-ExeML. The created service was accessed through the API in the views.py file.

<img width="362" alt="image" src="https://user-images.githubusercontent.com/70915939/207943074-fb4c3d09-e609-4096-af78-921ccf21bb9d.png"> <img width="372" alt="image" src="https://user-images.githubusercontent.com/70915939/207943107-5d6f9e2b-3f54-4389-bcae-92724ac15fcf.png">
