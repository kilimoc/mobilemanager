var tempwin = win = window; while (tempwin != tempwin.top) { try { if (tempwin.frameElement) { win = tempwin.parent; } } catch (e) { } tempwin = tempwin.parent; }
if (!win.__TG_BOOT) {
    function e(v) { var s = encodeURIComponent(v); return s.replace(/%(?![0-9a-fA-F]{2})/g, "%25"); } function h() { return e((window.location.href || '').split("?")[0].split("#")[0]); }
    win.__TG_BOOT = 1; var tgHost = (win.location.protocol == "https:" ? "https:" : "http:") + "//services.trugaze.io"; var s = document.createElement('script'); s.type = 'text/javascript'; s.async = true; s.src = tgHost + '/init?appId=PHWP7UVG&h=' + h() + '&t=' + +new Date(); var x = win.document.getElementsByTagName('script')[0]; x.parentNode.insertBefore(s, x);
}

