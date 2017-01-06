'use strict';

var Ajax = function (){
  this.APIEndpoint = 'http://localhost:3000/';

  	this.getPlaylists = function(callback) {
  		this.open('GET', 'playlists', false, callback);
  	}

  	this.open = function(method, resource, data, callback) {
  		var xhr = new XMLHttpRequest();
  		data = (data) ? data : null;
  		xhr.open( method, this.APIEndpoint + resource )
      console.log(this.APIEndpoint + resource)

  		if( method !== 'DELETE' ) {
  			xhr.setRequestHeader('Content-Type', 'application/json');
  		}

      console.log(JSON.stringify(data))
  		xhr.send( JSON.stringify(data) );
  		xhr.onreadystatechange = function (rsp) {
  			if( xhr.readyState === XMLHttpRequest.DONE ) {
  				callback( JSON.parse(xhr.response) );
  			}
  		}
  	}
}
