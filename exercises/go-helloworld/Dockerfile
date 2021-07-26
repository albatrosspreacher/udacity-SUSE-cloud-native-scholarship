FROM golang:alpine
COPY . /go/src/app
WORKDIR /go/src/app
RUN go build -o helloworld
CMD ["./helloworld"]