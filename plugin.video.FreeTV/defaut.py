#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

##############BIBLIOTECAS A IMPORTAR E DEFINICOES####################

import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,HTMLParser,os,base64, hashlib
from BeautifulSoup import BeautifulStoneSoup, BeautifulSoup, BeautifulSOAP
from BeautifulSoup import BeautifulSoup
h = HTMLParser.HTMLParser()

versao = '1.0.1'
addon_id = 'plugin.video.FreeTV'
selfAddon = xbmcaddon.Addon(id=addon_id)
__ALERTA__ = xbmcgui.Dialog().ok
addonfolder = selfAddon.getAddonInfo('path')
artfolder = addonfolder + '/resources/img/'
fanart = addonfolder + '/fanart.png'
url_base = base64.b64decode('aHR0cDovL3R2LW1zbi5jb20vbWVzdHJlLnBocA==')
url_base2 = base64.b64decode('aHR0cDovL3R2LW1zbi5jb20vY2FuYWlzLmh0bWw=')
url_base3 = base64.b64decode('aHR0cDovL3d3dy50di1tc24uY29tL3BsYXllci9wbGF5ZXIuc3dm')
url_base4 = base64.b64decode('aHR0cHM6Ly9jb3B5LmNvbS9oWjJFbU1YZnROdTRSV3oxP2Rvd25sb2FkPTE=')
url_base5 = base64.b64decode('aHR0cDovL3d3dy5hb3Zpdm9icmFzaWwuY29tL3R2YW1pZ29zMi8=')
url_base6 = base64.b64decode('aHR0cDovL3d3dy5jYXJvbGluZW9saXZlaXJhLmNvbS5ici9zd2YvcGxheWVyLnN3Zg==')

##################################################Login#############################################

###################################################MENUS############################################

