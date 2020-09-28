function domainName(url){
  var subURL = url.split('.')

  if(subURL[0].includes('www') == false){
      domain = subURL[0].replace(/http:\/\/|https:\/\//, '')
  } 
  else{
      domain = subURL[1]
  }
  
  return domain
}
