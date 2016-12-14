let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://444.hu/feed', true); // Also try http://444.hu/feed
httpRequest.send(null);
httpRequest.onreadystatechange = console.log;
