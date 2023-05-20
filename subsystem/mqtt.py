import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

on_message_suhu = on_message_mqtt('Suhu')
on_message_kelembaban = on_message_mqtt('Kelembaban')
on_message_cahaya = on_message_mqtt('Cahaya')

client = mqtt.Client()
client.message_callback_add('uas/pabriksmartfarm/suhu', on_message_suhu)
client.message_callback_add('uas/pabriksmartfarm/kelembaban', on_message_kelembaban)
client.message_callback_add('uas/pabriksmartfarm/cahaya', on_message_cahaya)

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
client.subscribe("uas/pabriksmartfarm/#")
client.loop_start()
