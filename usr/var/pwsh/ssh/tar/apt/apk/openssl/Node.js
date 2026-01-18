const https = require("https");
const fs = require("fs");

https.createServer({
  key: fs.readFileSync("privkey.pem"),
  cert: fs.readFileSync("fullchain.pem")
}, app).listen(443);
