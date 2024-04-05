function backend(endpoint, params) {
    return fetch("http://127.0.0.1:5000/" + endpoint + "?" + serialize(params)).then((response) => response.json());
}

function serialize(params) {
    return  new URLSearchParams(params).toString();
}

function setToken(token) {
    var expiration_date = new Date();
    expiration_date.setFullYear(expiration_date.getFullYear() + 1);
    
    var cookie = "token=" + token + "; path=/; expires=" + expiration_date.toUTCString();

    document.cookie = cookie;
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }