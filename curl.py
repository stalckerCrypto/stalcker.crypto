import pycurl
import StringIO

response = StringIO.StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere')
c.setopt(c.WRITEFUNCTION, response.write)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept-Charset: UTF-8'])
c.setopt(c.POSTFIELDS, '@request.json')
c.perform()
c.close()
print response.getvalue()
response.close()
