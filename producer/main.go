// package main

// import (
// 	"fmt"
// 	"html"
// 	"log"
// 	"net/http"
// )

// func main() {

// 	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
// 		fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
// 	})

// 	http.HandleFunc("/hi", func(w http.ResponseWriter, r *http.Request) {
// 		fmt.Fprintf(w, "Hi")
// 	})

// 	log.Fatal(http.ListenAndServe(":8081", nil))

// }

package main

import (
	"encoding/json"
	"log"
	"time"

	"github.com/Shopify/sarama"
	kingpin "gopkg.in/alecthomas/kingpin.v2"
)

type person struct {
	name string
	age  int
}

var (
	brokerList = kingpin.Flag("brokerList", "List of brokers to connect").Default("localhost:29092").Strings()
	topic      = kingpin.Flag("topic", "Topic name").Default("important").String()
	maxRetry   = kingpin.Flag("maxRetry", "Retry limit").Default("5").Int()
)

func main() {

	kingpin.Parse()
	config := sarama.NewConfig()
	config.Producer.RequiredAcks = sarama.WaitForAll
	config.Producer.Retry.Max = *maxRetry
	config.Producer.Return.Successes = true
	producer, err := sarama.NewSyncProducer(*brokerList, config)
	if err != nil {
		log.Panic(err)
	}
	defer func() {
		if err := producer.Close(); err != nil {
			log.Panic(err)
		}
	}()
	s := person{name: "Sean", age: 50}
	// msg := &sarama.ProducerMessage{
	// 	Topic: *topic,
	// 	Value: sarama.StringEncoder("Something Coola"),
	// }
	b, err := json.Marshal(s)
	msg := &sarama.ProducerMessage{
		Topic: *topic,
		Value: b,
	}

	for {
		partition, offset, err := producer.SendMessage(msg)
		if err != nil {
			log.Panic(err)
		}
		log.Printf("Message is stored in topic(%s)/partition(%d)/offset(%d)\n", *topic, partition, offset)
		time.Sleep(5 * time.Second)

	}
}
