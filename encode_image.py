import base64
with open('G:/Claude Apps/Vital Signs Trainer/Jeffrey.png', 'rb') as f:
    data = f.read()
b64 = base64.b64encode(data).decode('utf-8')
result = 'data:image/png;base64,' + b64
with open('G:/Claude Apps/Vital Signs Trainer/encoded_output.txt', 'w') as out:
    out.write(result)
print('Done. Length:', len(result))
