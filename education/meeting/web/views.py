# Create your views here.
from django.http import HttpRequest
import urllib
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.user import authenticate
from pyamf.remoting.gateway.wsgi import WSGIGateway
from pyamf.remoting.gateway import django
from django.shortcuts import render_to_response
import django.settings
import flashticle
    
#from flashticle import wsgigateway
from cgi import parse_qsl
import struct
import socket

django.settings.TEMPLATE_DIRS += (os.path.expanduser('~/Developer/Projects/University/education/meeting/web/templates'),)
assert False, django.settings.TEMPLATE_DIRS

def echo(data):
    return data

def stream_bytes(fp,num_bytes=1024):
    fp.write(num_bytes)

def stream_file(fp):
    while (fp.has_more_data):
        stream_bytes(fp,1024)

services = {
    'myservice.echo': echo,
    'educationserver.data': echo,
    }

def meeting(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/login/success/')
        else:
            return HttpResponseRedirect('/login/disabled_account/')
    else:
        return HttpResponse('/login/invalid_account/')

def logout_user(request):
    logout(user)
    return HttpResponseRedirect('/action/loggedout')

def videoplayer(request):
    qs = request.GET.copy()
    context = {'classid':'clsid:d27cdb6e-ae6d-11cf-96b8-444553540000',
               'width': '300',
               'height': '400',
               'id': 'videoplayer',
               'movie_src_path': 'http://localhost:9000/assets/VideoPlayer.swf',
               'security_settings': 'always'}
    return render_to_response('flashobject.xml',context,
                              context_instance=RequestContext(request))

def embed(request):
    qs = request.GET.copy()
    context = {}
    context['classid'] = urllib.unquote(qs['cli'])
    context['width'] = qs['w']
    context['height'] = qs['h']
    context['id'] = qs['i']
    context['movie_src_path'] = urllib.unquote(qs['v'])
    if qs['ss'][0] == 'sd':
        context['security_settings'] = 'sameDomain'
    if qs['ss'][0] == 'a':
        context['security_settings'] = 'always'
    return render_to_response('flashobject.xml',context,
                              context_instance=RequestContext(request))

@login_required(login_url='/login/user/login')
def application(request):
    config = {}
    #gateway = wsgigateway.FlashRemotingGateway(config)
    request.headers = request.META
    #process_body = gateway.get_processor(request)
    return HttpResponse(Template('''
    <!DOCTYPE HTML>
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"
    xmlns:v="urn:schemas-microsoft-com:vml"
    >
    <head>
    <meta content="IE=EmulateIE7" http-equiv="X-UA-Compatible"/>
    <meta http-equiv="cache-control" content="no-cache"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <link rel="stylesheet" type="text/css" href="/wbstyles.css"/>
    <script type="text/javascript" src="jquery-1.2.6.min.js"></script>
    <script type="text/javascript" src="AC_OETags.min.js"></script>
    <script type="text/javascript" src="AC_RunActiveContent.js"></script>
    <script type="text/javascript" src="wb.min.js"></script>
    </head>
    <h1>The Virtual Whiteboard</h1>
    <div class="whiteboard">
    <a href="/amf/crossdomain.xml"></a>
    <object src="/amf/whiteboard/">
    </object>
    </div>


<div class="whiteboard">

<html>
<head>
<body bgcolor="#ffffff">
<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
        width="400"
    height="300"
    id="haxe"
    align="middle">
<param name="movie" value="ht/test.swf"/>
<param name="allowScriptAccess" value="always" />
<param name="quality" value="high" />
<param name="scale" value="noscale" />
<param name="salign" value="lt" />
<param name="bgcolor" value="#ffffff"/>
<embed src="ht/test.swf"
       bgcolor="#ffffff"
       width="400"
       height="300"
       name="haxe"
       quality="high"
       align="middle"
       allowScriptAccess="always"
       type="application/x-shockwave-flash"
       pluginspage="http://www.macromedia.com/go/getflashplayer"
/>
</object>

</div> <!-- whiteboard -->
</div>



<div class="chat">
<input type="text" id="chat-input" width="1000"/>
</div>


<div class="play-video-section">
<form id="video-play" method="get" name="video-play">
<input type="text" id="video-play-name" width="800"/>
<input type="submit" id="video-play-button" value="Play">
</form>
</div>



<div class="submit-lecture-section">
<form id="video-submit" method="post">
<input type="text" id="video-submit-name" width="800"/>

<input type="submit" id="video-submit-button" value="Submit Lecture">
</form>
<div class="students_online">
Students currently online:
</div> <!-- [@students_online] -->
</body>
</html>
</div>
    </html>
    ''').render(RequestContext(
        request,{
'movie_link': urllib.urlencode(
{'cli': urllib.quote('clsid:d27cdb6e-ae6d-11cf-96b8-444553540001'),
    'w':'400',
    'h':'300',
    'i':'haxe',
    'ss':'a',
    'v':urllib.quote('http://localhost:9000/assets/test.swf')}),
'player_link': urllib.urlencode(
    {'cli': urllib.quote('clsid:d27cdb6e-ae6d-11cf-96b8-444553540002'),
     'w': '400',
     'h': '300',
     'i': 'VideoPlayer',
     'ss':'a',
     'v': urllib.quote('ht/bin-debug/VideoPlayer.swf')}),
'main_link': urllib.urlencode(
    {'cli': urllib.quote('clsid:d27cdb6e-ae6d-11cf-96b8-444553540003'),
     'w': '400',
     'h': '300',
     'i': 'main_player',
     'ss':'a',
     'v': urllib.quote('http://localhost:9000/assets/main.swf')})
})
))

def gateway_server(req):
    pass
