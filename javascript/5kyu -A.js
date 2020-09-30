//Link -> https://www.codewars.com/kata/514a024011ea4fb54200004b

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
