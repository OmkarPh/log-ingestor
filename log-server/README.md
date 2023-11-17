## Steps:


Ensure Go & Python are installed

Install golang dependencies
`go mod download`

Install Python dependencies
`pip install -r requirements.txt`


Local kafka instance (Optional)

Start zookeepr
`zookeeper-server-start /opt/homebrew/etc/zookeeper/zoo.cfg`

Start kafka server
`kafka-server-start /opt/homebrew/etc/kafka/server.properties`

Run server using:
`go run cmd/server.go`
