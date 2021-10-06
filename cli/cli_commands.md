# Kafka CLI Tools
This exercise is about using the Kafka CLI Commands

## Listing topics
First, let's see how to list topics that already exist within Kafka.  
`./kafka-topics.sh --list --bootstrap-server localhost:9092`   
The `--list` switch tells the `kafka-topics` CLI to list all known topics.
if you are using an older version of Kafka then `--bootstrap-server localhost:9092` needs to be replaced with `--zookeeper localhost:2181` 
  
We haven't created any topics yet, so what you're seeing are system topics that Kafka and other
Kafka ecosystem tools make use of.

## Creating topics

Now that we've seen what topics exist, let's create one.

`./kafka-topics.sh --create --topic "my-first-topic" --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092`

When you run this command it should silently exit after a few moments.

The switch `--topic "my-first-topic"` tells Kafka what to name the topic

The switch `--partitions 1` and the switch `--replication-factor 1` are required configuration
which we will explore more.


## Producing data

Now that we have a topic, let's add some data.

`./kafka-console-producer.sh --topic "my-first-topic" --broker-list PLAINTEXT://localhost:9092`

The switch `--broker-list` tells the tool where to find Kafka.

When you hit enter, you should be dropped into an interactive terminal.

Try typing out a few messages and hitting enter.

## Consuming data

While it's great that we've produced data, it would be more exciting if we could see it being
consumed.

Open a new terminal tab and run the following command:

`./kafka-console-consumer.sh --topic "my-first-topic" --bootstrap-server PLAINTEXT://localhost:9092`

Notice that nothing prints out? Remember that by default Kafka doesn't provide historical messages to new consumers. Return to the producer and enter a few new messages. You should see them come across the screen!

Hit `Ctrl+C` to exit the consumer. Let's try this again, but ask Kafka to provide all the messages that have been published to the topic:

`./kafka-console-consumer.sh --topic "my-first-topic" --bootstrap-server PLAINTEXT://localhost:9092 --from-beginning`

The `--from-beginning` switch tells `kafka-console-consumer` to read data from the beginning of the topic, not just data from when we connect.

You should now see output that includes all of the messages you've produced:



## Deleting topics

Now that we've explored working with the CLI tools, let's clean up our topic.

`./kafka-topics.sh --delete --topic "my-first-topic" --bootstrap-server localhost:9092`

This command is nearly identical to the `--create` command from earlier, except now we're calling the
command with the `--delete` switch instead.

This command does not print any output if it's successful. To check that your topic is actually deleted, list the topics one more time:

`./kafka-topics.sh --list --bootstrap-server localhost:9092`

`my-first-topic` should no longer appear in the list of topics.

