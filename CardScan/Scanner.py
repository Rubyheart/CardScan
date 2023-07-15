import easyocr
reader = easyocr.Reader(['en'])
Result = reader.readtext('Oathsworn.jpg')
print(Result)