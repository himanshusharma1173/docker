#Base Image
FROM ubuntu AS build

RUN apt-get update && apt-get install -y golang-go

#ENV GO111MODULE=Off

COPY . .

RUN CGO_ENABLED=0 go build -o /app .

#Multi Stage Build
FROM scratch

#Copy compiled binary from build stage
COPY --from=build /app /app

#EntryPoint for the conatiner to run the binary
ENTRYPOINT ["/app"]
