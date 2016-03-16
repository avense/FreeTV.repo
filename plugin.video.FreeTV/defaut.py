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

versao = '2.0.0'
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
	addDir('[B]Canais TV[/B]','-',2,'http://avensat.com/Trexx/LogosEntrada/1.png')
	addDir('[B]Canais TDT[/B]','-',3,'http://avensat.com/Trexx/LogosEntrada/2.png')
	addDir('Este addon é Free nao somos obrigados a ter nada a funcionar','',2,'http://avensat.com/Trexx/LogosEntrada/3.png')
	addDir('DesportoFree','-',9,'http://avensat.com/Trexx/LogosCategorias/freesport.png')
	addDir('Filmes Online','-',12,'http://avensat.com/Trexx/LogosEntrada/filme.png')
	
def  categorias():
	check_login = login()
	if check_login:
		addDir('[B]Eventos[/B]','http://avensat.com/Trexx/Listas/eventos.txt',4,'http://avensat.com/Trexx/LogosCategorias/coming.png')
		addDir('[B]Portugueses[/B]','http://avensat.com/Trexx/Listas/pts.txt',4,'http://avensat.com/Trexx/LogosCategorias/Portugal.png')
		addDir('[B]Desporto[/B]','http://avensat.com/Trexx/Listas/desporto.txt',4,'http://avensat.com/Trexx/LogosCategorias/desporto.png')
		addDir('[B]Musica[/B]','http://avensat.com/Trexx/Listas/musica.txt',4,'http://avensat.com/Trexx/LogosCategorias/musica.png')
		addDir('[B]Documentários[/B]','http://avensat.com/Trexx/Listas/documentarios.txt',4,'http://avensat.com/Trexx/LogosCategorias/documentari.png')
		addDir('[B]Filmes[/B]','http://avensat.com/Trexx/Listas/filmes.txt',4,'http://avensat.com/Trexx/LogosCategorias/movies.png')
		addDir('[B]Infantil[/B]','http://avensat.com/Trexx/Listas/banda_desenhada.txt',4,'http://avensat.com/Trexx/LogosCategorias/cartoon.png')
		addDir('[B]Praias[/B]','http://avensat.com/Trexx/Listas/praias_de_portugal_-webcam-.txt',4,'http://avensat.com/Trexx/LogosCategorias/beach.png')
		addDir('[B]Radios[/B]','http://avensat.com/Trexx/Listas/radios_de_portugal.txt',4,'http://avensat.com/Trexx/LogosCategorias/radio.png')
		addDir('[B]Canais Plexus[/B]','http://avensat.com/Trexx/Listas/plexus.txt',4,'http://avensat.com/Trexx/LogosCategorias/plexus.png')
		addDir('[B]Futebol No Estrangeiro[/B]','http://avensat.com/Trexx/Listas/jogos_canais_estrangeiros.txt',4,'http://avensat.com/Trexx/LogosCategorias/world_sport.png')
	else:
		addDir('[B]Alterar Definições[/B]','http://pastebin.com/raw/JSxSwLgT',1000,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
		addDir('[B]Entrar novamente[/B]','',None,'http://www.reversamag.com/wp-content/uploads/2016/01/talk-show-lgbt.jpg')
	    
def categorias_amigos():
		addDir('TDT Portugal','http://avensat.com/Trexx/ListaFree/freept.txt',4,'http://www.atelevisao.com/wp-content/uploads/2013/09/imagesCA7P4VOJ.jpg')
		
def canais_sport():
		addDir('Desporto Free','http://avensat.com/Trexx/ListaFree/freesport.txt',4,'http://avensat.com/Trexx/LogosCategorias/freesport.png')
		
def filmes_online():
		addDir('Filmes Dublados BR','http://avensat.com/Trexx/ListaFree/Filmes.txt',4,'http://avensat.com/Trexx/LogosEntrada/filme.png')
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
    canais_sport()	
	
elif mode==10:
    print ""
    player_master(name,url,iconimage)
	
elif mode==11:
    print ""
    player_series_e_desenhos_24hrs(name,url,iconimage)
	
elif mode==12:
	print ""
	filmes_online()
	
elif mode==1000: 
	abrirDefinincoes()
xbmcplugin.endOfDirectory(int(sys.argv[1]))