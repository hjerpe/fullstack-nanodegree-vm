from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from Database.TableHandler import TableHandler
from get_connection_string import get_connection_string
import cgi


def get_form_string(ind):
    op_string = "<form method='POST' enctype='multipart/form-data'"
    op_string += ''' action='/tablenames'> <input name="message%s" type="text" > 
                        <input type="submit" value="Submit"> </form>''' % (ind)
    return op_string


class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = "<html><body>"
                output += "<h1>Hello!</h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'>
                        <h2>What would you like me to say?</h2> 
                        <input name="message" type="text" >  
                        <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"

                self.wfile.write(output)
                print(output)

            elif self.path.endswith("/goddag"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = "<html><body>"
                output += "<h1>Tj&#228;na! <a href = '/hello'></br>Back to Hello</a></h1>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'> 
                        <h2>What would you like me to say?</h2> 
                        <input name="message" type="text" >
                                <input type="submit" value="Submit"> </form>'''
                output += "</body></html>"

                self.wfile.write(output)
                print(output)

            elif self.path.endswith("/tablenames"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                output = "<html><body>"
                output += "<h1>Tj&#228;na! <a href = '/hello'></br>Back to Hello</a></h1>"
                output += '<table><tr><th>Resturant</th></tr>'
                tableHandler = TableHandler(get_connection_string())

                for ind, name in enumerate(tableHandler.get_row_names()):
                    output += '<tr><td>{name}</td><td>{form}</td></tr>'.\
                            format(name=name,
                                    form=get_form_string(ind))
                output += '</table>'
                output += "</body></html>"

                self.wfile.write(output)

            return

        except IOError:
            self.send_error(404, 'File Not Found %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            print('ctype: %s' % ctype)
            print('pdict %s' % pdict)

            form = cgi.FieldStorage()
            print('form {f}'.format(f=form))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                key = fields.keys()[0]
                if key[-1].isdigit():
                    arr_ind = key[-1]
                    print('index to alter db row found')

                messagecontent = fields.get(key)
                print('fields: %s' % fields)
                print('inside ctype')
                print(messagecontent)

            print('outside ctype')
            output = "<html><body>"
            output += "<h2> As you wish! </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]

            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print(output)

        except:
            pass


def main():
    try:
        port = 1234
        server = HTTPServer(('', port), webserverHandler)
        print 'Web server running on port %s' % port
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C entered, stopping web server...'
        server.socket.close()


if __name__ == '__main__':
    main()
