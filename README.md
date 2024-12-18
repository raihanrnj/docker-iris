## A Simple IRIS Flower Classification Model Deployment project 

The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.


## Building a Docker Image

```
 git clone https://github.com/raihanrnj/docker-iris
 cd docker-iris 
 docker image build -t raihanrnj/docker-iris:1.0.0 . 
```


## Running the  container 

```
 docker run --rm --name docker-iris -p 8080:8080 -d raihanrnj/docker-iris:1.0.0  ` 
```

## Accessing the app

Open browser http://localhost:8080/




