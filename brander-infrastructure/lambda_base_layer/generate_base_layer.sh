#Generates a base layer for the Lambda function

#Remove the container first (if it already exists)
docker rm layer-container

#Build the base layer
docker build -t base-layer .

#Rename it to layer-container
docker run --name layer-container base-layer

#Copy the generated zip artifact so the CDK can use it
docker cp layer-container:layer.zip . && echo "Created layer.zip with updated base layer."