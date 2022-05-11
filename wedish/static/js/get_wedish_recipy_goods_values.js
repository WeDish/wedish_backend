$(document).on('change', 'select[id^=id_menuitem_set]', function () {
    let _this = $(this);
    let selectedVal = $(this).val();
    $.ajax({
        url: '/wedish_recipy/good/' + pk + '/',
        type: "POST", 
        data: {dataVal: selectedVal},
        success: function(res){
           console.log(res);
          //  $(_this).closest('tr').find('vTextField').val('hjkgkj');
        }
        ,
          errors: function(e) {
          alert(e);
        }
      });
});
