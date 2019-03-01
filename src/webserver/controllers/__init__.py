
# handles
def controller(urlparsed, srv):
    srv.wfile.write(str.encode("%s request: %s" % (srv.command, str(urlparsed))))
