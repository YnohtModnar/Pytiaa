
  $('.slideshow').hide();
  $('.explanation').hide();
  var id = 0;
  var div = 0;
  var end = false;
  var play = false;
  $("#"+div).show();
  $("#"+div+"_exp").show();
  $("#"+div).children("div").hide();
  $('#'+div+' > .'+id).show();

  $("#go").click(function(){
    play = true;
    $("#go").hide();
    //$(".slideshow > div:gt(0)").hide();
    $('.slideshow').hide();
    $("#"+div).show();
    setInterval(function() {
      if($("#"+div).children("div").length>id && play){
        $('#'+div+' > .'+(id-1)).hide();
        $('#'+div+' > .'+id).show();
        id++;
      }
    },  400);
  });

  function check(){
    if(div==$("#block_content").children(".slideshow").length-1){
      $("#next").hide();
    }else{
      $("#next").show();
    }
    if(div==0){
      $("#prev").hide();
    }else{
      $('#prev').show();
    }
  }

  check();

  $("#next").click(function(){
    div++;
    play = false;
    id = 0;
    $("#go").show();
    $('.slideshow').hide();
    $('.explanation').hide();
    $("#"+div).show();
    $("#"+div+"_exp").show();
    check();
  });
  $("#prev").click(function(){
    div--;
    play = false;
    id = 0;
    $("#go").show();
    $('.slideshow').hide();
    $('.explanation').hide();
    $("#"+div).show();
    $("#"+div+"_exp").show();
    check();
  });

  $(document).ready(function(){
    var j = 0;
    for(var i = 0; i<$("#block_content").children(".explanation").length;i++){
      jQuery.get('http://localhost:8000/static/img/kmeans/'+i+'/exp.html', ajout).done(function(){
        j++;
      });

    }
    function ajout(data) {
      $("#"+j+"_exp").html(data);
    }
  });
