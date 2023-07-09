

try:
	import ui
	from objc_util import *
	import os
except:
	pass
	


def safari_in_app_view (the_url):
		
	#========= SFSafariViewController to allow Safari extension in WebView
	def safariViewControllerDidFinish_(_self, _cmd, _controller):
		global SFSafariViewController_uiview
		#print('SafariViewControllerDidFinish_')
		SFSafariViewController_uiview.close()
	
	methods = [safariViewControllerDidFinish_,]
	protocols = ['SFSafariViewControllerDelegate']
	try:
			MySFSafariViewControllerDelegate = ObjCClass('MySFSafariViewControllerDelegate')
	except:
		MySFSafariViewControllerDelegate = create_objc_class('MySFSafariViewControllerDelegate', methods=methods, protocols=protocols)
	
	
	@on_main_thread	
	def MySFSafariViewController(url, w=None, h=None, local=None, popover_location=None, reader=False):
		global SFSafariViewController_uiview
		uiview = ui.View()
		uiview.background_color = 'white'
		uiview.present('fullscreen',hide_title_bar=True)
			
		# SFSafariViewController only accepts http: or https:,  not file:
		# thus, in this case, we need to create a local server
		ns_url = nsurl(url)
	
		SFSafariViewControllerConfiguration = ObjCClass('SFSafariViewControllerConfiguration').alloc().init()
		#
		SFSafariViewControllerConfiguration.setEntersReaderIfAvailable_(reader)
		SFSafariViewController = ObjCClass('SFSafariViewController').alloc().initWithURL_configuration_(ns_url,SFSafariViewControllerConfiguration)
		#print(dir(SFSafariViewController))
			
		# Use new delegate class:
		delegate = MySFSafariViewControllerDelegate.alloc().init()
		SFSafariViewController.delegate = delegate		
		SFSafariViewController.setModalPresentationStyle_(3)
		SFSafariViewController_uiview   = uiview		# used by delegate
		
		objc_uiview = ObjCInstance(uiview)
		SUIViewController = ObjCClass('SUIViewController')
		vc = SUIViewController.viewControllerForView_(objc_uiview)	
	
		vc.presentViewController_animated_completion_(SFSafariViewController, True, None)
	
	MySFSafariViewController(the_url, 900, 700)


if __name__ == "__main__":
	url = 'https://apple.com'
	safari_in_app_view(url)