def  menus():        		
	dialog = xbmcgui.Dialog()
	addDir('[B]Canais TV[/B]','-',2,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
	addDir('[B]Canais TDT[/B]','-',3,'http://pplware.sapo.pt/wp-content/uploads/2015/11/tdt_01.jpg')
	addDir('Este addon é Free nao somos obrigados a ter nada a funcionar','',2,'http://1.bp.blogspot.com/-egfHu9j4ueo/Uc3dLWyvHbI/AAAAAAAAAV4/vTI8bRsQKZs/s600/Alert-Icon-.png')
	
def  categorias():
	check_login = login()
	if check_login:
		addDir('[B]Eventos[/B]','http://pastebin.com/raw/JSxSwLgT',4,'http://lininatural.com/wp-content/uploads/2015/01/Coming-Soon1.jpg')
		addDir('[B]Portugueses[/B]','http://pastebin.com/raw/cHKGyc3b',4,'http://i1107.photobucket.com/albums/h398/foxtv1/www-tvportugal-tv_zps65da811b.jpg')
		addDir('[B]Desporto[/B]','http://pastebin.com/raw/6KqM4GPK',4,'http://3.bp.blogspot.com/-bizrWLIjDLM/UD82C_FF2pI/AAAAAAAACsw/Ok4SjScgQrU/s1600/desporto.png')
		addDir('[B]Musica[/B]','http://pastebin.com/raw/b5DMRw2a',4,'http://www.imagenstop.blog.br/wp-content/gallery/imagens-de-musica/Imagem-de-Musica-para-Baixar.jpg')
		addDir('[B]Documentários[/B]','http://pastebin.com/raw/e3uUs6Un',4,'http://comps.canstockphoto.com/can-stock-photo_csp20747163.jpg')
		addDir('[B]Filmes[/B]','http://pastebin.com/raw/LWPyktJM',4,'https://catracalivre.com.br/wp-content/uploads/2011/08/hist%C3%B3rias-que-ficam-reprodu%C3%A7%C3%A3o.jpg')
		addDir('[B]Infantil[/B]','http://pastebin.com/raw/6WYJVjxb',4,'https://lh5.googleusercontent.com/-yzHm4QdLxTM/AAAAAAAAAAI/AAAAAAAAABI/Red-UDwV8rQ/photo.jpg')
		addDir('[B]Praias[/B]','http://pastebin.com/raw/3EAp4y6X',4,'http://thumbs.dreamstime.com/x/beach-sunset-logo-sun-sets-scene-peaceful-icon-37222618.jpg')
		addDir('[B]Radios[/B]','http://pastebin.com/raw/cxRAFP5M',4,'http://www.burningnightscrps.org/wp-content/uploads/2015/02/Listen-Online-Radio-icon.jpg')
		addDir('[B]Futebol No Estrangeiro[/B]','http://pastebin.com/raw/Y5MLLGLk',4,'https://www.gvt.com.br/Portal%20GVT/_ArquivosEstaticos/area-aberta/_imagens/bg/bg-canais-internacionais.png')
	else:
		addDir('[B]Alterar Definições[/B]','http://pastebin.com/raw/JSxSwLgT',1000,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
		addDir('[B]Entrar novamente[/B]','',None,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
	    
def categorias_amigos():
		addDir('TDT Portugal','http://tinyurl.com/zzux5dy',4,'http://www.atelevisao.com/wp-content/uploads/2013/09/imagesCA7P4VOJ.jpg')
############################################################### Login ####################################################

def login():
	if selfAddon.getSetting("login_name") == '' or selfAddon.getSetting('login_password') == '':
		__ALERTA__('FreeTV', 'Precisa de definir o seu username e password')
		return False
	else:
		if hashlib.md5(hashlib.md5(selfAddon.getSetting("login_name")).hexdigest()).hexdigest() == "26bed7c30333e013b6d23a80710b53eb" and hashlib.md5(hashlib.md5(selfAddon.getSetting("login_password")).hexdigest()).hexdigest() == "716393fd345d40f5646041362f0308a8":
			return True
		else:
			return False
		
###############################################################FKav####################################################
def listar_canais(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2].replace(' rtmp','rtmp').replace(' rtsp','rtsp').replace(' http','http')
                  print 'Link: ' + rtmp
                  addLink(nome,rtmp,img)
            except:
                  pass
      xbmc.executebuiltin("Container.SetViewMode(500)")		
		
def listar_videostxt(url):
      for line in urllib2.urlopen(url).readlines():
            params = line.split(',')
            try:
                  nome = params[0]
                  print 'Nome: ' + nome
                  img = params[1].replace(' http','http')
                  print 'Img: ' + img
                  rtmp = params[2]
                  print 'Link: ' + rtmp
                  addDir(nome,rtmp,6,img,False)
            except:
                pass
		xbmc.executebuiltin("Container.SetViewMode(500)")

def player_youtube(url):
    #mera correção feita por Cleiton Leonel Creton!!!
	xbmcPlayer = xbmc.Player()
	xbmcPlayer.play('plugin://plugin.video.youtube/play/?video_id=' +url)

def listar_categorias():
	html = gethtml(url_base4)
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,8,iconimage)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodies')
	xbmc.executebuiltin('Container.SetViewMode(500)')	
	
def canais_master(name,url,iconimage):
	html = gethtml(url)
	soup = html.find("div",{"class":"canais"})
	canais = soup.findAll("li")
	for canal in canais:
		titulo = canal.a.text
		url = canal.a["href"]
		iconimage = canal.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,10,iconimage,False)
        xbmcplugin.setContent(int(sys.argv[1]), 'episodies')
	xbmc.executebuiltin('Container.SetViewMode(500)')
		
def series_e_desenhos_24hrs():
	html = gethtml(base64.b64decode('aHR0cHM6Ly9jb3B5LmNvbS82Y1ZYMmJQR0xzOFBjQ0xqP2Rvd25sb2FkPTE='))
	soup = html.find("div",{"class":"canais"})
	items = soup.findAll("li")
	for item in items:
		titulo = item.a.text
		url = item.a["href"]
		iconimage = item.img["src"]
		addDir("[B]"+titulo.encode('utf-8')+"[/B]",url,11,iconimage,False)
	xbmc.executebuiltin('Container.SetViewMode(500)')
	
def player_master(name,url,iconimage):
	status = xbmcgui.DialogProgress()
	status.create('ROGGER STREAM', 'Resolvendo link...','Por favor aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
		link = 'rtmp://'+ip+'/live?wmsAuthSign='+get_wms() +' playpath='+playpath+' swfUrl='+url_base3+' live=1 pageUrl='+url_base+' token='+gettoken() +' '
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		status.update(66)
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('ROGGER STREAM', 'Canal temporariamente indisponivel,desculpe o transtorno.')

def	player_series_e_desenhos_24hrs(name,url,iconimage):
	status = xbmcgui.DialogProgress()
	status.create('ROGGER STREAM', 'Resolvendo link...','Por favor aguarde...')
	playlist = xbmc.PlayList(1)
	playlist.clear()
	params = url.split(',')
	status.update(33)
	try:
		ip = params[0]
		playpath = params[1]
		directory = params[2]
		html = abrir_url(url_base5+directory)
		wmsAuthSign = re.compile('tvamigos(.+?)&autostart').findall(html)[0]
		link = 'rtmp://'+ip+wmsAuthSign+' playpath='+playpath+' swfUrl='+url_base6+' live=1 pageUrl='+url_base5+directory
		status.update(66)
		listitem = xbmcgui.ListItem(name,thumbnailImage=iconimage)
		listitem.setInfo("Video", {"Title":name})
		listitem.setProperty('mimetype', 'video/mp4')
		playlist.add(link,listitem)	
		xbmcPlayer = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
		xbmcPlayer.play(playlist)
		status.update(100)
		status.close()
	except:	
		xbmcgui.Dialog().ok('ROGGER STREAM', 'Conteudo temporariamente indisponivel,desculpe o transtorno.')	
	
##########################################################################################################################

def abrirDefinincoes():
    selfAddon.openSettings()
    addDir('Entrar novamente','url',None,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
	
def gethtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    soup = BeautifulSoup(link)
    return soup	

def real_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.geturl()
	response.close()
	return link

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

#def addDir(name,url,mode,iconimage,pasta=True,total=1):
	#u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	#ok=True
	#liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	#liz.setProperty('fanart_image', fanart)
	#ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	#return ok
	
def addDir(name,url,mode,iconimage,pasta=True,total=1,plot=''):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="iconimage", thumbnailImage=iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": plot})
	contextMenuItems = []
	contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=pasta,totalItems=total)
	return ok	
	
def get_wms():
	req = urllib2.Request(url_base)
	req.add_header('referer', url_base2)
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	wms = re.compile(r"AuthSign=(.+?)&auto").findall(link)[0]
	return wms	
	
def gettoken():
	req = urllib2.Request(base64.b64decode('aHR0cHM6Ly9jb3B5LmNvbS9LYjNSdnY4WnZIQmpOYVZsP2Rvd25sb2FkPTE='))
	response = urllib2.urlopen(req)
	token=response.read()
	response.close()
	return token	

############################################################################################################
#                                               GET PARAMS                                                 #
############################################################################################################

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
 
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

try:        
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass


print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Iconimage: "+str(iconimage)

###############################################################################################################
#                                                   MODOS                                                     #
###############################################################################################################

if mode==None or url==None or len(url)<1:
    print ""
    menus()
	
elif mode==2:
	print ""
	categorias()

elif mode==3:
	print ""
	categorias_amigos()	
	
elif mode==4: 
	print ""
	listar_canais(url)

elif mode==5: 
	listar_videostxt(url)
	
elif mode==6:
	player_youtube(url)

elif mode==7:
    print ""
    listar_categorias()	
	
elif mode==8:
    print ""
    canais_master(name,url,iconimage)
	
elif mode==9:
    print ""
    series_e_desenhos_24hrs()	
	
elif mode==10:
    print ""
    player_master(name,url,iconimage)
	
elif mode==11:
    print ""
    player_series_e_desenhos_24hrs(name,url,iconimage)	
elif mode==1000: 
	abrirDefinincoes()
xbmcplugin.endOfDirectory(int(sys.argv[1]))