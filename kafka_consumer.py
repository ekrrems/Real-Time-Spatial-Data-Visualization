from kafka import KafkaConsumer
from text_to_coordinates import address_to_coordinates
import folium
import json
import psycopg2

# Connect to Postgresql Database
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='location_db',
    user='postgres',
    password='Adanali_01'
)

cur = conn.cursor()

def data_to_postgresql(message):
    """
    Add kafka topic data to Postgresql 
    """
    lat, long = address_to_coordinates(message["location"])
    query = f"INSERT INTO locations (name, date, latitude, longitude) VALUES ('{message['name']}', '{message['date']}', {lat}, {long});"

    try:
    # Execute the SQL query with the data
        cur.execute(query)
    
    # Commit the transaction to make the changes persistent
        conn.commit()
    
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
        conn.rollback()


# Create a Folium Map to Visualize the data 
map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)


# Create a function to add markers
def add_marker(msg):
    lat, long = address_to_coordinates(msg["location"])
    label = msg["name"]
    marker = folium.Marker(location=[lat, long], popup=label)
    marker.add_to(map)
    map.fit_bounds([[lat, long]])
    map.save("map.html")
    # Run "python -m http.server" on terminal


bootstrap_servers = 'localhost:9092'  # Replace with your Kafka broker(s) address
topic = 'location-topic' 

consumer = KafkaConsumer(topic, 
                         bootstrap_servers=bootstrap_servers)

try:
    for message in consumer:
        received_msg = json.loads(message.value.decode("utf-8"))
        data_to_postgresql(received_msg)
        add_marker(received_msg)
        
        print(f'Received message: {(received_msg["name"])}, {received_msg["location"]}')
except Exception as e:
    print(f'Error occurred: {e}')

consumer.close()
cur.close()
conn.close()

# C:\kafka>bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic location-topic --from-beginning


