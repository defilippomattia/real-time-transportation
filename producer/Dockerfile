## We specify the base image we need for our
## go application
#docker pull golang:1.18.0-alpine3.14
FROM golang:1.17.0-alpine3.14
## We create an /app directory within our
## image that will hold our application source
## files
RUN apk add git

RUN mkdir /app
## We copy everything in the root directory
## into our /app directory
ADD . /app
## We specify that we now wish to execute 
## any further commands inside our /app
## directory

WORKDIR /app
RUN go mod init main
RUN go get gopkg.in/alecthomas/kingpin.v2
RUN go get -u github.com/Shopify/sarama

## we run go build to compile the binary
## executable of our Go program
RUN go env -w GO111MODULE=auto
RUN go mod tidy
RUN go build -o main .

## Our start command which kicks off
## our newly created binary executable
CMD ["/app/main"]