function myMap() {
  var mapCanvas = document.getElementById("map");
  var myCenter = new google.maps.LatLng(13.083174267450966, 80.27044884740279); 
  var mapOptions = {center: google.maps.LatLng(13.041673863527596, 80.2339330970405), zoom: 13};
  var map = new google.maps.Map(mapCanvas,mapOptions);
  var marker = new google.maps.Marker({
    position: myCenter,
  });
  marker.setMap(map);
}