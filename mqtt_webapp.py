import streamlit as st
import paho.mqtt.client as mqtt

# MQTT Settings
broker = "broker.hivemq.com"
port = 1883
topic = "lumishue/MAHESH/control"

# MQTT Setup
client = mqtt.Client()
client.connect(broker, port, 60)
client.loop_start()

def send_command(command):
    client.publish(topic, command)
    st.success(f"✅ Sent: {command}")

# Streamlit UI
st.set_page_config(page_title="Lumishue Controller", layout="centered")
st.title("🟡 Lumishue ESP32 Controller")
st.markdown("Control your ESP32 LED modes via MQTT")

st.divider()
col1, col2 = st.columns(2)

with col1:
    if st.button("🌇 Sunset Mode"):
        send_command("sunset")
    if st.button("🌙 Moonlight Mode"):
        send_command("moonlight")
    if st.button("🌿 Nature Mode"):
        send_command("nature")

with col2:
    if st.button("🍒 Cherry Mode"):
        send_command("cherry")
    if st.button("🎲 Shuffle ON"):
        send_command("shuffle_on")
    if st.button("❌ Shuffle OFF"):
        send_command("shuffle_off")

st.divider()
if st.button("🔌 Disconnect"):
    client.loop_stop()
    client.disconnect()
    st.warning("Disconnected from MQTT broker")
