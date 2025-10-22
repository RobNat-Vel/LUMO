"""Script para enviar un mensaje de prueba a través de la API de WhatsApp Business."""
"""
import requests

ACCESS_TOKEN = "EAAV40UXwZCEQBP0kOZANdOSqoJuaHyziZB2InIvZBJmGBqpfbZA1ZAzQ5RhgqlMdZAhYS8ZArNwWI91tCg91umKhkYIcatbeHAJIYOIeYJSL588qj4vr2ErXIL1ZA6RSXvLwqSwhl420RZAeUWwFlHgVqsZBEtkkzNgEzGOZCb9JOkS90avJpNXlCU26wJqhvaGJDiivuSMZAKWgZAr4cDe2ZA4qf5FqnDnnkvPcGsqUza5yrUir7sZD"
PHONE_NUMBER_ID = "848865624980629"
TO = "5217779864080"

url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": TO,
    "type": "text",
    "text": {"body": "Mensaje enviado desde Python ✅"}
}

r = requests.post(url, headers=headers, json=data)
print(r.status_code, r.text)
"""
# Código mejorado con mensajes de depuración
import requests

ACCESS_TOKEN = "EAAV40UXwZCEQBPyvMgHqKuFJN6qViuiWBYfj9RnaUNMEkfGUWK2FtOegDdSm1yq7HHQGakQgvVh4R0ZBfyQH9sNZB8frnnaKZAC6VRWptK0J5Az9vZClZAR0W6rmPuvFvgnofCNWVEqYEcdgNDwekBbgV3mSZAYye6TvuZBXaoXHjdp7dNDB1h7dcg4ZC8Do0fqaHPcgMBV5WZAXZBFewRJTfmzZAoQquN2Oz2l0ruqWLzkYMQZDZD"
PHONE_NUMBER_ID = "848865624980629"
TO = "5217779864080"

url = f"https://graph.facebook.com/v21.0/{PHONE_NUMBER_ID}/messages"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": TO,
    "type": "text",
    "text": {"body": "Mensaje personalizado desde Python ✅"}
}

print("🔍 URL:", url)
print("🔍 Encabezados:", headers)

r = requests.post(url, headers=headers, json=data)
print("🔍 Código de respuesta:", r.status_code)
print("🔍 Respuesta completa:", r.text)
