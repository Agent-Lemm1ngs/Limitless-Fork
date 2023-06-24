import os
try:
  import quart
except:
  os.system("pip install quart")
  import quart
from quart import Quart,redirect,render_template

print("Started")

app = Quart(__name__ )#,static_url_path='/static')



@app.route('/')
async def home():
  return "hi"


app.run(debug=True,host="0.0.0.0",port=8080)
